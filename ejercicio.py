import random
matriz=[]
mayor=0
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
        for j in range(len(matriz)):
            for i in range(len(matriz)):
                if Col == j+1:
                    print(matriz[i][j])
    if accion==5:
        Fil=int(input("¿Qué fila quieres? "))
        for i in range(len(matriz)):
            if Fil==i+1:
                print(matriz[i])
    if accion==6:
        FoC=input("¿Fila o columna? ")
        if FoC=='columna':
            Col=int(input("¿Qué columna será? "))
            for i in range(columna):
                Max=matriz[i][Col]
                if Max>mayor:
                    mayor=Max
            print("el numero mayor en la columna es ", mayor)
        if FoC=='fila':
            fila=int(input("¿Qué fila será?: "))
            print("el numero mayor en la fila es ",max(matriz[fila]))
    if accion==7:
        for i in range(fila):
            filas=0
            for j in range(fila):
                filas+=matriz[i][j]
            print("El promedio de la fila ", i+1, " es ", filas/fila)
    if accion==8:
        for j in range(columna):
            columnas=0
            for i in range(columna):
                columnas+=matriz[i][j]
            print("El promedio de la columna ", j+1, " es ", columnas/columna)
    if accion==9:
        exit



