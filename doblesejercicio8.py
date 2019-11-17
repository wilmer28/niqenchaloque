import os
#declaracion de variables
altura,radio,volumen_del_cilindro=0.0,0.0,0.0

#imput
altura=int(os.sys.argv[1])
radio=int(os.sys.argv[2])

#processing
volumen_del_cilindro=str(((radio**2)*altura)/2)

#outpout
print("################################")
print("volumen del cilindro")
print("################################")
print("#altura                   :",altura)
print("#radio                     :",radio)
print("#volumen del cilindro",volumen_del_cilindro)
print("################################")

#condicionales simples
if(altura==radio):
    print("cilindro equilatero")
else:
    print("cilindro cualquiera")
