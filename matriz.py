import random


matriz=[]
filas=5;columnas=5
def elementos():
    for inicializar in range(filas):
        matriz.append([0]*columnas)

    for i in range(filas):
        for j in range(columnas):
            matriz[i][j]=random.randint(1,200)

def Mostrar():
    print("La matriz es la siguiente:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
elementos()

Mostrar()

continuos = []
for lista in matriz:
    for element in range(len(lista)-1):
        if lista[element] == lista[element+1]-1:
            continuos.append((lista[element],lista[element+1]))
print("los numeros continuos son: ")
print(continuos)

