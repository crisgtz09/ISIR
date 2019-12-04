#una empresa importadora desea determinar cuantos dolares puede 
#adquirir con cierta cantidad de pesos mexicanos
#datos de entrada son el tipo de cambio y la cantidad en peso mexicanos
#la salida sera la cantidad de dolares
mxn=1
suma_dlls=0
suma_pesos=0
print("-----------------Hola, ¿Que tal?----------------------")
preciodlls=float(input( "Ingrese el valor actual del dolar: "))
while preciodlls <= 0:
    print( "Ingrese un valor valido porfavor ")
    preciodlls=float(input( "Ingrese el valor actual del dolar: "))
while (mxn!=0):
    mxn=float(input("Ingrese la cantidad de pesos a convertir: "))
    dlls= mxn/preciodlls
    print(" Los dolares a obtener son: ", dlls, "dolares")
    suma_dlls=suma_dlls+dlls
    suma_pesos=suma_pesos+mxn
print("los pesos que convertiste fueron ", suma_pesos, " pesos")
print ("La cantidad de dolares obtenidos han sido ",suma_dlls, "dolares")
print("------------HASTA LUEGO-----------------")
