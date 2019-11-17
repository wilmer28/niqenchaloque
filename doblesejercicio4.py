import os
#declaracion de variables
alumno,numero_de_libros_prestados="",0.0

#imput
alunmo=str(os.sys.argv[1])
numero_de_libros_prestados=int(os.sys.argv[2])

#outpout
print("################################")
print("libros prestados")
print("################################")
print("#alumno                   :",alumno)
print("#numero de libros prestados    :",numero_de_libros_prestados)
print("################################")

#condicionales simples
if(numero_de_libros_prestados>20):
    print("ya no se le puede prestar mas libros")
else:
    print("la biblioteca esta a su dispocicion")
