import os
#declaracion de variables
nombre,nota1,nota2,nota3="",0.0,0.0,0.0

#imput
nombre=str(os.sys.argv[1])
nota1=int(os.sys.argv[2])
nota2=int(os.sys.argv[3])
nota3=int(os.sys.argv[4])

#processing
promedio=str((nota1+nota2+nota3)/3)

#outpout
print("################################")
print("el promedio de notas")
print("################################")
print("#nombre               :",nombre)
print("#nota1                :",nota1)
print("#nota2                :",nota2)
print("#nota3                :",nota3)
print("#promedio             :",promedio)
print("################################")

#condicionales simples
if(promedio>14):
    print("es un alumno promedio")
