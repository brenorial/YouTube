# YouTube Downloader com Barra de Progresso

Este projeto é um aplicativo de desktop em Python para baixar vídeos e áudios do YouTube, utilizando uma interface gráfica moderna com `customtkinter` e exibindo uma barra de progresso durante o download.

## Bibliotecas e Aplicativos Necessários

1. **Python**: Certifique-se de ter o Python instalado em sua máquina.
2. **yt_dlp**: Para gerenciar downloads do YouTube.
3. **customtkinter**: Para criar a interface gráfica.
4. **Pillow**: Para manipulação de imagens.
5. **ffmpeg**: Necessário para conversão de vídeo e áudio.

## Instalação e Configuração do FFmpeg

Para utilizar o `ffmpeg` no seu projeto, é necessário instalá-lo e configurá-lo corretamente no seu sistema. Siga os passos abaixo para realizar a instalação e configurar o `ffmpeg` como variável de ambiente.

### 1. Baixando o FFmpeg

1. **Acesse o site oficial do FFmpeg**: [FFmpeg Downloads](https://ffmpeg.org/download.html).
2. **Escolha o seu sistema operacional** e baixe a versão adequada:
   - **Windows**: Acesse a seção "Windows" e baixe o arquivo executável do FFmpeg.
   - **Mac**: Acesse a seção "Mac" e use o Homebrew para instalar (`brew install ffmpeg`).
   - **Linux**: Acesse a seção "Linux" e use o gerenciador de pacotes da sua distribuição para instalar (`sudo apt install ffmpeg` para distribuições baseadas no Debian/Ubuntu).

### 2. Instalando o FFmpeg

#### Windows

1. **Extraia o arquivo ZIP**: Após o download, extraia o conteúdo do arquivo ZIP para um diretório de sua escolha, por exemplo, `C:\ffmpeg`.
2. **Renomeie a pasta**: Certifique-se de que a pasta extraída tem o nome `ffmpeg` e contém subpastas como `bin`, `doc`, `presets`, etc.
