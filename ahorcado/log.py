import time

def log(que):
    f = open("palabra_elegida.txt", "a")
    f.write("[" + str(time.ctime()) + "]\t" + str(que) + "\n")
    f.close()