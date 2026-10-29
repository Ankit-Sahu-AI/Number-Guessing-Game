#Number Guessing Game

#use random library for secret number
import random
#computer choose a number between 1 to 100
secret_number = random. randint(1, 100)
#Disply with some designing
print("\n\t\t🕹Number Guessing❓Game👾")
#instruction for the game:
print("\nI choose a number between [1 to 100]\nCan you guess my secret number under 5 attempts🤓")
#make a loop for asking choose multiple times
attempt = 0
while True:
  guess = int(input("\nTell me your guess : "))
  attempt += 1
  if guess < secret_number:
    print("\nIt's too low 📉, Try again🥱")
  elif guess > secret_number:
    print("\nIt's too high 📈, Try again🥱")
  else :
    print(f"\n\tBooyah!🎉 You won🏆\nYou guess the right secret number in just {attempt} attempts")
    break
  if attempt == 5:
    print("\nGame Over💀👎\nYou lost this game, Try again😿")
    break
