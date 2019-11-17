import os
#declaracion de variables
cliente,precio_de_los_productos="",0.0

#imput
cliente=str(os.sys.argv[1])
precio_de_los_productos=int(os.sys.argv[2])

#outpout
print("################################")
print("descuento de los productos")
print("################################")
print("#cliente                   :",cliente)
print("#precio de los productos   :",precio_de_los_productos)
print("################################")

#condicionales simples
if(precio_de_los_productos>400):
    print("tiene un descuento del 20%")
else:
    print("precio normal")
