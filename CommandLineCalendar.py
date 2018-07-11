"""Add ,view, delete events in Command line Calender 
by @Bodavijay"""
from time import sleep,strftime,gmtime
name=raw_input("Enter your name : ")
calendar={}
def welcome(name):
  print "Welcome "+name
  print "Calender is openeing..."
  sleep(1)
  print strftime("%a, %d %b %Y",gmtime())
  print strftime("%T",gmtime())
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome(name)
  start=True
  while start:
    user_choice=raw_input(" A to add \n U to update\n V to View \n D to Delete \n X to exit \n")
    user_choice=user_choice.upper()
    if user_choice =="V":
      if len(calendar.keys())==0:
        print "This calendar is empty"
      else:
        print(calendar)
    elif user_choice=="U":
      date=raw_input("What date?(MM/DD/YYYY) " )
      sleep(1)
      update=raw_input("Enter the update: ")
      calendar[date]=update
      sleep(0.5)
      print "Update Successful"
      print calendar
    elif user_choice=="A":
      event=raw_input("Enter event: ")
      date=raw_input("Enter date (MM/DD/YYYY) ")
      yea=int(strftime("%Y",gmtime()))
      new_year=int(date[6:10])
      if len(date)!=10 or yea<new_year:
        print "Invalid date!!"
        try_again=raw_input("Try Again? Y for Yes, N for No: ")
        try_again=try_again.upper()
        if try_again=="Y":
          continue
        else:
          print("Exiting program...")
          start=False
      else:
        calendar[date]=event
        print "Event Added Successfully"
        print calendar
    elif user_choice=="D":
        if len(calendar.keys())==0:
            print "This calendar is empty"
        else:
            event=raw_input("What event?")
            for date in calendar:
              if event==calendar[date]:
                del calendar[date]
                print "Deleted Successfully"
                print calendar
              else:
                print "incorrect information"
    elif user_choice=="X":
      start=False
    else:
      print "Invalid command"
      start=False

start_calendar() 
  
  
