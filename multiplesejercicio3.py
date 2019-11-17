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
if(dias_de_vacaciones<30):
    print("se le abona un pago extra")
if(dias_de_vacaciones>30 and dias_de_vacaciones<35):
    print("se le descuenta 10 soles por dia")
if(dias_de_vacaciones>35):
    print("esta despedido")
