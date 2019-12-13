#Un spa reserva citas los 7 días de la semana, pero cada día tiene un número de personas a las que le se puede atender y un precio
#primero capturar el precio de cada día y el número de personas que se pueden atender (NPPA), luego iniciar la captura de las reservaciones pidiendo día de la semana, 
#e imprimir el importe que debe pagar por ese día, la captura de reservaciones terminará cuando en día digite un cero, e imprimirá cuantas personas se atendieron por día
#, así como el importe obtenido. (La matriz quedaría de la siguiente manera, pero si considera necesario puede agregar mas columnas).

lista=['---DIA---','PRECIO','NPPA','RESERVACIONES','P TOTAL','VACANTES']
matriz=[]
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

print (lista)
for i in range(len(matriz)):
    print (matriz[i])