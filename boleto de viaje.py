#una compañia de autobuses requiere determinar el costo del boleto 
#de un viaje sencillo, basado en los kilometros por recorrer
#calcular el importe del boleto dado el costo por km
#y los km a recorrer del pasajero
kmviaje=1
preciokm=float(input("¿Cúal es el costo por kilometro?: "))
while preciokm <= 0:
    print( "Ingrese un valor valido porfavor ")
    preciokm=float(input("¿Cúal es el costo por kilometro?: "))
while (kmviaje!=0):
    kmviaje=int(input("Ingrese los kilometros a recorrer: "))
    precio=kmviaje*preciokm
    print("El costo total es:", precio, "pesos")
print("------------GRACIAS POR VIAJAR CON NOSOTROS---------------------")