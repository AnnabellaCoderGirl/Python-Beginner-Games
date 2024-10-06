import random

guessNumber = 1
print('Welcome!')
print('You have 10 guesses. Good luck!')
computers_number = random.randint(0,1000)
while True:
  prompt = f'Guess number {guessNumber}, what is your guess? '
  players_guess = input(prompt)
  if computers_number == int(players_guess):
    print('Correct!')
    break
  elif computers_number > int(players_guess):
    print('Too Low')
  else:
    print('Too High')
  if guessNumber == 10:
    print('You ran out of guesses!')
    print(f'The answer is {computers_number}.')
    break

  guessNumber += 1