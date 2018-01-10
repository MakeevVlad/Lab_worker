#Changeble file

from numpy import sin, cos
def f_1(*args):
	lol = float(args[1])
	return 9.81*(2*(29 - lol)/290 + 0.24/2)
