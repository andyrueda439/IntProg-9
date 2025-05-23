# 4. Buscar un elemento
def buscar_palabra():
    lista = ["manzana", "banana", "uva", "pera", "sandía"]
    palabra = input("Ingresa una palabra: ")
    if palabra in lista:
        print("La palabra está en la lista.")
    else:
        print("La palabra NO está en la lista.")