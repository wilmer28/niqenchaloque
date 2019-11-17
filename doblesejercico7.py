import os
#declaracion de variables
cliente,precio_de_la_recarga="",0.0

#imput
cliente=str(os.sys.argv[1])
precio_de_la_recarga=int(os.sys.argv[2])

#outpout
print("################################")
print("promociones de la recarga")
print("################################")
print("#cliente                   :",cliente)
print("#precio de la recarga   :",precio_de_la_recarga)
print("################################")

#condicionales simples
if(precio_de_la_recarga>15):
    print("tiene las promociones de la recarga")
else:
    print("tiene solo su recarga")
