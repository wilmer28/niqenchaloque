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
if(numero_de_libros_prestados<5):
    print("aun puede emprestarmas libros")
if(numero_de_libros_prestados>5 and numero_de_libros_prestados<10):
    print("no puede emprestar mas libros")
