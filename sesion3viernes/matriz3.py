matriz = [["Axel", "Oscar", "Joshua"], 
          ["Alfredo", "Donald", "Andy"],
            ["Kevin", "Cristopher", "Josue"]]

cant_letras = []

print("-"*29)
for fila in matriz:
    for columna in fila:
        print(f"|{columna}", end = " ")    
    print("|")
    print("-"*29)

for fila in matriz:
    new_row=[]
    for columna in fila:
        new_row.append(len(columna))
    cant_letras.append(new_row)

for fila in cant_letras:
    for columna in fila:
        print(f"|{columna}", end = " ")
    print("|")
    print("-"*17)