#imported the module
import random as r

num=r.randrange(100)
Guess=5

while Guess >=0:
    your_guess = int(input("enter your Guess"))

    def check(x):
        if your_guess ==x:
            print('you win')
        elif your_guess > x:
            print("you are close,keep trying lower")
        else:
            print('you are close,keep trying higher')

    if Guess > 1:
        check(num)
    elif Guess == 1:
        check(num)
        print('this is your last chance, make the most of it')

    else:
        print("yoou lost")
    Guess = Guess - 1