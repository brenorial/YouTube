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

### Baixando o FFmpeg

1. **Acesse o site oficial do FFmpeg**: [FFmpeg Downloads](https://ffmpeg.org/download.html).
2. **Escolha o seu sistema operacional** e baixe a versão adequada:
   - **Windows**: Acesse a seção "Windows" e baixe o arquivo executável do FFmpeg.
   - **Mac**: Acesse a seção "Mac" e use o Homebrew para instalar (`brew install ffmpeg`).
   - **Linux**: Acesse a seção "Linux" e use o gerenciador de pacotes da sua distribuição para instalar (`sudo apt install ffmpeg` para distribuições baseadas no Debian/Ubuntu).

# Como Adicionar o FFmpeg às Variáveis de Ambiente

O `FFmpeg` é uma ferramenta de linha de comando para converter multimídia. Para usá-lo de qualquer lugar no seu sistema, você precisa adicionar o diretório do executável `ffmpeg` às variáveis de ambiente do sistema. Abaixo estão as etapas para Windows e macOS/Linux.

## Windows

1. **Baixe e Instale o FFmpeg**:
   - Vá até o site oficial do [FFmpeg](https://ffmpeg.org/download.html) e baixe a versão mais recente para Windows.
   - Extraia o arquivo ZIP baixado. Você deve encontrar uma pasta chamada `ffmpeg` com subpastas como `bin`, `doc`, etc.

2. **Copie o Caminho do Executável**:
   - Navegue até a pasta `bin` dentro da pasta `ffmpeg` que você extraiu. O caminho deve ser algo como `C:\caminho\para\ffmpeg\bin`.
   - Copie este caminho.

3. **Adicione o Caminho às Variáveis de Ambiente**:
   - Pressione `Win + R`, digite `sysdm.cpl` e pressione Enter para abrir as Propriedades do Sistema.
   - Vá para a aba `Avançado` e clique no botão `Variáveis de Ambiente`.
   - Na seção `Variáveis do sistema`, encontre e selecione a variável `Path`, e clique em `Editar`.
   - Clique em `Novo` e cole o caminho copiado (por exemplo, `C:\caminho\para\ffmpeg\bin`).
   - Clique em `OK` para fechar todas as janelas.

4. **Verifique a Instalação**:
   - Abra o Prompt de Comando (`cmd`).
   - Digite `ffmpeg -version` e pressione Enter. Se o FFmpeg estiver corretamente instalado, você verá informações sobre a versão do FFmpeg.
