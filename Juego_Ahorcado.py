import random 
imagenes=["""
+---+
 | |
 |
 |
 |
 |
=========""",'''
+---+
 | |
 O |
 |
 |
 |
=========''', '''
+---+
 | |
 O |
 | |
 |
 |
=========''', '''
+---+
 | |
 O |
/| |
 |
 |
=========''', '''
 +---+
 | |
 O |
/|\ |
 |
 |
=========''', '''
+---+
 | |
 O |
/|\ |
/  |
 |
 =========''', '''
+---+
 | |
 O |
/|\ |
/ \ |
 |
=========''']

words_rando=["cangrejo", "perro", "gato", "cabra"]
def word_selected(words_rando):
  words_rando=random.choice(words_rando)
  return  words_rando
word_selected(words_rando)

def tablero (imagenes,letras_incorrectas,elected_word,letras_correctas):
  print(imagenes [len(letras_incorrectas)])
  print()

  print("letras incorrectas:", end=" ")
  for i in letras_incorrectas:
    print(i,end="")
  print()

  espacios_vacios="_" * len(elected_word)

  for i in range(len(elected_word)):
    if elected_word[i] in letras_correctas:
      espacios_vacios= espacios_vacios[:i] + elected_word[i] + espacios_vacios[i+1:]
  for x in espacios_vacios:
    print(x, end="")
  print()

def customer_letter(letras_probadas):
  while True:
    print("Ingrese una letra")
    letter=input()
    letter=letter.lower()
    if len(letter) !=1:
      print("ingresa solo una letra")
    elif letter in letras_probadas:
      print("ya la probaste")
    elif letter not in "abcdefghijklmnñopuqrvstxyz":
      print("tiene que se una letra")
    else:
      return letter

def jugar_n():
  print("Quieres jugar nuevamente")
  return input().lower().startswith("s")
  
 
elected_word= word_selected(words_rando)
letras_incorrectas=""
letras_correctas= ""
juego_terminado=False

while True:
  tablero (imagenes,letras_incorrectas,elected_word,letras_correctas)
  letter = customer_letter(letras_incorrectas+letras_correctas)
  if letter in elected_word:
    letras_correctas=letras_correctas + letter
    encontrado_letras=True
    for i in range(len(elected_word)):
      if elected_word[i] not in letras_correctas:
        encontrado_letras=False
        break
    if encontrado_letras:
      print("has ganado, la palabra era "+elected_word)
      juego_terminado=True
  
  else:
    letras_incorrectas= letras_incorrectas + letter
    if len(letras_incorrectas)==len(imagenes)-1:
      tablero (imagenes,letras_incorrectas,elected_word,letras_correctas)
      print("perdiste")
      juego_terminado=True

  if juego_terminado:
    if jugar_n():
      letras_incorrectas=""
      letras_correctas=""
      elected_word=word_selected(words_rando)
      juego_terminado=False
    else:
      break