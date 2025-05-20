#Cargar una lista maualmente
numeros = []

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

print("Lista ingresada:", numeros)