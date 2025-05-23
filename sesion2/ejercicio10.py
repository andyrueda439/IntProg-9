#Sumar elementos en posiciones pares

def elementos_posiciones_pares():
    lista = [int(input(f"Ingrese los numeros {i+1}: ")) for i in range(10)]
    suma = sum(lista[i] for i in range(0, len(lista), 2))
    print("Suma de elementos en posiciones pares: ", suma)

elementos_posiciones_pares()