for n in range(101):
	if n == 0:
		continue
	
	if (n % 3 == 0) & (n % 15 == 0) or (n % 5 == 0) & (n % 15 == 0):
		print('FizzBuzz')
	elif n % 3 == 0:
		print('Fizz')
	elif n % 5 == 0:
		print('Buzz')
	else:
		print(n)