#System packages
from importlib import reload
import numpy as np
from tkinter import *

#User's packages
import Rooling as Rl
#import Functions as F
import Functions_list as F_l
import Plotter

b = 3
num = 1
num_err = 1
#Rl.Enter_function(num)
#F = reload(F)
#Plotter.Plot_simple_function(num)
def Non():
    print('None')

def Plot_button():
    Reload_button()
    arg_ = []
    args_val = str(arguments_.get()) #Function arguments
    func_val = str(function_.get())  #Function

    arg_.append(num)

    arg_.append(str(file_path_x_.get()) ) #Paths of data files 2, 3
    arg_.append(str(file_path_y_.get()))

    arg_.append(str(x_label_.get()))   #X label 4
    arg_.append(str(y_label_.get()))   #Y label 5

    arg_.append(int(var.get())) #If we need aproximation(1 - yes, 0 - no) 6

    arg_.append(str(aprox_style_.get()))# Aproximation style 7
    arg_.append(str(aprox_color_.get()))#Aproximation Color 8
    arg_.append(str(main_style_.get()))# Main style 9
    arg_.append(str(main_color_.get())) #Main Color 10

    arg_.append(float(errorbars_x_.get()))#X error 11
    arg_.append(int(err_var.get())) #   12
    arg_.append(num_err) #13

    arg_.append(int(sc_var.get())) #If we need scale settings 14
    arg_.append(float(locator_x_.get())) #X scale 15
    arg_.append(float(locator_y_.get())) #Y scale 16
    arg_.append(str(x_adaptation_.get())) #X adaptation function 17
    arg_.append(str(y_adaptation_.get())) #Y adaptation function 18
    arg_.append(int(adapt_var.get())) # If we need adaptation function 19

    #Saving approx function
    if var.get() == 1:
        Rl.Enter_function('1', args_val, func_val)

    if adapt_var == 1:
        if apr_val == 0:
            Rl.Enter_adapt_function(1, str(y_adaptation_.get()))
            Rl.Enter_adapt_function(2, x_adaptation_.get())

        '''
        Rl.Enter_function(n, 'y', str(y_adaptation_.get()))
        Rl.Enter_function(n, 'x', str(x_adaptation_.get()))
        '''

    if adapt_var.get() == 1:
        Rl.Enter_adapt_function(1, y_adaptation_)
        Rl.Enter_adapt_function(2, x_adaptation_)

    #Saving error function
    if err_var.get() == 1:
        if var.get == 1:
            arg_[0] += 1
        Rl.Enter_err_function(num, str(error_args_.get()), errorbars_y_.get())

    Plotter.Plot_s(*arg_)

    #except ValueError:
        #print("Error!")

def Reload_button():
    global Plotter
    Plotter = reload(Plotter)

    file1 = open('Functions_list.py', 'w+')
    file2 = open('Functions.py', 'w+')
    #Cleaning Functions_list.py
    file1.write('#Changeble file\n\nimport Functions as F\nfrom importlib import reload')
    file1.write('\n\ndef f_num(*args):\n\tnum = args[0]\n\tif num == 0:\n\t\treturn 0\n')
    #Cleaning Functions.py
    file2.write('#Changeble file\n\nfrom math import *')

    file1.close()
    file2.close()

    file1 = open('Err_Functions_list.py', 'w+')
    file2 = open('Err_Functions.py', 'w+')
    #Cleaning Err_Functions_list.py
    file1.write('#Changeble file\n\nimport Err_Functions as F\nfrom importlib import reload')
    file1.write('\n\ndef err_num(*args):\n\tnum = args[0]\n\tif num == 0:\n\t\treturn 0\n')
    #Cleaning Err_Functions.py
    file2.write('#Changeble file\n\nfrom math import *')

    file1.close()
    file2.close()

    file1 = open('Adapt_Functions_list.py', 'w+')
    file2 = open('Adapt_Functions.py', 'w+')
    #Cleaning Err_Functions_list.py
    file1.write('#Changeble file\n\nimport Adapt_Functions as F\nfrom importlib import reload')
    file1.write('\n\ndef f_num(*args):\n\tnum = args[0]\n\tif num == 0:\n\t\treturn 0\n')
    #Cleaning Err_Functions.py
    file2.write('#Changeble file\n\nfrom math import *')

    file1.close()
    file2.close()

def Dev_tool():
    function_.insert(END, '9.81*(2*(29 - x)/290 + 0.24/2)')
    arguments_.insert(END, 'x')
    file_path_y_.insert(END, 'Y.txt')
    file_path_x_.insert(END, 'X.txt')

def Extras_button_addon_err():
    if err_var.get() == 0 and xrs_var.get() == 1:
        errorbars_y_.grid_remove()
        errorbars_x_.grid_remove()
        error_args_.grid_remove()
        error_args_label_.grid_remove()
        errorbars_x_label_.grid_remove()
        errorbars_y_label_.grid_remove()
    if err_var.get() == 1 and xrs_var.get() == 0:
        errorbars_y_.grid_remove()
        errorbars_x_.grid_remove()
        error_args_label_.grid_remove()
        error_args_.grid_remove()
        errorbars_x_label_.grid_remove()
        errorbars_y_label_.grid_remove()
    if err_var.get() == 1 and xrs_var.get() == 1:
        errorbars_y_.grid()
        errorbars_x_.grid()
        error_args_label_.grid()
        error_args_.grid()
        errorbars_x_label_.grid()
        errorbars_y_label_.grid()

def Extras_button_addon():
    if xrs_var.get() == 1 and var.get() == 0:
        aprox_style_label_.grid_remove()
        aprox_style_.grid_remove()
        aprox_color_button.grid_remove()
        aprox_color_.grid_remove()
    if xrs_var.get() == 0 and var.get() == 1:
        aprox_style_label_.grid_remove()
        aprox_style_.grid_remove()
        aprox_color_button.grid_remove()
        aprox_color_.grid_remove()
    if xrs_var.get() == 1 and var.get() == 1:
        aprox_style_label_.grid()
        aprox_style_.grid()
        aprox_color_button.grid()
        aprox_color_.grid()

def Extras_button_addon_scale():
    if sc_var.get() == 0 and xrs_var.get() == 1:
        locator_x_.grid_remove()
        locator_x_label_.grid_remove()
        locator_y_.grid_remove()
        locator_y_label_.grid_remove()

    if sc_var.get() == 1 and xrs_var.get() == 0:
        scale_var_.grid_remove()
        locator_x_.grid_remove()
        locator_x_label_.grid_remove()
        locator_y_.grid_remove()
        locator_y_label_.grid_remove()

    if sc_var.get() == 1 and xrs_var.get() == 1:
        scale_var_.grid()
        locator_x_.grid()
        locator_x_label_.grid()
        locator_y_.grid()
        locator_y_label_.grid()

def Extras_button_addon_adapt():
    if adapt_var.get() == 0 and xrs_var.get() == 1:
        y_adaptation_label_.grid_remove()
        y_adaptation_.grid_remove()
        x_adaptation_label_.grid_remove()
        x_adaptation_.grid_remove()

    if adapt_var.get() == 1 and xrs_var.get() == 1:
        y_adaptation_label_.grid()
        y_adaptation_.grid()
        x_adaptation_.grid()
        x_adaptation_label_.grid()

    if adapt_var.get() == 1 and xrs_var.get() == 0:
        y_adaptation_label_.grid_remove()
        y_adaptation_.grid_remove()
        x_adaptation_label_.grid_remove()
        x_adaptation_.grid_remove()



#SentDex
def Extras_button():
    if xrs_var.get() == 0:
        aprox_style_label_.grid_remove()
        aprox_style_.grid_remove()
        aprox_color_button.grid_remove()
        aprox_color_.grid_remove()
        #########################
        main_style_label_.grid_remove()
        main_style_.grid_remove()
        main_color_button.grid_remove()
        main_color_.grid_remove()
        #########################
        errorbars_x_.grid_remove()
        error_args_label_.grid_remove()
        errorbars_y_.grid_remove()
        error_args_.grid_remove()
        errorbars_x_label_.grid_remove()
        errorbars_y_label_.grid_remove()
        #########################
        scale_var_.grid_remove()
        locator_x_.grid_remove()
        locator_x_label_.grid_remove()
        locator_y_.grid_remove()
        locator_y_label_.grid_remove()
        #########################
        data_adaptation_var_.grid_remove()
        y_adaptation_label_.grid_remove()
        y_adaptation_.grid_remove()
        x_adaptation_label_.grid_remove()
        x_adaptation_.grid_remove()

    if err_var.get() == 0:
        errorbars_button_.grid_remove()
        errorbars_x_.grid_remove()
        error_args_label_.grid_remove()
        errorbars_y_.grid_remove()
        error_args_.grid_remove()
        errorbars_x_label_.grid_remove()
        errorbars_y_label_.grid_remove()

    if xrs_var.get() == 1 and var.get() == 1:
        aprox_style_label_.grid()
        aprox_style_.grid()
        aprox_color_button.grid()
        aprox_color_.grid()
        #########################
    if xrs_var.get() == 1:
        errorbars_button_.grid()
        scale_var_.grid()
        data_adaptation_var_.grid()

        main_style_label_.grid()
        main_style_.grid()
        main_color_button.grid()
        main_color_.grid()

    if err_var.get() == 1 and xrs_var.get() == 1:
        errorbars_y_.grid()
        errorbars_x_.grid()
        error_args_label_.grid()
        error_args_.grid()
        errorbars_x_label_.grid()
        errorbars_y_label_.grid()

    if sc_var.get() == 0:
        locator_x_.grid_remove()
        locator_x_label_.grid_remove()
        locator_y_.grid_remove()
        locator_y_label_.grid_remove()

    if sc_var.get() == 1 and xrs_var.get() == 1:
        scale_var_.grid()
        locator_x_.grid()
        locator_x_label_.grid()
        locator_y_.grid()
        locator_y_label_.grid()

    if adapt_var.get() == 0:
        y_adaptation_label_.grid_remove()
        y_adaptation_.grid_remove()
        x_adaptation_label_.grid_remove()
        x_adaptation_.grid_remove()
    if adapt_var.get() == 1 and xrs_var.get() == 1:
        y_adaptation_label_.grid()
        y_adaptation_.grid()
        x_adaptation_label_.grid()
        x_adaptation_.grid()


root = Tk()
root.title('Lab_worker_demo')
root.resizable(width=False, height=False) #Scale holder

frame = Frame(root)
frame.grid()
Reload_button()

#Aprox Function input
function_label = Label(frame, text = 'Approximation', bg = 'darkgrey').grid(row = 1, column = 2, columnspan = 3)
function_ = Entry(frame, width = 20)
function_.grid(row = 2, column = 1, columnspan = 4, padx = (10, 0))
var = IntVar() #If we need aproxi mation
ap_var_button = Checkbutton(frame, variable = var, command = Extras_button_addon ).grid(row = 1, column = 1, columnspan = 1)


#Arguments' names input
arguments_label = Label(frame, text = 'Arguments').grid(row = 1, column = 5, columnspan = 4)
arguments_ = Entry(frame, width = 20)
arguments_.grid(row = 2, column = 5, columnspan = 4, padx = (10, 0))

#Plot button
plot_button = Button(frame, text = 'Plot', command = Plot_button, width = 20)
plot_button.grid(row = 4, column = 19, columnspan = 4, padx = (10, 0))

#Button to recreate function's determination
reload_button= Button(frame, text = 'Reload', command = Reload_button, width = 20)
reload_button.grid(row = 2, column = 19, columnspan = 4, padx = (10, 0))

#files paths input
file_path_ylabel_ = Label(frame, text = 'Full name of the data file(Y axis)').grid(row = 1, column = 9, columnspan = 10)
file_path_y_ = Entry(frame, width = 40)
file_path_y_.grid(row = 2, column = 9, columnspan = 9, padx = (10, 0))

file_path_xlabel = Label(frame, text = 'Full name of the data file(X axis)').grid(row = 3, column = 9, columnspan = 10)
file_path_x_ = Entry(frame, width = 40)
file_path_x_.grid(row = 4, column = 9, columnspan = 9, padx = (10, 0))

#Axis labels
x_label_label_ = Label(frame, text = 'X axis label').grid(row = 3, column = 1, columnspan = 4)
x_label_= Entry(frame, width = 20)
x_label_.grid(row = 4, column = 1, columnspan = 4, padx = (10, 0))

y_label_label_ = Label(frame, text = 'Y axis label').grid(row = 3, column = 5, columnspan = 4)
y_label_= Entry(frame, width = 20)
y_label_.grid(row = 4, column = 5, columnspan = 4, padx = (10, 0))



#Line styless
aprox_style_label_ = Label(frame, text = 'Approximation style\n(-, -., --, :)')
aprox_style_label_.grid(row = 7, column = 1, columnspan = 4)

aprox_style_ = Entry(frame, width = 10)
aprox_style_.insert(END, '-' )#Standart setting
aprox_style_.grid(row = 7, column = 5, columnspan = 1)
########
main_style_label_ = Label(frame, text = 'Main style\n(-, -., --, :)')
main_style_label_.grid(row = 6, column = 1, columnspan = 4)

main_style_ = Entry(frame, width = 10)
main_style_.insert(END, '-' )#Standart setting
main_style_.grid(row = 6, column = 5, columnspan = 1)


#Line Colors
aprox_color_ = Entry(frame, width = 20)
aprox_color_.grid(row = 7, column = 11, columnspan = 5)
aprox_color_.insert(END, 'red')

aprox_color_button = Button(frame, width = 20, command = lambda : aprox_color_button.config(bg = aprox_color_.get()) , text = 'Aprox color\n(press to check)', bg = 'red')
aprox_color_button.grid(row = 7, column = 7, columnspan = 4, padx =(10, 10), pady = (10,0 ), ipadx = 2)
#######
main_color_ = Entry(frame, width = 20)
main_color_.grid(row = 6, column = 11, columnspan = 5)
main_color_.insert(END, 'blue')

main_color_button = Button(frame, width = 20, command = lambda : main_color_button.config(bg = main_color_.get()) , text = 'Main color\n(press to check)', bg = 'blue')
main_color_button.grid(row = 6, column = 7, columnspan = 4, padx =(10, 10), ipadx = 2)

#ErrorBars
err_var = IntVar()
errorbars_button_ = Checkbutton(frame, variable = err_var, command = Extras_button_addon_err, text = 'ErrorBars')
errorbars_button_.grid(row = 8, column = 1, columnspan = 3, padx = (4,0),  pady = (10, 0))

errorbars_x_label_ = Label(frame, text = 'X error')
errorbars_x_label_.grid(row = 8, column = 5, columnspan = 1, pady = (10, 0))
errorbars_x_ = Entry(frame, width = 10)
errorbars_x_.grid(row = 9, column = 5, columnspan = 1, pady = (0, 10))
errorbars_x_.insert(END, 0.0)

errorbars_y_label_ = Label(frame, text = 'Y error (may be a function)')
errorbars_y_label_.grid(row = 8, column = 7, columnspan = 4, pady = (10, 0))
errorbars_y_ = Entry(frame, width = 22)
errorbars_y_.grid(row = 9, column = 7, columnspan = 4, pady = (0, 10))
errorbars_y_.insert(END, 0.0)

error_args_label_ = Label(frame, text = 'Error function arguments')
error_args_label_.grid(row = 8, column = 11, columnspan = 4, pady = (10, 0))
error_args_ = Entry(frame, width = 20)
error_args_.grid(row = 9, column = 11, columnspan = 5, pady = (0, 10))
error_args_.insert(END, 'x')
#error_bars_style_ = Label(frame,)

#Scale settings
sc_var = IntVar()
scale_var_ = Checkbutton(frame, text = 'Scale settings', variable = sc_var, command = Extras_button_addon_scale)
scale_var_.grid(row = 10, column = 1, columnspan = 3, padx = (31,0),  pady = (10, 0))

locator_x_label_ = Label(frame, text = 'X scale')
locator_x_label_.grid(row = 10, column = 5, columnspan = 2, pady = (10, 0), padx = (0, 7))
locator_x_ = Entry(frame, width = 10)
locator_x_.grid(row = 11, column = 5, columnspan = 1, pady = (0, 10))
locator_x_.insert(END, 1.0)


locator_y_label_ = Label(frame, text = 'Y scale')
locator_y_label_.grid(row = 10, column = 6, columnspan = 3, pady = (10, 0), padx = (4, 0))
locator_y_ = Entry(frame, width = 10)
locator_y_.grid(row = 11, column = 8, columnspan = 1, pady = (0, 10), padx = (15, 0))
locator_y_.insert(END, 1.0)


#Data adaptation
adapt_var = IntVar()
data_adaptation_var_ = Checkbutton(frame, text = 'Data adaptation', variable = adapt_var, command = Extras_button_addon_adapt)
data_adaptation_var_.grid(row = 12, column = 1, columnspan = 4, padx = (9,0),  pady = (10, 0))

y_adaptation_label_ = Label(frame, text = 'Y adapt function')
y_adaptation_label_.grid(row = 12, column = 5, columnspan = 4, pady = (10, 0), padx = (0, 10))
y_adaptation_ = Entry(frame, width = 20)
y_adaptation_.grid(row = 13, column = 5, columnspan = 4, pady = (10, 0), padx = (0, 10))

x_adaptation_label_ = Label(frame, text = 'X adapt function')
x_adaptation_label_.grid(row = 12, column = 9, columnspan = 6, pady = (10, 0), padx = (10, 7))
x_adaptation_ = Entry(frame, width = 20)
x_adaptation_.grid(row = 13, column = 9, columnspan = 6, pady = (10, 0), padx = (10, 7))


#If we need extra settings
xrs_var = IntVar()
Extras_button()
extras_button_ = Checkbutton(frame, text = 'More settings', variable = xrs_var, command = Extras_button)
extras_button_.grid(row = 5, column = 1, columnspan = 3, padx = (30, 0))

Dev_tool()

root.mainloop()
