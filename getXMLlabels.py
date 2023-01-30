import os


def navi(animal):
    pasta = f'./Dataset/images/{animal}/XML/'
    pastaDestino = f'./Dataset/PASCAL_annotation/'
    
    for diretorio, subpastas, arquivos in os.walk(pasta):
        if len(arquivos) == 0:
            print("N tem imagens no images")
        else:
            for arquivo in arquivos:
                if arquivo.endswith(".xml"):
                    os.replace(f"{pasta}/{arquivo}", f"{pastaDestino}/{arquivo}")


animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]    
for item in animals:
    navi(item)