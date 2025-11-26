from random import randint
import arts

images = [arts.rock, arts.paper, arts.scissor]

print("Welcome to Rock, Paper and Scissor game.")
choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. \n"))

computer_choice = randint(0,2)

if choose == 0 and computer_choice == 0:
    print("You choose Rock")
    print(images[0])
    print("Computer choose Rock")
    print(images[0])
    print("It's a Draw, nobody wins!")
elif choose == 0 and computer_choice == 1:
    print("You choose Rock")
    print(images[0])
    print("Computer chooses Paper")
    print(images[1])
    print("Paper beats Rock. Computer Wins!")
elif choose == 0 and computer_choice == 2:
    print("You choose Rock")
    print(images[0])
    print("Computer chooses Scissor")
    print(images[2])
    print("Rock beats Scissor. You Win!")

elif choose == 1 and computer_choice == 0:
    print("You choose Paper")
    print(images[1])
    print("Computer chooses Rock")
    print(images[0])
    print("Paper beats Rock. You Win!")
elif choose == 1 and computer_choice == 1:
    print("You choose Paper")
    print(images[1])  
    print("Computer chooses Paper")  
    print(images[1])    
    print("It's a Draw, nobody wins!")
elif choose == 1 and computer_choice == 2:
    print("You choose Paper")
    print(images[1])
    print("Computer chooses Scissor")  
    print(images[2])
    print("Scissor beats Paper. Computer Wins!")
    
elif choose == 2 and computer_choice == 0:
    print("You choose Scissor")
    print(images[2])
    print("Computer chooses Rock")  
    print(images[0])
    print("Rock beats Scissors. Computer Wins!")
elif choose == 2 and computer_choice == 1:
    print("You choose Scissor")
    print(images[2])
    print("Computer chooses Paper")  
    print(images[1])
    print("Scissor beats Paper.You Win! ")
elif choose == 2 and computer_choice == 2:
    print("You choose Scissor")
    print(images[2])
    print("Computer chooses Scissor")  
    print(images[2])
    print("It's a Draw, nobody wins!")    
else:
    print("You typed an invalid option.")


    
