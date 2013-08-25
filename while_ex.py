num = 23;
running = True;

while running:
	guess = int(raw_input('Enter an integer : '))

	if guess == num:
		print "Congrats!!"	
		running = False
	elif guess < num:
		print "No, It is a higher guess.."
	else:
		print "No, it is a lower guess.. "

else:
	print "The while loop is over.. :)"

print "Done \m/ "
