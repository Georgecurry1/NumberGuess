#make a function that generates a random number between 1 and 50
#get user input after function is ran
#if the numbers match, output "Its a match!"
#else output "the numbers were not a match!"

import random

def randomNum():
   num = random.randint(1,50)
   return num
    

print("Lets generate a number between 1 and 50")
randomInt = randomNum()

yourNum = input("Enter the number you think the system has created between 1 and 50")

if int(yourNum) == randomInt:
   print("The numbers match!")
else:
   print("These numbers do not match!")