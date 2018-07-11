"""This program is dice roll and guess the number"""
from random import randint
from time import sleep
def get_user_guess():
  guess=int(raw_input("Guess a number: "))
  return guess
def roll_dice(number_of_sides):
  first_roll=randint(1,number_of_sides)
  second_roll=randint(1,number_of_sides)
  max_val=number_of_sides*2
  print "%d "%(max_val)
  guess=get_user_guess()
  if guess > max_val:
    print "Invalid guess"
  else:
    print "Rolling..."
    sleep(2)
    print "%d "%(first_roll)
    sleep(1)
    print "%d " %(second_roll)
    sleep(1)
    total_roll=first_roll+second_roll
    print "Result..."
    sleep(1)
    if guess==total_roll:
      print "Congratulations ! You Won."
    else:
      print "Oops! You lost"
         
roll_dice(6)
  
  
  
  
  
  
  
