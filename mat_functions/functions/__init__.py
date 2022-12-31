import numpy as np
import matplotlib.pyplot as plt
import functions.lineal_function as fl
import functions.polynomial_function as fp
import functions.trigonometric_function as ft
N=100
x=np.linspace(-10,10,num=N)

def Graph(x,y):
    plt.plot(x,y)
    plt.grid()
    plt.show()