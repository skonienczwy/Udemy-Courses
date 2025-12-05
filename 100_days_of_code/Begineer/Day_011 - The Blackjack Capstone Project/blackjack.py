import random
import art

def balckjack():
    print(art.logo)
    cards = [11,11,11,11, 2,2,2,2, 3,3,3,3,  4,4,4,4, 5,5,5,5,  6,6,6,6, 7,7,7,7, 8,8,8,8, 9,9,9,9, 10,10,10,10, 10,10,10,10, 10,10,10,10, 10,10,10,10]
    player_cards = [] 
    computer_cards = []
    game = True 

    def initial_hand():
        for _ in range(2):#The underscore _ is used as a placeholder to indicate that the loop variable is not going to be used.        
            card = random.choice(cards)
            player_cards.append(card)
            cards.remove(card)
        card = random.choice(cards)
        computer_cards.append(card)
        cards.remove(card)
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)} ")
        print(f"Computer's first card: {computer_cards}")   

    def player_hands():
        card = random.choice(cards)
        player_cards.append(card)
        cards.remove(card)
        return player_cards

    def computer_hands(player_result):
        while player_result > sum(computer_cards) and sum(computer_cards) <= 17:
            card = random.choice(cards)
            computer_cards.append(card)
            cards.remove(card)
        return computer_cards    

    def calculate_score(player_score, computer_score):
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        if player_score == 21 and computer_score == 21:
            return f"It is draw: Computer Score:{computer_score}, Your score:{player_score}"
        elif player_score == 21 and computer_score < 21:
            return f"Player Wins: Computer Score:{computer_score}, Your score:{player_score}"
        elif player_score < 21 and player_score > computer_score:
            return f"Player Wins: Computer Score:{computer_score}, Your score:{player_score}"
        elif computer_score > 21:
            return f"Player Wins: Computer Score:{computer_score}, Your score:{player_score}"
        else:
            return f"Computer Wins: Computer Score:{computer_score}, Your score:{player_score}"
    
    
   
    initial_hand()
    while game:
        choice = input("Type 'Y' to get another card, type 'N' to pass: ").lower()
        
        if choice == 'y':
            player_hands()
            print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
            if sum(player_cards) > 21:
                game = False
                break
        else:
            computer_hands(sum(player_cards))
            print(f"Computer's cards: {computer_cards}, Computer's score: {sum(computer_cards)}")
            game = False
            break

    player_score = sum(player_cards)
    computer_score = sum(computer_cards)
    print(calculate_score(player_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'Y' or 'N': ").lower() == 'y':
    print("\n" *20)
    balckjack()