##En este capítulo crearás el juego “Adivina el Número”. La computadora pensará un número aleatorio
# entre 1 y 20, y te pedirá que intentes adivinarlo. La computadora te dirá si cada intentoes
# muy alto o muy bajo. Tú ganas si adivinas el número en seis intentos o menos



from random import randint

x=(input("Como te llamas? "))
print("Hola "+x)
jugar=input("Quieres Jugar? Si\n No \n")
while jugar == "si" :
  mas=int(input("intenta adivinar el numero que estoy pensando entre el 1 y el 10 \n Cual es el numero?"))
  v=randint(1,10)
  if v == mas:
    print("Correcto el numero era", v)
  else:
    print("Incorrecto el numero era ", v)
    jugar=input("Quieres Jugar? Si\n No \n")

