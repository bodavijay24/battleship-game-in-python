"""This program is Rock , Paper, scissor game
@BodaVijay
"""
from random import randint
options=["ROCK","PAPER","SCISSORS"]
message ={"tie" : "Yawn it's a tie!",
         "won":"Yay you won!",
         "lost" :"Aww you lost!"}
def decide_winner(user_choice,computer_choice):
  print "User choice : %s  "%(user_choice)
  print "Computer choice : %s "%(computer_choice)
  if user_choice==computer_choice:
    print message["tie"]
  elif user_choice ==options[0] and computer_choice ==options[2]:
    print message["won"]
  elif user_choice ==options[1] and computer_choice==options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice==options[1]:
    print message["won"]
  else:
    print message["lost"]
    
def play_RFS():
  user_choice=raw_input("Enter Rock, Paper, or Scissors").upper()
  index=randint(0,2)
  computer_choice=options[index]
  decide_winner(user_choice,computer_choice)
play_RFS()
  
    
  
  
  
