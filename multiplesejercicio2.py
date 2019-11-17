import os
#declaracion de variables
curso,ejercicios_resueltos="",0.0

#imput
curso=str(os.sys.argv[1])
ejercicios_resueltos=int(os.sys.argv[2])

#outpout
print("################################")
print("total de ejercicios resueltos")
print("################################")
print("#curso                   :",curso)
print("#ejercicios resueltos    :",ejercicios_resueltos)
print("################################")

#condicionales simples
if(ejercicios_resueltos<100):
    print("puntaje normal")
if(ejercicios_resueltos>100 and ejercicios_resueltos<300):
    print("ganas 2 puntos mas")
if(ejercicios_resueltos>300):
    print("ganas 5 puntos mas")
