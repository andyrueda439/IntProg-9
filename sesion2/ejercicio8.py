#Eliminar duplicados
def eliminar_duplicados():
    lista = [int(input(f"Ingrese los numeros {i+1}: ")) for i in range (10)]
    listas_sin_duplicados = list(set(lista))
    print("Lista sin duplicados: ", listas_sin_duplicados)
eliminar_duplicados()