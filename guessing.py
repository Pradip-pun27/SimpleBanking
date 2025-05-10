# Guessing any Random number betn 1-100

import random as random
low = 1
up = 10
value = random.randint(low, up)
guess = 0
print("Guessing Program in Python.")

res = True
while res:
    try:
        ans = int(input("Enter any number in betn 1 - 10: "))
        if low <= ans <= up:
            guess += 1
            if ans > value:
                print("Your guess is larger.")
            elif ans < value:
                print("Your guess is smaller.")
            else:
                print("CORRECT GUESS. OWHOO!")
                print(f"No of Guesses = {guess}")
                res = False
        else:
            print("Entered number is out of range.")
    except ValueError as v:
        print("Invalid input! Please enter a valid number.")
        print(v);

print("Correct Value is: ", value)
