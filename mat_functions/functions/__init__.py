import numpy as np
import matplotlib.pyplot as plt
from functions.lineal_function import f as fl
from functions.polynomial_function import f as fp
from functions.trigonometric_function import f as ftri
from functions.trascendental_functions import f as ftra
from functions.logarithmic_function import f as flog
from functions.compound_functions import f as fc

N=100
x=np.linspace(-10,10,num=N)

def graph(x,y):
    plt.plot(x,y)
    plt.grid()
    plt.show()