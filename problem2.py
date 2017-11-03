import random
number = random.randint(1,1000)
number = int(number)
guess = 0
while number != guess:
	guess = 0
	guess = input("enter a number between 1 and 1000")
	guess = int(guess)
	if guess > 1000 or guess < 1:
		print("you are out of range")
	elif guess == number:
		print("you won")
	elif guess < number:
		print("go higher")
	elif guess > number:
		print("go lower")

