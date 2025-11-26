
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to Treasure Island. Your mission is to find the treasure")

left_or_right = input('You\'re at a crossroad. Where do you want to go?  '
                      'Type "Left" or "Right": ').lower()

if left_or_right == 'left':
    wait_or_swim = input('You\'ve come to a lake. There is an island in the middle of the lake. '
                         'Type "wait" for a boat. ' 
                         'Type "swim" to swim across. \n').lower()
    if wait_or_swim == 'wait':
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. \n'
                       'Which colour do you choose? \n').lower()
        if door == 'yellow':
            print('You found  the treasure. You Win!')
        elif door == 'blue':
            print('You enter a room of beasts. Game Over!')
            quit()
        elif door == 'red':
            print('It is a room full of fire. Game Over!')
            quit()
        else:
            print('Your option does not exist...you are dead. Game Over!')
    else:
        print('You were attacked by trout. Game Over!')
        quit()



else:
    print("You fell into a hole. Game Over.")   