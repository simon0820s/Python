#Varios try
try:
    print(0/0)
except ZeroDivisionError as error:
    print('error division por cero')

#Nos pasamos el error por los gvos
try:
    assert 1!=1,'Uno no es igual a uno'
except AssertionError as error:
    print("error")

#Nos pasamos el error por las bolas
try:
    age=int(input('ingrese su edad unicamente usando numeros enteros '))
    if age<18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print("error")

#try unificado
try:
    print(0/0)
    assert 1!=1,'Uno no es igual a uno'
    age=int(input('ingrese su edad unicamente usando numeros enteros '))
    if age<18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print('error division por cero')
except AssertionError as error:
    print(error)
except Exception as error:
    print("error")
print("seguimos con el codigo que sigue fuera del try")