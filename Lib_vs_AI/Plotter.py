#system packages
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
from importlib import reload
from tkinter import *

#User's packages
import Functions_list as F_l
import Err_Functions_list as Err_l
import Functions as F
import Adapt_Functions_list as A_l
import Rooling as Rl

#Just for test. Plots only function
def Plot_simple_function(num):
    fig, ax = plt.subplots()
    x = np.arange(-15, 15, 1)

    y=[]

    for i in x:
        y.append(F_l.f_num(num, i))
        print (F_l.f_num(num, i))
    ax.plot(x, y)
    plt.show()

#Plot with lab data set
def Plot_n(num, file_path):
    fig, ax = plt.subplots()
    x = Rl.Get_data(file_path)
    global F_l
    F_l = reload(F_l)
    y = []
    c = 0
    for i in x:
        x[c] = float(i)
        c+=1
        y.append(F_l.f_num(num, i))
    ax.plot(x, y)
    plt.show()


def Plot_s(num, filex_path, filey_path, x_label, y_label, apr_val,
apr_style, apr_color, main_style, main_color, x_err, var_err, num_err,
var_scale, x_scale, y_scale, x_adapt, y_adapt, adapt_var):


    fig, ax = plt.subplots()

    x = Rl.Get_data(filex_path)
    y = Rl.Get_data(filey_path)
    for i in range(0, len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])



    global F_l
    F_l = reload(F_l)
    global Err_l
    Err_l = reload(Err_l)

    #Aproximation
    if apr_val == 1:
        xa = np.arange(float(x[0]), float(x[len(x)-1]), ( -float(x[0])+float(x[1]) )/100 )
        ya = []
        c = 0
        for i in xa:
            xa[c] = float(i)
            c+=1
            ya.append(F_l.f_num(num, i))
        ax.plot(xa, ya, ls = apr_style, color = apr_color, lw = 1)

    if adapt_var == 1:
        for i in range(0, len(x)):
            x[i] = A_l.f_num(1, y[i])
            y[i] = A_l.f_num(2 ,x[i])


    #Errorbars
    if var_err == 1:
        y_err = []
        for i in range(0, len(y)):
            y_err.append(float(Err_l.err_num( num_err, x[i])))
        ax.errorbar(x, y, xerr = x_err, yerr = y_err, color = 'red', ls = ' ', lw = 1 )

    #Scale
    if var_scale ==1:
        x_loc = matplotlib.ticker.MultipleLocator (base = x_scale)
        y_loc = matplotlib.ticker.MultipleLocator (base = y_scale)
        ax.xaxis.set_major_locator(x_loc)
        ax.yaxis.set_major_locator(y_loc)



    ax.grid(color="blue", which="both", linestyle=':', linewidth=0.5)

    ax.set_ylabel(y_label)
    ax.set_xlabel(x_label)

    ax.plot(x, y, ls = main_style, color = main_color)

    plt.show()
