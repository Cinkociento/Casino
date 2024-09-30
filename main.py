import time
import random
import sys

print('Welcome to my game called "Roulette"')
print("Remember hazard is ilegal! Don't play this game with your friend!")

time.sleep(3.5)

ready = input("Are toy ready?: ")

if ready in ["yes", "Yes", "ya", "Ya", "Yes of course", "yes of course", "Of course", "of course"]:
  print("Your number is drawn")
  time.sleep(2.5)
  user_number = [random.randint(0, 100)]
  print("Your number is ")
  print(user_number)
else:
  print("ERROR! - You are stupid!")
  time.sleep(3)
  sys.exit(1)

time.sleep(2)

win_number = [random.randint(0, 100)]

print("When you win you see True")
print(win_number in user_number)

time.sleep(2.5)

print("Win numer is: ")
print(win_number)

time.sleep(3)

ready2 = input("do you want to play a different roulette game?: ")

if ready2 in ["yes", "Yes", "ya", "Ya", "Yes of course", "yes of course", "Of course", "of course"]:
  print('Welcome to my game called "Lotto"')
  print("Remember hazard is ilegal! Don't play this game with your friend!")
  time.sleep(5)

  for i in range(3):
    user_number = [int(input("Enter your 3 lucky number from 0 to 100: "))]

  print('When you win, you see "True"')
  time.sleep(2)

  for i in range(3):
    win_number = [random.randint(0, 100)]

  print(win_number in user_number)
  time.sleep(1.5)

  print("Win numer is: ")
  print(win_number)
  print("Game is end!")
  print("GoodBye!")
  time.sleep(3)
else:
  print("Game is successfully done!")
  print("GoodBye")
  time.sleep(3)
  sys.exit(1)