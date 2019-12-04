#se requiere determinar el costo de una llamada dado el tiempo en horas
#minutos y segundos, asi como un costo por minuto, considere
#que los segundos se cobraran como minuto completo
#realice el programa que calcule el importe de la llamada

segundos=int

while segundos!=0:
    
    segundos=int(input("¿Cuántos segundos duro la llamada?"))
    horas=int(segundos/3600)
    segundos-=horas*3600
    minutos=int(segundos/60)
    segundos-=minutos*60
    costo=float(input("¿Cuál es el costo por minuto?: "))
    print("%s:%s:%s" % (horas,minutos,segundos))
    print("Es el tiempo de llamada")
    if minutos>=1 and segundos>=1:
        costominutos=costo*minutos
        print(costominutos," Es el precio a pagar ")
    if horas>=1:
        costominutos=costo*minutos
        costohora=costo*60
        costofinal=costohora+costominutos
        print(costofinal, "Pesos es el precio a pagar")
