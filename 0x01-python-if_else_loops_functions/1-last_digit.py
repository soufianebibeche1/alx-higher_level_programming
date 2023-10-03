#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10  # get the last digit

if lastdigit < 0:
    lastdigit = -lastdigit

msg = f"Last digit of {number} is {lastdigit} and is"

if lastdigit > 5:
    msg = msg + " greater than 5"
elif lastdigit == 0:
    msg = msg + " 0"
else:
    msg = msg + " less than 6 and not 0"

print(msg)
