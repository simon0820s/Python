from functions import *

def main():
    #Función lineal
    Lineal(x)
    #Función polinomica
    Polynomial(x)
    #Función trignometrica
    Trigonometric(x)

def Lineal(x):
    y=fl.F(x)
    Graph(x,y)
def Polynomial(x):
    y=fp.F(x)
    Graph(x,y)
def Trigonometric(x):
    y=ft.F(x)
    Graph(x,y)

if __name__=='__main__':
    main()
