print("Welcome to Python Pizza Deliveries!")


size = input('What size pizza do you want? S, M or L: \n')
if size == 'S' or  size == 's':
    bill = 15
elif size == 'M' or  size == 'm':
    bill = 20
elif size == 'L' or  size == 'l':
    bill = 25    
else:
    print("Wrong size")
    quit()

pepperoni = input('Do you want pepperoni on your pizza? Y or N : \n')
if pepperoni == 'Y' or pepperoni == 'y':
    if size == 'S' or size == 's':
        bill = bill + 2
    else:
        bill = bill + 3
cheese = input('Do you want extra cheese? Y or N : \n')        
if cheese == 'Y' or cheese == 'y':
    bill +=1


print(f"Your final bill is ${bill}")