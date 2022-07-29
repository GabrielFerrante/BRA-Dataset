import os
from re import L



def createTrain():
    # o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
    imagensTrain = []
    imagensValid = []

    animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]

    for item in animals:
        
        pasta = f'./images/{item}'
        for diretorio, subpastas, arquivos in os.walk(pasta):
            for arquivo in arquivos[:int(0.8 * len(arquivos))]:
                if arquivo.endswith(".jpg"):
                    imagensTrain.append(f"../Dataset/images/train/" + arquivo)
            
            for arquivo in arquivos[int(0.8 * len(arquivos)):]:
                if arquivo.endswith(".jpg"):
                    imagensValid.append(f"../Dataset/images/val/" + arquivo)

    with open("images/train.txt", "w") as outfile:
        for img in imagensTrain:
            outfile.write(img)
            outfile.write("\n")            
        outfile.close()
    
    with open("images/valid.txt", "w") as outfile:
        for img in imagensValid:
            outfile.write(img)
            outfile.write("\n")            
        outfile.close()
createTrain()
