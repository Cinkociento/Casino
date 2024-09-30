import time
import random
import sys

print('Welcome to my game called "Roulette"')
print("Remember hazard is ilegal! Don't play this game with your friend!")

time.sleep(3.5)

ready = input("Are toy ready?: ")

if ready == "yes" or "Yes":
  print("Your number is drawn")
  time.sleep(2.5)
  user_number = [random.randint(0, 100)]
  print("Your number is ")
  print(user_number)
else:
  sys.exit(1)
  SystemExit(1)

time.sleep(2)

win_number = [random.randint(0, 100)]

print("When you win you see True")
print(win_number in user_number)

time.sleep(2.5)

print("Win numer is: ")
print(win_number)

time.sleep(3)