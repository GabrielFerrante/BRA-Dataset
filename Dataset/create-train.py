import os
from re import L



def createTrain():
    # o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
    imagens = []

    animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]

    for item in animals:
        os.chdir(os.path.join("imagens", item))
        
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".jpg"):
                oldName = os.path.dirname(os.path.abspath(__file__))+ "/" + filename
                if filename.count(item) > 1:
                    codigo = filename.split(item)[len(filename.split(item))-1]
                    print(codigo)
                    filename = item + codigo
                    
                    newName = os.path.dirname(os.path.abspath(__file__))+ "/" + filename
                    
                    
                else:
                    newName = os.path.dirname(os.path.abspath(__file__))+ "/" + filename

                os.rename(oldName, newName)

                imagens.append(f"data/imagens/" + filename)

            
            if filename.endswith(".txt"):

                if filename.count("classes") == 0:
                    
                    oldName = os.path.dirname(os.path.abspath(__file__))+ "/" + filename

                    if filename.count(item) > 1:
                        codigo = filename.split(item)[len(filename.split(item))-1]
                        filename = item + codigo
                        
                        newName = os.path.dirname(os.path.abspath(__file__))+ "/" + filename
                    else:
                        filename = item + filename
                        newName = os.path.dirname(os.path.abspath(__file__))+ "/" + filename

                    os.rename(oldName, newName)
                    imagens.append(f"data/imagens/" + filename)
            

                
                
                
            
        os.chdir("..")

        with open("train.txt", "w") as outfile:
            for img in imagens:
                outfile.write(img)
                outfile.write("\n")
            outfile.close()
        os.chdir("..")

createTrain()