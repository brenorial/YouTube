import yt_dlp as youtube_dl
import os
import threading
import customtkinter
from tkinter.filedialog import askdirectory
from PIL import Image


# Funções de download
def baixar_video(link, destino, progresso_callback=None):
    try:
        print(f"Tentando baixar o vídeo do link: {link}")
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'progress_hooks': [lambda d: progresso_callback(d) if progresso_callback else None]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            arquivo = ydl.prepare_filename(info_dict)
        return f'Download do vídeo realizado!'
    except Exception as e:
        return f"Falha no download do vídeo: {str(e)}"


def baixar_audio(link, destino, progresso_callback=None):
    try:
        print(f"Tentando baixar o áudio do link: {link}")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(destino, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [lambda d: progresso_callback(d) if progresso_callback else None]
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)
            arquivo = ydl.prepare_filename(info_dict).replace('.webm', '.mp3').replace('.m4a', '.mp3')
        return f'Download realizado!'
    except Exception as e:
        return f'Falha no download do áudio: {str(e)}'


# Função para rodar o download em uma thread separada
def iniciar_download(func, link, destino, progresso_callback=None):
    def trabalho():
        msg = func(link, destino, progresso_callback)
        msg_lbl.configure(text=msg)
        # Esconder a barra de progresso após o download
        progress_bar.place_forget()

    # Iniciar a thread
    threading.Thread(target=trabalho, daemon=True).start()


# Função de callback para atualizar a barra de progresso
def atualizar_progresso(d):
    if d.get('status') == 'downloading':
        total_bytes = d.get('total_bytes')
        downloaded_bytes = d.get('downloaded_bytes')
        if total_bytes is not None and downloaded_bytes is not None:
            progresso = (downloaded_bytes / total_bytes) * 100
            print(f"Progresso: {progresso}%")  # Depuração
            progress_bar.set(progresso / 100)
            window.update_idletasks()
    elif d.get('status') == 'finished':
        print("Download concluído!")  # Depuração
        progress_bar.set(1.0)  # Completar a barra quando o download terminar
        window.update_idletasks()


# Configuração da interface gráfica
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()
window.geometry("550x300")
window.title("YouTube Downloader MP4 e MP3")

script_dir = getattr(window, '_MEIPASS', os.path.dirname(os.path.realpath(__file__)))
img_path = os.path.join(script_dir, r"C:/Users/Usuario/Documents/Python/YouTube Video/bg.png")

img = customtkinter.CTkImage(Image.open(img_path), size=(430, 510))
img_label = customtkinter.CTkLabel(window, image=img, text='')
img_label.place(x=-5, y=-160)


def baixarmp3():
    msg_lbl.configure(text="")
    link = str(link_entry.get())
    if not link:
        msg_lbl.configure(text="Por favor insira um link.")
        return
    destino = askdirectory()
    if not destino:
        msg_lbl.configure(text="Por favor selecione um diretório.")
        return
    progress_bar.set(0)  # Resetar a barra de progresso
    progress_bar.place(x=180, y=160)  # Mostrar a barra de progresso
    iniciar_download(baixar_audio, link, destino, atualizar_progresso)


def baixarmp4():
    msg_lbl.configure(text="")
    link = str(link_entry.get())
    if not link:
        msg_lbl.configure(text="Por favor insira um link.")
        return
    destino = askdirectory()
    if not destino:
        msg_lbl.configure(text="Por favor selecione um diretório.")
        return
    progress_bar.set(0)  # Resetar a barra de progresso
    progress_bar.place(x=180, y=160)  # Mostrar a barra de progresso
    iniciar_download(baixar_video, link, destino, atualizar_progresso)


def baixarambos():
    msg_lbl.configure(text="")
    link = str(link_entry.get())
    if not link:
        msg_lbl.configure(text="Por favor insira um link.")
        return
    destino = askdirectory()
    if not destino:
        msg_lbl.configure(text="Por favor selecione um diretório.")
        return
    progress_bar.set(0)  # Resetar a barra de progresso
    progress_bar.place(x=180, y=160)  # Mostrar a barra de progresso

    # Iniciar downloads em threads separadas
    iniciar_download(baixar_audio, link, destino, atualizar_progresso)
    iniciar_download(baixar_video, link, destino, atualizar_progresso)


link_entry = customtkinter.CTkEntry(window, placeholder_text='URL do Vídeo', width=355, height=28)
link_entry.place(x=170, y=15)

download_btn = customtkinter.CTkButton(window, text='Baixar MP3 e MP4', width=160, height=28, command=baixarambos)
download_btn.place(x=268, y=105)

mp4_btn = customtkinter.CTkButton(window, text='Baixar em MP4', width=160, height=28, command=baixarmp4)
mp4_btn.place(x=365, y=55)

mp3_btn = customtkinter.CTkButton(window, text='Baixar em MP3', width=160, height=28, command=baixarmp3)
mp3_btn.place(x=170, y=55)

# Adicionar a barra de progresso, inicialmente fora de vista
progress_bar = customtkinter.CTkProgressBar(window, width=340, height=20)
progress_bar.set(0)  # Certifique-se de que a barra de progresso comece em 0
progress_bar.place_forget()  # Inicialmente fora de vista

# Label para mensagens
msg_lbl = customtkinter.CTkLabel(window, text='', width=340, height=28)
msg_lbl.place(x=180, y=190)  # Ajustar a posição da label para mensagens

fonte = customtkinter.CTkFont(family='Helvetica', size=10)

texto = customtkinter.CTkLabel(window, text="Desenvolvido por Rial", font=fonte)
texto.place(x=300, y=260)

window.mainloop()
