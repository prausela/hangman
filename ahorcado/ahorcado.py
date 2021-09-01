import random
import pantalla
import time
import puntaje
from sortedcontainers import SortedSet

palabras = [
    "PROGRAMADORA"          , "HARVARD"         , "LIQUID PAPER"    , "NUMEROS PRIMOS"  , "PESTICIDA",
    "CAMBRIDGE"             , "HIDDEN FIGURES"  , "MICROSOFT WORD"  , "ENCRIPTADO"      , "METALES",
    "ESTRELLAS"             , "SISMO"           , "IBM"             , "ASTROFISICA"     , "SPACEX",
    "PROTEINAS"             , "ENZIMAS"         , "INSULINA"        , "MASCARA DE GAS"  , "BUG",
    "PRINCIPIA MATHEMATICA" , "ASME"
  ]

class PalabraOculta:
  def __init__(self, palabra):
    self.lista_interna = convertir_palabra_elegida_a_lista(palabra)

  def __len__(self):
      return len(self.lista_interna)

  def __delitem__(self, index):
      self.lista_interna.__delitem__(index)

  def insert(self, index, value):
      self.lista_interna.insert(index, value)

  def __setitem__(self, index, value):
      self.lista_interna.__setitem__(index, value)

  def __getitem__(self, index):
      return self.lista_interna.__getitem__(index)

  def append(self, value):
    self.insert(len(self) + 1, value)

  def __repr__(self):
    representacion = ""
    for i in range(0, len(self.lista_interna)):
      if i != 0:
        representacion += "    "
      representacion += " ".join(self.lista_interna[i])
    return representacion

  def __str__(self):
    return self.__repr__()

class LetrasUsadas:
  def __init__(self):
    self.letras_usadas  = SortedSet()

  def agregar_letra(self, letra):
    if letra in self.letras_usadas:
      return False
    self.letras_usadas.add(letra)
    return True

  def __repr__(self):
    return " ".join(self.letras_usadas)

  def __str__(self):
    return self.__repr__()

def convertir_palabra_elegida_a_lista(palabra_elegida):
  lista = []
  palabras = palabra_elegida.split(" ")

  for i in range(0, len(palabras)):
    lista.append(list(palabras[i]))
  return lista

def guionar_palabra_elegida(palabra_elegida):
  for i in range(0, len(palabra_elegida)):
    for j in range(0, len(palabra_elegida[i])):
      palabra_elegida[i][j] = "_"

def obtener_posiciones_de_las_letras(palabra_elegida):
  posiciones = dict()
  for i in range(0, len(palabra_elegida)):
    for j in range(0, len(palabra_elegida[i])):

      if not palabra_elegida[i][j] in posiciones:
        posiciones[palabra_elegida[i][j]] = []
        for _ in range(0, len(palabra_elegida)):
          posiciones[palabra_elegida[i][j]].append([])

      posiciones[palabra_elegida[i][j]][i].append(j)

  return posiciones

def intentar_con_letra(palabra_elegida, posiciones_de_todas, letra):
  if not letra in posiciones_de_todas:
    return False
  posiciones = posiciones_de_todas[letra]
  for i in range(0, len(posiciones)):
    for j in range(0, len(posiciones[i])):
      palabra_elegida[i][posiciones[i][j]] = letra
  return True


palabra_azar        = random.choice(palabras)
palabra_elegida     = PalabraOculta(palabra_azar)
palabra_oculta      = PalabraOculta(palabra_azar)
posiciones          = obtener_posiciones_de_las_letras(palabra_elegida)
intentos_restantes  = 5
letras_usadas       = LetrasUsadas()

f = open("palabra_elegida.txt", "a")
f.write("[" + str(time.ctime()) + "]\t" + str(palabra_elegida) + "\n")
f.close()

guionar_palabra_elegida(palabra_oculta)

while len(posiciones) > 0 and intentos_restantes > 0:
  pantalla.limpiar_pantalla()
  pantalla.mostrar_intento(palabra_oculta, intentos_restantes, letras_usadas)

  letra   = pantalla.pedir_letra()
  acierto = intentar_con_letra(palabra_oculta, posiciones, letra)
  if acierto:
    posiciones.pop(letra)
  else:
    intentos_restantes -= 1

  letras_usadas.agregar_letra(letra)

pantalla.limpiar_pantalla()
if len(posiciones) <= 0:
  puntos = puntaje.puntaje_palabra(str(palabra_elegida).replace(" ", ""))
  pantalla.mensaje_de_victoria(palabra_elegida, intentos_restantes, letras_usadas, puntos)
else:
  pantalla.mensaje_de_derrota(palabra_elegida, intentos_restantes, letras_usadas)

input()
