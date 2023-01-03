from functions import *

def create():
    #Función lineal
    lineal(x)
    #Función polinomica
    polynomial(x)
    #Función trignometrica
    trigonometric(x)
    #Funcion trascendental
    trascendental(x)
    #Funcion logaritmica
    logarithmic()
    #Funcion compuesta
    compound(x)

def lineal(x):
    y=fl(x)
    graph(x,y)
def polynomial(x):
    y=fp(x)
    graph(x,y)
def trigonometric(x):
    y=ftri(x)
    graph(x,y)
def trascendental(x):
    y=ftra(x)
    graph(x,y)
def logarithmic():
    x,y=flog()
    graph(x,y)
def compound(x):
    y=fc(x)
    graph(x,y)

if __name__=='__main__':
    create()
