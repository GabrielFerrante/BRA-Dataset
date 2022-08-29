import os
import numpy as np
from PIL import Image




def average(listL, listA):
    return ((sum(listL)/ len(listL)), (sum(listA)/ len(listA)))

def getSizes():

    animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]

    

    for item in animals:
            larguras = []
            alturas = []
            os.chdir(os.path.join("images", item))
                
            for filename in os.listdir(os.getcwd()):
                if filename.endswith(".jpg"):
                    im = Image.open(filename)
                    l, a = im.size
                    larguras.append(l)
                    alturas.append(a)
            

            tupla = average(larguras, alturas)

            print(f'O valor médio de largura para a classe {item} é de: {int(tupla[0])}\nVariância de: {np.var(larguras)}\nDesvio padrão de: {np.std(larguras)}')
            print(f'O valor médio de altura para a classe {item} é de: {int(tupla[1])}\nVariância de: {np.var(alturas)}\nDesvio padrão de: {np.std(alturas)}')

            

            os.chdir("..")
            os.chdir("..")

    

getSizes()