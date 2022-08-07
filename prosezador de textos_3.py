print("*"*100)
#le pedimos el nombre al usuario
nombre = input("Hola, Por favor ingresa tu nombre: ")

print("*"*100)
#le pedimos el texto al usuario

texto = input(f"ok, {nombre} ingresa tu texto: ")
texto=texto.lower()

print("*"*100)
#creamos la lista donde vamos a almacenar las 3 letras y convertimos lo ingresado por el usuario en "minusculas" con lower
lista = []

print(f"Acontinuacion {nombre}, ingresaras las 3 letras que quieres analizar. ")
lista.append(input("primera letra: ").lower())
lista.append(input("segunda letra: ").lower())
lista.append(input("tercera letra: ").lower())

print("*"*100)
#creamos 3 variables y definimos cada una, contando la cantidad de letras en el texto con el metodo "count" con el index de la lista

print("cantidad de letras!".upper())
cantidad_letras1 = texto.count(lista[0])
cantidad_letras2 = texto.count(lista[1])
cantidad_letras3 = texto.count(lista[2])

print("*"*100)
#mostramos en pantalla el resultado del metodo count

print(f"se a encontrado la letra '{lista [0]}' repetida {cantidad_letras1} veces")
print(f"se a encontrado la letra '{lista [1]}' repetida {cantidad_letras2} veces")
print(f"se a encontrado la letra '{lista [2]}' repetida {cantidad_letras3} veces")

print("*"*100)
#zeparamos las palabras del texto individualmente y la almacenamos en una lista a cada una de elllas con el metodo "split"
#y mostramos en pantalla la cantidad total de palabras en la lista con el metodo "len"

print("cantidad de palabras!".upper())

palabras=texto.split()
print(f"hemos encontrado {len(palabras)} palabras en tu texto")

print("*"*100)
#mostramos la primera y ultima letra del texto con el metodo index

print("letras de inicio y fin!".upper())
primera_letra = texto[0]
ultima_letra = texto[-1]

print(f"{nombre}, la primera letra de su texto es '{primera_letra}' y la letra final '{ultima_letra}'")

print("*"*100)
#invocamos la lista de palabras creada y le aplicamos el metodo reverse para revertir el orden de la lista
#luego usamos el metodo join para unir esa lista en un conjuto de string con un espacio entre si

print("texto invertido".upper())

palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"bueno {nombre}, si ordenamos tu texto al revees va a decir: '{texto_invertido}'")

print("*"*100)
