import numpy as np
import matplotlib.pyplot as plt
from functions import *

def main():
    N=100
    x=np.linspace(-10,10,num=N)
    #Función lineal
    Lineal(x)
    #Función polinomica
    Polynomial(x)

def Lineal(x):
    y=fl.f(x)
    graph(x,y)

def Polynomial(x):
    y=fp.f(x)
    graph(x,y)

def graph(x,y):
    plt.plot(x,y)
    plt.grid()
    plt.show()

if __name__=='__main__':
    main()
