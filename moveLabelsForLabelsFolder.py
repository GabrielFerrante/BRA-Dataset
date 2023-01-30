import os

def moveLabels(folder):
    pasta = f'./Dataset/images/{folder}'
    pastaDestino = f'./Dataset/labels/{folder}'
    
    for diretorio, subpastas, arquivos in os.walk(pasta):
        if len(arquivos) == 0:
            print("N tem imagens no images")
        else:
            for arquivo in arquivos:
                if arquivo.endswith(".txt"):
                    os.replace(f"{pasta}/{arquivo}", f"{pastaDestino}/{arquivo}")

moveLabels('train')
moveLabels('val')


