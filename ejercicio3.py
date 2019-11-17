import os
#declaracion de variables
empleado,dias_de_vacaciones="",0.0

#imput
empleado=str(os.sys.argv[1])
dias_de_vacaciones=int(os.sys.argv[2])

#outpout
print("################################")
print("vacaciones de un empleado")
print("################################")
print("#empleado                   :",empleado)
print("#dias de vacaciones    :",dias_de_vacaciones)
print("################################")

#condicionales simples
if(dias_de_vacaciones>15):
    print("se le descuenta 5soles x dia")
