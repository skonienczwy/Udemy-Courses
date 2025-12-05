import random
import art
# number = random.randrange(1,100)
# number = 30
# guess = 29
# result = number - guess
# print(result)

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking o a number between 1 and 100.")
choose = input("Choose a diffilty. Type 'easy' or 'hard': ").lower()
attempts = 0

if choose == 'easy':
    attempts = 10
else:
    attempts = 5
number = random.randrange(1,100)

# def guessing_game(guess,turn):
        
#         result = number - guess
#         if result > 0:
#             print("Too low") 
#             return turn - 1          

            
#         elif result < 0:
#             print("Too high")
#             return turn - 1                                
#         else:
#             print(f"You got it! The answer was {number}")
                

  

while attempts != 0:
    
    print(f"You have {attempts} remaining to guess the number.") 
    print(number)   
    guess = int(input("Make a guess: "))
   
    result = number - guess
    if result > 0:
        print("Too low")
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The answer was {number}")
        
    elif result < 0:
        print("Too high")
        attempts -= 1
        if attempts == 0:
            print(f"You've run out of guesses. The answer was {number}")

    else:
        print(f"You got it! The answer was {number}")
        attempts = 0        




    






