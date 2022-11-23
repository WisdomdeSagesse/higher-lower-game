import random as rd
from game_data import data
from art import logo, vs
from replit import clear


def rand_choice_description(choice):
    details = []
    details.append(choice['name'])
    if choice['description'][0] in ['a','e','i','o','u']:
        details.append('an')
    else:
        details.append('a')
    details.append(choice['description'])
    details.append('from')
    details.append(choice['country'])
    description = ' '.join(details)
    return description

def rand_choice_value(choice):
    num_followers = choice['follower_count']
    return num_followers

def compare_answer(user_pick,pick_a, pick_b):
    if user_pick == 'a':
        return pick_a > pick_b
    elif user_pick == 'b':
        return pick_b > pick_a
def play_game():  
  print(logo)
  choice_a = rd.choice(data)    
  choice_b = rd.choice(data)
  score = 0
  end_game = False
  while not end_game:
      print(f"Compare A: {rand_choice_description(choice_a)}")
      print(vs)
      print(f"Against B: {rand_choice_description(choice_b)}")
      user_pick = input("Who has more followers? Type 'A' or 'B': ").lower()
      while user_pick != 'a' and user_pick != 'b':
          user_pick = input("You have entered a wrong key. Type 'A' or 'B': ").lower()
      if compare_answer(user_pick, rand_choice_value(choice_a), rand_choice_value(choice_b)) == True:
          score += 1
          print(f"You are correct. Current score: {score}")
          choice_a = choice_b
          choice_b = rd.choice(data)
          clear()
      else:
          print(f"You are wrong. Final score : {score}")
          end_game = True
  response = input("Play again? Enter 'y' for Yes and 'n' for No: ").lower()
  while response != 'y' and response != 'n':
    response = input("You have entered the wrong option. Enter 'y' for Yes and 'n' for No: ").lower()
  if response == 'y':
    clear()
    play_game()
  else:
    return
play_game()   