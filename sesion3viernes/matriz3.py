matriz = [["axel", "oscar", "joshua"], ["alfredo", "donald", "andy"], ["kevin", "cristopher", "josue"]]
print("-"*29)
for fila in matriz:
    for columna in fila:
        print(f"|{columna:>6}", end = " ")    
    print("|")
    print("-"*29)