import numpy as np
sec_num = np.random.randint(1,100)
# print(sec_num)

while True:
    try:
        guess = int(input("Enter your guess: "))
        if guess < 1 or guess > 100:
            print("please enter a number between 1 and 100")
        elif guess < sec_num:
            print("you guessed too low")
        elif guess > sec_num:
            print("you guessed too high")
        else:
            print(f"you guessed correctly{sec_num}")
            break
    except ValueError:
        print("invaild input")