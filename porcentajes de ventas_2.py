print ("*"*100)

nombre = input("Bienvenido, por favor ingrese su nombre: ")

print ("*"*100)

ventas = float(input(f"Hola {nombre}, ingresa por favor tu cantidad de ventas: "))

porcentaje = round(ventas * 13/100)

print ("*"*100)

print (f" OK,{nombre}. Este mes ganaste ${porcentaje}")
