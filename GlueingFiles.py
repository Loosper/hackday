import os
count = 0
fileName = open("packets/FileName.txt", "r")

with open("packets/"+fileName.read(), "ab") as fullFile:
    while True:
        try:
            name = "packets/pack" + str(count) + ".bin"
            with open(name, "rb") as file:
                fullFile.write(file.read())
            count += 1
        except FileNotFoundError:
            try:
                os.remove("FileName.txt")
                for i in range (count):
                    os.remove("packets/pack"+str(i)+".bin")
                    count -= 1
            except FileNotFoundError:
                break
