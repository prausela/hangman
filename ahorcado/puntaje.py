frecuencia_letras = {
    "A" : 13,
    "B" : 2,
    "C" : 5,
    "D" : 6,
    "E" : 14,
    "F" : 1,
    "G" : 1,
    "H" : 1,
    "I" : 6,
    "J" : 1,
    "K" : 0,
    "L" : 5,
    "M" : 3,
    "N" : 7,
    "Ñ" : 1,
    "O" : 9,
    "P" : 3,
    "Q" : 1,
    "R" : 7,
    "S" : 8,
    "T" : 5,
    "U" : 4,
    "V" : 1,
    "W" : 0,
    "X" : 0,
    "Y" : 1,
    "Z" : 1
}

import operator
max_frec = max(frecuencia_letras.items(), key=operator.itemgetter(1))[0]
max_frec = frecuencia_letras[max_frec]

puntaje_letras = dict()
for i, e in enumerate(frecuencia_letras):
  puntaje_letras[e] = max_frec - frecuencia_letras[e]

def puntaje_palabra(palabra, intentos_restantes, tiempo_restante, pista):
  global puntaje_letras
  puntaje = 0
  for i in range(0, len(palabra)):
    puntaje += puntaje_letras[palabra[i]]
  if not pista:
    puntaje *= 2
  puntaje += 10*intentos_restantes
  puntaje += tiempo_restante
  return puntaje