#Assert exception, para verificaciones
suma=lambda x,y: x+y
assert suma(10,20)==30
print("la suma salio bien")

#Exception creada, se pueden personalizar los errores
age=int(input('ingrese su edad unicamente usando numeros enteros '))
if age<18:
    raise Exception('No se permiten menores de edad')