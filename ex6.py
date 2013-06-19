# Strings and Text

# Assigning a string to a variable.  String format d represents that number ten.
x = "There are %d types of people." %10
# Assigning a string to a variable
binary = "binary"
do_not = "don't"
# This string references the two variables as string formats 
y = "Those who know %s and those who %s" % (binary, do_not)

# Python prints variable x and y
print x
print y

# Python prints the string with variable x through a formatted variable
print "I said: %r." %x
print "I also said: '%s'." %y

# Assigning boolean false to hilarious!
hilarious = False
# Assigned string to joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

#Print to python
print joke_evaluation % hilarious


w = "This is the left side of..."
e = "a string with a right side."
f = 10

# Print concatenated strings
print w + e