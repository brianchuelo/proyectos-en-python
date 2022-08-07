from random import randint
vidas = 0
estimado = 0
aleatorio = randint(1,5)

print('*'*100)
nombre = input('ingresa tu nombre: ')
print('*'*100)
print(f"ok {nombre}, he pensado un numero del 1 al 100 para que adivines \n y tienes tan solo 8 intentos para adivinarlo, puedes ?? ")
print('*'*100)


while vidas <8 :
    estimado = int(input("ingrese su numero: "))
    vidas +=1
    if estimado not in range(1,101):
        print(f"{nombre}, tu numero no se encuentra en el rango del 1 al 100")
    elif estimado < aleatorio:
        print(f" mi numero es mas alto")
    elif estimado > aleatorio:
        print(f"mi numero es mas bajo")
    else:
        print(f"FELIZITACIONES!\n ganaste el juego {nombre}, en {vidas} intentos")
        break
if vidas >= 8:
    print(f"JAJAJAJAJA PERDISTE {nombre}, mi numero era {aleatorio}")






