import random as rd
from game_data import data
from art import logo, vs
from replit import clear


def rand_choice_description(choice):
    account_name = choice['name']
    if choice['description'][0] in ['a','e','i','o','u']:
        vowel = 'an'
    else:
        vowel = 'a'
    account_desc = choice['description']
    account_country = choice['country']
    description = f"{account_name}, {vowel} {account_desc} from {account_country}"
    return description

def rand_choice_value(choice):
    num_followers = choice['follower_count']
    return num_followers

def compare_answer(pick_a, pick_b):
    user_pick = input("Who has more followers? Type 'A' or 'B': ").lower()
    while user_pick != 'a' and user_pick != 'b':
        user_pick = input("You have entered a wrong key. Type 'A' or 'B': ").lower()
    if user_pick == 'a':
        return pick_a > pick_b
    elif user_pick == 'b':
        return pick_b > pick_a

def play_game():  
  print(logo)
  choice_b = rd.choice(data)
  score = 0
  end_game = False
  while not end_game:
      choice_a = choice_b
      choice_b = rd.choice(data)
      while choice_a == choice_b:
            choice_b = rd.choice(data)
      print(f"Compare A: {rand_choice_description(choice_a)}")
      print(vs)
      print(f"Against B: {rand_choice_description(choice_b)}")
      if compare_answer(rand_choice_value(choice_a), rand_choice_value(choice_b)) == True:
          score += 1
          print(f"You are correct. Current score: {score}")
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
    clear()
    return


play_game()   