import time
import random

list = ["The best way to get on with something is to stop talking and start doing", "Much seems impossible until you do it", "Don't let yesterday's day take away too much from today", "Everything is in our hands, therefore they cannot be omitted. "," Only the one who does, will learn something. "," Whatever you learn, you learn for yourself. " " try to do everything well: it will turn out badly by itself. "]

print("Hi, you can write your plan")
def rus():
  name=input("Name: ")
  while True:
    date=int(input("Please enter the year:"))
    if date<=2022:
      print("Wrong. Please enter the current one:")
    if date>=2022:
      month=int(input('Month: '))
      # if month>=13:
      #   print("Wrong. Please indicate again")
      day=int(input('Day: '))
      # if day>=31:
      #   print("Wrong. Please indicate again")
      hour=int(input('Time: '))
      print("What will I remind you of?")
      text = input()
      print("In how many minutes?")
      # Here you first write checking number in range         0.1 to 0.9 this is just for checking
      clock = float(input())
      clock = clock * 60
      time.sleep(clock)
      print("Do" + text)
      print("Quote of the Day: ",random.choice(list))
rus()    
       
      
