def printmax(x, y):
	"Prints the max. of two numbers"
	
	x = int(x)
	y = int(y)

	if x>y:
	
		print x, "is maximum."
	else:
		print y, "is maximum."

printmax(3, 4)
print printmax.__doc__
