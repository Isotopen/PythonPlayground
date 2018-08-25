#random number math game
#import the random function
import random
#set the number variables to random numbers from 1 to 10
number1 = random.randint(1, 10)
number2 = random.randint(1, 10)
#Ask the question
print('What is ' + str(number1) + ' + ' + str(number2) + '?')
answer = input()
#possible outcomes
if int(answer) == number1 + number2:
    print('Correct!')
else:
    print('Nope! The answer is ' + str(number1 + number2))
    
