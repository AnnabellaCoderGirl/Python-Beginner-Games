import random
import datetime

number_correct = 0
number_incorrect = 0
print('Welcome!')
sixtySeconds = datetime.timedelta(seconds=60)
startTime = datetime.datetime.now()
Multiplicand = random.randint(0,12)
Multiplier = random.randint(0,12)
while True:
  prompt = f'What is {Multiplicand} x {Multiplier}? '
  players_guess = input(prompt)
  if int(players_guess) == Multiplicand * Multiplier:
    print('Correct!')
    number_correct += 1
    Multiplicand = random.randint(0,12)
    Multiplier = random.randint(0,12)
  else:
    print('Try again!')
    number_incorrect += 1
  if (datetime.datetime.now() - startTime) >= sixtySeconds:  
    print('Times up!')
    print(f'You got {number_correct} correct and {number_incorrect} wrong.')
    break