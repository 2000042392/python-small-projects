import random
print("Welcome to the Number Guessing Game")
number= random.randint(1,100)
attempt=0

while True:
    try:
     guess=int(input("Guess the number"))
     attempt+=1
     if guess<number:
         print("Too low")
     elif guess>number:
         print("Too high")
     else:
         print("congratulations")
         print("You guessed the number")
         print("Number of attempts: ",attempt)
         break


    except ValueError:
      print("Please enter a valid number.")
