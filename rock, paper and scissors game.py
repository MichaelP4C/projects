import random
while True:
 
  choices = ['rock', 'paper', 'scissors']
  computer = random.choice(choices)
  player = None
  while player not in choices:
    player = input('Enter: ROCK, PAPER or SCISSORS').lower()
    
#just testing github

  

