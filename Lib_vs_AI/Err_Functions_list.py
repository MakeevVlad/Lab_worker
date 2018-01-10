#Changeble file

import Err_Functions as F
from importlib import reload

def err_num(*args):
	num = args[0]
	if num == 0:
		return 0
	if num == 1:
		global F
		F = reload(F)
		return F.err_1(*args)
