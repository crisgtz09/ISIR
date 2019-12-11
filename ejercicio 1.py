import random
matriz=[]
columna=int(input("¿Cuántas columnas serán? "))
fila=int(input("¿Cuántas filas serán? "))
menu=['1.Imprimir matriz','2.Totales por Columnas','3.Totales por Filas','4.Imprimir una columna ','5.Imprimir una fila ','6.Número mayor en una fila o columna ','7.Promedios Filas ','8.Promedios Columnas ','9.Salir' ]
for i in range (fila):
    matriz.append([])
    for j in range (columna):
        matriz[i].append(random.randint(1,100))
for i in range(len(menu)):
    print(menu[i])
accion=int
while accion!=9:
    accion=int(input("¿Qué opcion desea realizar? "))
    if accion<0 or accion>9:
        print ("ingrese una opcion valida")
    if accion==1:
        for i in range (len(matriz)):
            print(matriz[i])
    if accion==2:
        for i in range(columna):
            Col=0
            for j in range(fila):
                Col+=matriz[j][i]
            print("la suma de la columna ", i+1, " es ",Col)
    if accion==3:
        for i in range(fila):
            fil=0
            for j in range(columna):
                fil+=matriz[i][j]
            print("la suma de la fila", i+1, " es de ",fil)
    if accion==4:
        Col=int(input("¿Qué columna quieres?"))
        for i in range(len(matriz)):
            if Col == i+1:
                print(matriz[j])
    if accion==5:
        Fil=int(input("¿Qué fila quieres? "))
        for i in range(len(matriz)):
            if Fil == i+1:
                print(matriz[i])