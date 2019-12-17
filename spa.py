#Un spa reserva citas los 7 días de la semana, pero cada día tiene un número de personas a las que le se puede atender y un precio
#primero capturar el precio de cada día y el número de personas que se pueden atender (NPPA), luego iniciar la captura de las reservaciones pidiendo día de la semana, 
#e imprimir el importe que debe pagar por ese día, la captura de reservaciones terminará cuando en día digite un cero, e imprimirá cuantas personas se atendieron por día
#, así como el importe obtenido. (La matriz quedaría de la siguiente manera, pero si considera necesario puede agregar mas columnas).

lista=['---DIA---','PRECIO','NPPA','RESERVACIONES','P TOTAL','VACANTES']
matriz=[]
dias1=['1.-lunes','2.-martes','3.-miercoles','4.-jueves','5.-viernes','6.-sabado','7.-domingo','0.-salir']
dias=int
NPPA=int(input("¿Cuántas personas se pueden atender por dia? "))
precio=int(input("¿Cuánto es el precio por persona? "))
for i in range(7):
    dia=input("Ingrese el dia: ")
    reservaciones=int(input("¿Reservacion para cuantas personas? "))
    precio_total=precio*reservaciones
    vacantes=NPPA-reservaciones
    matriz.append([])
    matriz[i].append(dia)
    matriz[i].append(precio)
    matriz[i].append(NPPA)
    matriz[i].append(reservaciones)
    matriz[i].append(precio_total)
    matriz[i].append(vacantes)
while  dias!=0:
    for i in range(len(dias1)):
        print (dias1[i])
    dias=int(input("¿Qué dia desea la nueva reservacion? "))
    reser=int(input("¿Cuántas personas a reservar?"))
    if dias<0 or dias>7:
        print ("ingrese un dia valido")
    if (dias==1):
        q=matriz[0][3]+reser
        matriz[0][3]=q
        w=q*precio
        matriz[0][4]=w
        e=(matriz[0][5]-q)
        matriz[0][5]=e
    if (dias==2):
        q=matriz[1][3]+reser
        matriz[1][3]=q
        w=q*precio
        matriz[1][4]=w
        e=(matriz[1][5]-q)
        matriz[1][5]=e
    if (dias==3):
        q=matriz[2][3]+reser
        matriz[2][3]=q
        w=q*precio
        matriz[2][4]=w
        e=(matriz[2][5]-q)
        matriz[2][5]=e
    if (dias==4):
        q=matriz[3][3]+reser
        matriz[3][3]=q
        w=q*precio
        matriz[3][4]=w
        e=(matriz[3][5]-q)
        matriz[3][5]=e
    if (dias==5):
        q=matriz[4][3]+reser
        matriz[4][3]=q
        w=q*precio
        matriz[4][4]=w
        e=(matriz[4][5]-q)
        matriz[4][5]=e
    if (dias==6):
        q=matriz[5][3]+reser
        matriz[5][3]=q
        w=q*precio
        matriz[5][4]=w
        e=(matriz[0][5]-q)
        matriz[5][5]=e
    if (dias==7):
        q=matriz[6][3]+reser
        matriz[6][3]=q
        w=q*precio
        matriz[6][4]=w
        e=(matriz[6][5]-q)
        matriz[6][5]=e


print (lista)
for i in range(len(matriz)):
    print (matriz[i])