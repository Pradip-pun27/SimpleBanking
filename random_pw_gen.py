# Random secure P.W generator python's program
import random
letters = [chr(i) for i in range(ord('A'), ord('Z')+1)] + [chr(i) for i in range(ord('a'), ord('z')+1)]
numbers =['0','1','2','3','4','5','6','7','8','9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*',
    '(', ')', '-', '_', '=', '+', '[', ']',
    '{', '}', ':', ';', ',', '.', '<', '>',
    '?', '/', '|', '~'
]
print("-----------Wlcm to the Pw generator Program-----------------")
n_letter=int(input("How many letters u wanna put in yrs pw(Enter that number): "))
n_number=int(input( "How many numbers u wanna put in yrs pw(Enter that number): "))
n_symbol=int(input("How many symbols(Special_cahracters) u wanna put in yrs pw(Enter that number): "))
pw=[]
for i in range(1,n_letter+1):
    char =random.choice(letters)
    pw+=char;
for i in range(1,n_symbol+1):
    char=random.choice(symbols)
    pw+=char
for i in range(1,n_number+1):
    char=random.choice(numbers)
    pw+=char
random.shuffle(pw)
password=""
for char in pw:
    password+=char
print(f"Yrs random Password is {password}")
