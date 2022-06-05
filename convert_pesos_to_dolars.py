pesos = input("Ingrese la cantida de pesos colombianos a convertir: ")
pesos = float(pesos)
valor_dolar = 3818
dolares = pesos/valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("La cantidad es de  $" + dolares + " dolares" )
