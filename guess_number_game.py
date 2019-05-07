###########################
#### GUESS NUMBER GAME ####
###########################

## DESCRIPTION ##
# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

print("Welcome to guess number game! let's see if you can guess my 3 digit number!")
print("Code has been generated, please guess a 3 digit number")

import random
digits = list(range(10))
random.shuffle(digits)
answer = digits[:3]

def check_status(num,answer):
    x = num % 10
    num /= 10
    y = num % 10
    num /= 10
    z = num

    if x == answer[2] or y == answer[1] or z == answer[0]:
        print("Match")
    elif x in answer or y in answer or z in answer:
        print("Close")
    else:
        print("Nope")

def perfect_match(num,answer):
    if num % 10 == answer[2]:
        num /= 10
        if num % 10 == answer[1]:
            num /= 10
            if num % 10 == answer[0]:
                return True
    return False

guess = input("What is your guess? ")

if perfect_match(guess,answer):
    print("Perfect Match")
else:
    check_status(guess,answer)
