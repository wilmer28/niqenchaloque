import os
#declaracion de variables
numeros_de_tickets_de_happyland=0.0

#imput
numeros_de_tickets_de_happyland=int(os.sys.argv[1])

#outpout
print("################################")
print("tickets de happyland")
print("################################")
print("#ticketsde happyland     :",numeros_de_tickets_de_happyland)
print("################################")

#condicionales simples
if(numeros_de_tickets_de_happyland>200):
    print("te ganaste un ticket mas")
else:
    print("sigue intentando")
