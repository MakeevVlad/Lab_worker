#Changeble file

import Functions as F
from importlib import reload

def f_num(*args):
	num = args[0]
	if num == 0:
		return 0
	if num == 1:
		global F
		F = reload(F)
		return F.f_1(*args)
