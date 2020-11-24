# Collatz Theory by artehist (https://github.com/Artehist)
# Script works at Python 3 and written in English.

def collatz(number):
	while number != 1:
		if number % 2 == 0:
			number = number // 2
			print(number)

		else:
			number = number * 3 + 1
			print(number)			

a = int(input("Enter a natural number: "))
print(collatz(a))

input("Now you can close the program.")
