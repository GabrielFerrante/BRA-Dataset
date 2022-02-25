import os




def createTrain(pasta):
    # o que o codigo abaixo faz: adiciona o nome e caminho de todos as fotos (.jpg) em um txt
    imagens = []
    os.chdir(os.path.join("imagens", pasta))
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".jpg"):
            imagens.append(f"imagens/{pasta}/" + filename)
    os.chdir("..")

    with open("train.txt", "w") as outfile:
        for img in imagens:
            outfile.write(img)
            outfile.write("\n")
        outfile.close()
    os.chdir("..")


animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]

for item in animals:
    createTrain(item)