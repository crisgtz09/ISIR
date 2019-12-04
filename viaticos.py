#una empresa quiere calcuar los viaticos de un empleado que viajara por cierto numero de dias, se tiene un presupuesto por dia para hospedajes y para comidas
#ademas de 100 pesos extras para gastos varios, calcular el  monto  del cheque que debe entregar al empleado dado los impportes de hospedaje y de comida por dia
#y la cantidad de dias que viajará

hospedaje=int
while hospedaje!=0:
    hospedaje=float(input("¿Cuánto es el costo del hospedaje por dia? "))
    dias=int(input("¿Cuántos dias durará? "))
    des=float(input("¿Cuánto gastó de desayuno? "))
    com=float(input("¿Cuánto gastó de comida? "))
    cena=float(input("¿Cuánto gastó de cena? "))
    comida=des+com+cena
    comida_total=comida*dias
    hospedaje_total=hospedaje*dias
    varios=100*dias
    gasto_total=comida_total+hospedaje_total+varios
    print("El gasto de comida por un dia fue de ", comida, "pesos")
    print("El gasto de comida en la estadia total es de ", comida_total)
    print("Se imprimira un cheque por la cantidad de ", gasto_total, " pesos")
    print("_______________________________________________________________________")
    print("| BANORTE                                                             |")
    print("|                                                                     |")
    print("|                           $",gasto_total,"                                 |")
    print("|                                           ___________________       |")
    print("|                                                 firma               |")
    print("|_____________________________________________________________________|")
print("Gasta mucho este wey, corranlo")