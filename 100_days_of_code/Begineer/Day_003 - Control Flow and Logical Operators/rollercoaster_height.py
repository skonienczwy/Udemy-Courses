print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n"))


if height >= 120:
    print("You are allowed to buy a ticket to the rollercoaster.")
    age = int(input("What is your age? \n"))
    if age <= 12:        
        bill = 5
    elif age >= 12 and age <= 18:       
        bill = 7 
    elif age >= 45 and age <=55:
        bill = 0             
    else:        
        bill = 12
        
    photo = input("Do you want to have a photo take? Types y for Yes and n for No. \n")   
    if photo =='y' or photo == 'Y':
        bill = bill + 3   
        print(f"The total price of the ticket is ${bill}") 
    elif photo =='n' or photo == 'N':
        print(f"The total price of the ticket is ${bill}") 
else:
    print("Unfortunatelly you can not buy a rollercoaster ticket.")

