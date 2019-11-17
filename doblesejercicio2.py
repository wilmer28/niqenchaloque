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
if(ejercicios_resueltos>300):
    print("te ganaste 5 punto extra")
else:
    print("sigue esforsandote")
