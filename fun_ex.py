def func(x):
#	global x
	
	print 'x is', x
	x = 2
	print 'Changed global x to ', x

x = 50
func(x)
print 'Value of x is ', x

