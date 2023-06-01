import random
while True:
 
  choices = ['rock', 'paper', 'scissors']
  computer = random.choice(choices)
  player = None
  beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
  #prevents user from entering wrong input(repeats loop)
  while player not in choices:
    player = input('Enter: ROCK, PAPER or SCISSORS:  ').lower()
    
    
  
  if beats[player] == computer:
   print("Computer won!")
  if beats[computer] == player:
    print("Player won!")
  if player == computer:
    print("Draw!")

  play_again = input('Do you want to try again?: yes  no: ')

  if play_again != 'yes':
    break
   
print('Have a good day!')

