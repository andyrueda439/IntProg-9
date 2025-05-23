#Separar pares e impares
import random

def separar_pares_impares():
    lista = [random.randint(1, 100) for _ in range(10)]
    pares = [x for x in lista if x % 2 == 0]
    impares = [x for x in lista if x % 2 != 0]
    print("Lista original:", lista)
    print("Pares:", pares)
    print("Impares:", impares)

separar_pares_impares()