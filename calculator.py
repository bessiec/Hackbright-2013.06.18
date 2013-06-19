from arithmetic import * 

close_calc = False

while not close_calc: 
	user_input = raw_input(">")
	
	new_input = tokenize(user_input)
	#print new_input

	evaluate = new_input[0]
	#print evaluate


	if evaluate == "q":
		close_calc = True
	elif evaluate == "+":
		print add(int(new_input[1]), int(new_input[2]))
	elif evaluate == "-":
		print subtract(int(new_input[1]), int(new_input[2]))
	elif evaluate == "*":
		print multiply(int(new_input[1]), int(new_input[2]))
	elif evaluate == "/":
		function = divide(float(new_input[1]), float(new_input[2]))
		print "%.6f" % function
	elif evaluate == "square":
		print square(int(new_input[1]))
	elif evaluate == "cube":
		print cube(int(new_input[1]))
	elif evaluate == "power":
		print power(int(new_input[1]), int(new_input[2]))
	elif evaluate == "mod":
		print mod(int(new_input[1]), int(new_input[2]))
	else: 
		print "Invalid entry. Try Again!"


