#matriz escalar
# Crear una matriz escalar con precios con descuento en la diagonal
def matriz_descuento(n, precio_base, porcentaje_descuento):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            if i == j:
                precio_con_descuento = precio_base * (1 - porcentaje_descuento / 100)
                fila.append(round(precio_con_descuento, 2))
            else:
                fila.append(0)
        matriz.append(fila)
    return matriz

# Imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Entradas del usuario
n = int(input("Ingrese el tamaño de la matriz (n x n): "))
precio_base = float(input("Ingrese el precio base del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (sin %): "))

# Generar y mostrar la matriz
matriz = matriz_descuento(n, precio_base, porcentaje_descuento)
print("Matriz con precios con descuento aplicado en la diagonal:")
imprimir_matriz(matriz)