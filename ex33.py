#While loops

def counting (end_count, increments):
	i = 0
	numbers = []

	while i < end_count:
		print "At the top i is %d" % i
		numbers.append(i)

		i += increments
		print "Numbers now: ", numbers
		print "At the bottom i is %d" %i

		print "The numbers:"

		for num in numbers:
			print num

def counting_again (end_count, increments):
	x= range(0, end_count, increments)

	for num in x:
		print num



print range(1,10,2)
print range(10)
counting(10,2)
counting_again(10,2)