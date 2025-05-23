# 5. Contar elementos mayores que 50
def contar_mayores_que_50():
    lista = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
    mayores = [x for x in lista if x > 50]
    print(f"Cantidad de números mayores que 50: {len(mayores)}")

contar_mayores_que_50()