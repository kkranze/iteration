import random
num = input("please enter a number from 1 to 1000")
num = int(num)
if num > 1000:
        print("to high")
if num < 1:
        print("to low")
guess = random.randint(0,1000)
print(guess)
while guess != num:
        hl = input("is it higher or lower")
        if hl == ("higher"):
                guess = random.randint(guess,1000)
                print (guess)
        if hl == ("lower"):
                guess = random.randint(0,guess)
                print (guess)
