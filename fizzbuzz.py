#Create a function fizz_buzz to return 'Fizz', 'Buzz', 'FizzBuzz',
#or the argument it receives, all depending on the argument of the function, 
#a number that is divisible by, 3, 5, or both 3 and 5, respectively.
#When the number is not divisible by 3 or 5,the number itself should be returned.
def fizz_buzz(num):
	if (num % 15 == 0):
		return "FizzBuzz"
	elif (num % 5 == 0):
		return "Buzz"
	elif (num % 3 == 0 ):
		return "Fizz"
	else:
		return num 

print(fizz_buzz(45))

