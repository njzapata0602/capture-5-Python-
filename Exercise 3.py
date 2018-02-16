#Nick Zapata - ch 5 - ex 3 - 2/15/18
def count(string, letter):
	x = 0
	for i in string:
		if i == letter:
			x += 1
	print ("This letter" + letter + "appears" + str(x) + "times in the string: " + string)
	
count("This is a test", "t")