import time

def loggear(que):
    f = open("palabra_elegida.txt", "a")
    f.write("[" + str(time.ctime()) + "]\t" + str(que) + "\n")
    f.close()

def loggear_puntaje(intentos_restantes, tiempo_restante, puntaje_final):
    loggear("tiempo restante:    " + str(tiempo_restante) + "s")
    loggear("intentos restantes: " + str(intentos_restantes))
    loggear("puntos:             " + str(puntaje_final))