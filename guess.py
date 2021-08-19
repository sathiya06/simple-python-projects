import random


def user_guess():
    x = int(input("Enter the number limit"))
    r_number = random.randint(1, x)
    guess = 0
    while guess != r_number:
        guess = int(input("Enter your guess: "))
        if guess - r_number < 10 and guess - r_number > 0:
            print("you are close but a little high")
        elif r_number - guess < 10 and r_number - guess > 0:
            print("you are close but a little low")
        elif r_number < guess:
            print("you are close but a too high")
        elif r_number > guess:
            print("you are close but a too low")
    print(f"Congrats!!! You Found The Number {r_number}")


def comp_guess():
    x = int(input("Enter the number limit"))
    low = 1
    high = x
    feedback = ""
    while feedback != "c" and low != high:
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high(h),too low(l),correct(c)").lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"Yay!!! I guessed the correct number{guess}")


t = int(input("press 1 to make computer guess 0 to u guess"))
if t == 0:
    user_guess()
if t == 1:
    comp_guess()
