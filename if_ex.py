
num = 25;
guess = int(raw_input('Enter the guess number : '));

if guess == num:
	print 'Congrats!!'
	print "You Win.. :)"
elif guess < num:
	print "Wrong guess, you entered smaller number"
else:
	print "Guess Number entered is larger.. "

print "Done"

