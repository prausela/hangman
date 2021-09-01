import os
import puntaje

def pedir_letra():
    letra = str(input("LETRA: "))
    while len(letra) == 0 or not letra[0].isalpha():
        print()
        print("DEBE INGRESAR UNA LETRA ASCII")
        letra = str(input("LETRA: "))
    return letra[0].upper()

def mostrar_intento(palabra_oculta, intentos_restantes, letras_usadas):
    print()
    print("TU PALABRA:")
    print(palabra_oculta)
    print()
    print("INTENTOS RESTANTES: %s"%(intentos_restantes))
    print()
    print("LETRAS USADAS:")
    print(letras_usadas)
    print()

def mensaje_de_victoria(palabra_elegida, intentos_restantes, letras_usadas, puntos):
    print()
    print("ADIVINASTE LA PALABRA!!")
    mostrar_intento(palabra_elegida, intentos_restantes, letras_usadas)
    print("TU PUNTAJE:")
    print(puntos)
    print()

def mensaje_de_derrota(palabra_elegida, intentos_restantes, letras_usadas):
    print()
    print("BUEN INTENTO!!")
    print("FROM FAILURE YOU LEARN, FROM SUCCESS.. MEH NOT SO MUCH")
    mostrar_intento(palabra_elegida, intentos_restantes, letras_usadas)

def limpiar_pantalla():
  if os.name == 'posix':
    os.system('clear')
  else:
    os.system('cls')