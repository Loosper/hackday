import os

def nameSend(fileName):
    with open("packets/FileName.txt", "w") as nameFile:
        nameFile.write(fileName)



def send(filePackage, fileNum):
    name = "packets/pack" + str(fileNum) + ".bin"
    with open(name, "wb") as pack:
        pack.write(filePackage)
    
    
def splitFile(fileName):
    nameSend(fileName)
    with open(fileName, "rb") as file:
        buf = file.read(10240)
        count = 0
        while (buf):
            send(buf, count)
            count +=1
            buf = file.read(10240)
        for i in range (count-1):
            os.remove("packets/pack"+str(i)
                      +".bin")
