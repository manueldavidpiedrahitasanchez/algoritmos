

#ejecicio 1,5

'''Escriba un programa que realice la comprobación
de la división. Recuerde:
Divisor * Cociente + Residuo = Dividendo
Tome como entrada dos números, realice la
división entre ellos y entregue al usuario un texto
descriptivo con la comprobación de la división.'''

dividendo=int(input("ingrese el primer numero"))
divisor=int(input("ingrese el segundo numero"))



#calculos
cociente=dividendo/divisor
residuo=dividendo%divisor

print(f"la comprobacion de la divisiones es : {divisor}por {cociente} mas {residuo}es igual a {dividendo}")