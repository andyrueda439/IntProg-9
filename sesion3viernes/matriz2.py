matriz = [[10.5, 2.5], [300.03, 4.71]]
print("-"*17)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6.1f}", end = " ")    
    print("|")
    print("-"*17)