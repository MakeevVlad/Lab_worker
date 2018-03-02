
def Enter_function(num, args, equation): #Function saving

	file = open('Functions.py', 'a')
	head = '\ndef f_%s(*args):\n\t' % str(num)
	file.write(head)
	#args = 'x'
	#equation = 'x*x*x'

	file.write( '%s = float(args[1])\n\t' % args )

	file.write( 'return %s\n' % equation)
	file.close()

	#Saving function's name to the Functions_list

	file = open('Functions_list.py', 'a')
	file.write('\tif num == %s:\n\t\tglobal F\n\t\tF = reload(F)' % str(num))
	file.write('\n\t\treturn F.f_%s(*args)\n' % str(num))
	file.close()

def Enter_err_function(num, args, equation):
	file = open('Err_Functions.py', 'a')
	head = '\ndef err_%s(*args):\n\t' % str(num)
	file.write(head)
	#args = 'x'
	#equation = 'x*x*x'

	file.write( '%s = float(args[1])\n\t' % args )

	file.write( 'return %s\n' % equation)
	file.close()

	#Saving function's name to the Functions_list

	file = open('Err_Functions_list.py', 'a')
	file.write('\tif num == %s:\n\t\tglobal F\n\t\tF = reload(F)' % str(num))
	file.write('\n\t\treturn F.err_%s(*args)\n' % str(num))
	file.close()

def Enter_adapt_function(num, equation):
		file = open('Adapt_Functions.py', 'a')
		head = '\ndef adpt_%s(*args):\n\t' % str(num)
		file.write(head)
		#args = 'x'
		#equation = 'x*x*x'

		file.write( 'x = float(args[1])\n\t' )

		file.write( 'return %s\n' % equation)
		file.close()

		#Saving function's name to the Functions_list

		file = open('Adapt_Functions_list.py', 'a')
		file.write('\tif num == %s:\n\t\tglobal F\n\t\tF = reload(F)' % str(num))
		file.write('\n\t\treturn F.adpt_%s(*args)\n' % str(num))
		file.close()


def Get_data(file_path):
	f = open(file_path)
	data = []
	for line in f:
		data.append(line)
	f.close()
	return data
