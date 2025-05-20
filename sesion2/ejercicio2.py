# Solicita 10 números al usuario, los guarda en una lista y muestra la suma total
numeros = []

for i in range(10):
    num = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(num)

suma_total = sum(numeros)
print("La suma total es:", suma_total)
