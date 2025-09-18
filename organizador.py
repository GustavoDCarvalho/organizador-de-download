
import os
import shutil

download_organizador = '/Users/gustavo/Downloads'  

tipos_arquivos = {
    'Imagens': ['.jpg', '.png', '.jpeg', '.gif'],
    'Documentos': ['.pdf', '.docx', '.txt'],
    'Vídeos': ['.mp4', '.mov'],
    'Áudios': ['.mp3', '.wav'],
    'Compactados': ['.zip', '.rar']
}
for pasta in tipos_arquivos:
    caminho = os.path.join(download_organizador, pasta)
    if not os.path.exists(caminho):
        os.mkdir(caminho)

for arquivo in os.listdir(download_organizador):
    caminho_arquivo = os.path.join(download_organizador, arquivo)

    if os.path.isfile(caminho_arquivo):
        _, extensao = os.path.splitext(arquivo)
        movido = False

        for categoria, extensoes in tipos_arquivos.items():
            if extensao.lower() in extensoes:
                destino = os.path.join(download_organizador, categoria, arquivo)
                shutil.move(caminho_arquivo, destino)
                movido = True
                break

        if not movido:
            outros = os.path.join(download_organizador, 'Outros')
            if not os.path.exists(outros):
                os.mkdir(outros)
            shutil.move(caminho_arquivo, os.path.join(outros, arquivo))
