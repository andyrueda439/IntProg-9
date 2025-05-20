# Solicita 8 calificaciones, las guarda y calcula el promedio
calificaciones = []

for i in range(8):
    nota = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(nota)

promedio = sum(calificaciones) / len(calificaciones)
print("El promedio es:", promedio)