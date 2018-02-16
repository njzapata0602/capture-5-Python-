#Nick Zapata - ch 5 - ex 1 - 2/15/18

fruit = input('Enter a string: ')
index = len(fruit)
while index > 0:
	letter = fruit[index-1]
	print (letter)
	index = index - 1