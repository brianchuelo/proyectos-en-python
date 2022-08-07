import random
import collections
from operator import itemgetter

def crear_diccionario_lista():
    diccionario={"ID_1":("Edad",random.randint(1,101)),
                 "ID_2":("Edad",random.randint(1,101)),
                 "ID_3":("Edad",random.randint(1,101)),
                 "ID_4":("Edad", random.randint(1, 101)),
                 "ID_5":("Edad", random.randint(1, 101)),
                 "ID_6":("Edad", random.randint(1, 101)),
                 "ID_7":("Edad", random.randint(1, 101)),
                 "ID_8":("Edad", random.randint(1, 101)),
                 "ID_9":("Edad", random.randint(1, 101)),
                 "ID_10":("Edad",random.randint(1, 101))}
    return diccionario
diccionario=crear_diccionario_lista()
def oredanr_diccionario(diccionario):
    for elem in sorted(diccionario.items(), key=itemgetter(1)) :
     print(elem[0] , " :" , elem[1])
print(f"la persona mas joven es el { min(diccionario.items(), key=itemgetter(1))[0]} y el mas viejo es {max(diccionario.items(), key=itemgetter(1))[0]}")

oredanr_diccionario(diccionario)