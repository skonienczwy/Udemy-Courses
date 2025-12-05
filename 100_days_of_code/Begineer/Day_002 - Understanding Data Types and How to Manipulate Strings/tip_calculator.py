print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? \n$"))
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
people = float(input("How many people to split the bill?\n"))

bill = (bill*(tip/100))+bill
result = bill / people

print(f"Each person should pay: ${round(result,2)}")

