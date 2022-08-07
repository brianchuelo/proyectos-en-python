from random import choice

palabras =["helicoptero", "avioneta","helefante","raton"]
letras_correctas= []
letras_incorrectas=[]
intentos = 6
aciertos=0
juego_terminado= False
print("*" * 100)
nombre=input("Hola, 👋≧◉ᴥ◉≦\nPor favor dime tu nombre: ")


def elegir_palabra(lista):
    palabra_elegida=choice(lista)
    # elegimos una palabra al azar de la lista con el metodo chois

    letras_unicas= len(set(palabra_elegida))
    #aca guardamos en una variable la cantidad de letras unicas poniendola dentro de un set que hace que tengamos una cantidad de elementos como de palabras
    return palabra_elegida, letras_unicas


def pedir_letra():
    letra_elegida= " "
    es_valida = False
    abecedario = "abcdefghijklmñopqrstuwvxzy"
#comprovamos que la letra sea valida con un bucle while
    while not es_valida:
        letra_elegida=input(f"elige una letra {nombre}:").lower()
        #comprovamos que la letra elegida este en el abecedario y que sea una sola letra y no mas
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida=True
        else:
            print("no has elegido una letra correcta:")
        return letra_elegida

def mostrar_tablero(palabra_elegida):
    lista_oculta = []
    #hacemos que el bucle for revise la palabra eelgida y agregue a letras correcta a la lista oculta
    for letra in palabra_elegida:
        if letra in letras_correctas:
            lista_oculta.append(letra)
            #si la letra no es correcta agrega un guion, para que se muestre en pantalla
        else:
            lista_oculta.append("-")

    print(" ".join(lista_oculta))

def chequear_letra(letra_elegida,palabra_oculta,vidas,coincidencias):
    fin =False
    #si la letra elegida es esta en la palabra oculta, la agregamos a la lista de letras correcta
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencias +=1

    #si la letra elegida no esta en la palabra oculta, la agregamos a la lista de palabras incorrectas
    else:
        letras_incorrectas.append(letra_elegida)
        vidas-=1
    #verificamos si el usuario se quedo sin vidas o si gano el juego
    if vidas == 0:
        fin= perder()
    elif coincidencias==letras_unicas:
        fin=ganar(palabra_oculta)
    return vidas,fin,coincidencias

def perder():
    print("JAJAJAJA te quedaste sin vidas ☠☠☠ ( ˘︹˘ ) ☠☠☠")
    print("la palabra oculta era " + palabra)
    return True

def ganar(palabra_descubierta):
    mostrar_tablero(palabra_descubierta)
    print(f"felicitaciones {nombre}!! ganaste ¯\_( ͡❛‿‿‿ ͡❛)_/¯ ✌ ✌".upper())
    return True

palabra,letras_unicas=elegir_palabra(palabras)

while not juego_terminado:
    print("\n" + "*"*100)
    mostrar_tablero(palabra)
    print("\n" + "*"*100)
    print("letras incorrectas: " + "☠".join(letras_incorrectas))
    print(f"vidas {intentos} ❤")
    letra=pedir_letra()
    print("\n" + "*" * 100)

    intentos,terminado,aciertos =chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado
