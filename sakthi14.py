from art import logo,vs
import random
from game_data import data
from replit import clear

def print_data(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name} , a{description} , from {country}"

def check_answer(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess == "A"
  else :
    return guess == "B"

def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = random.choice(data)
  account_b = random.choice(data)

  while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
      account_b = random.choice(data)

    print(f"compare A: {print_data(account_a)}.")
    print(vs)
    print(f"Against B: {print_data(account_b)}.")

    guess = input("Who has more followers? type 'a'or 'b':").lower
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"you are right! current score:{score}")
    else:
      game_should_continue = False
      print(f"sorry,that's wrong.final score:{score}")

game()