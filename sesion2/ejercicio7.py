#Encontrar el maximo y el minimo
def maximo_minimo():
    lista = [int(input(f"Ingrese el numero {i+1}: ")) for i in range (10)]
    print("Maximo: ", max(lista))
    print("Minimo: ", min(lista))

maximo_minimo()