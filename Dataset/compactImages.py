from zipfile import ZipFile
import os

def compactWithYOLOAnn():


    zipObj = ZipFile('zipWithObjs.zip', 'w')

    animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]

    for item in animals:
        os.chdir(os.path.join("images", item))
            
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".jpg"):
                
                zipObj.write(filename)
            
            if filename.endswith(".txt"):
                zipObj.write(filename)

        
        os.chdir("..")
        os.chdir("..")

    zipObj.close()

def compactWithXMLAnn():
    zipObj = ZipFile('zipWithObjsXML.zip', 'w')

    animals = ["anta", "jaguarundi", "loboGuara", "oncaParda", "tamanduaBandeira"]

    for item in animals:
        os.chdir(os.path.join("images", item))
            
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".jpg"):
                
                zipObj.write(filename)
        
        os.chdir(os.getcwd()+"/XML")
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".xml"):
                zipObj.write(filename)

        os.chdir("..")
        os.chdir("..")
        os.chdir("..")

    zipObj.close()

#Choice the function executable
compactWithYOLOAnn()