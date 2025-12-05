import art

print(art.logo)
print("Welcome to the secret auction program.")

auction = True
bids = {}

def max_bid(bids_to_check):
    max_value = 0
    winner = ''
    for i in bids_to_check:
            if bids_to_check[i] > max_value:            
                max_value = bids_to_check[i]  
                winner = i          
    print(f"The winner is {winner} with a bid of {max_value}.")

while auction:
    name = input("What is your name?: ")
    bid =   int(input("What's your bid?: $"))
    bids[name] = bid
    keep_going = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if keep_going == 'no':
        # winner = ''
        max_bid(bids_to_check=bids)
        auction = False

      


