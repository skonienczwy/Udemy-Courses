import game_data
import random
import art     

# Copy the data to work with
data_copy = game_data.data.copy()
game = True
score = 0 
place_holder = random.choice(data_copy)
data_copy.remove(place_holder)

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

while game:
    print(art.logo)
    if len(data_copy) != 0:
        b = random.choice(data_copy)
        data_copy.remove(b)
        
        
        print(f"Compare A: {format_data(place_holder)}")
        print(art.vs)
        print(f"Against B: {format_data(b)}")
        
        
        choose = input("Who has more followers? 'A' or 'B': ").lower()
        
        if choose == 'a' and place_holder['follower_count'] > b['follower_count']:
            score += 1
            print(f"You're right! Current score: {score}")
            
        elif choose == 'b' and b['follower_count'] > place_holder['follower_count']:
            score += 1
            place_holder = b  # Update place_holder to b since b is the new choice
            print(f"You're right! Current score: {score}")
            
        else:
            game = False
            print(f"Sorry, that's wrong. Final score: {score}")
        
        # Update place_holder to be the last correct choice
        if choose == 'a' and place_holder['follower_count'] > b['follower_count']:
            place_holder = place_holder  # No change
            
        elif choose == 'b' and b['follower_count'] > place_holder['follower_count']:
            place_holder = b  # Update place_holder to b
        
    else:
        game = False
        print(f'Your knowledge is incredible; you nailed the entire list. Your final score is {score}.')