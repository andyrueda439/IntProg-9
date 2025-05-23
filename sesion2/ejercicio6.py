# Invertir una lista
def invertir_lista():
    lista = [int(input(f"Ingrese el numero {i+1}: ")) for i in range(10)]
    lista_invertida = lista[::-1]
    print("Lista invertida: ", lista_invertida)

invertir_lista()