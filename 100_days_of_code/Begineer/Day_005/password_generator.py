import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
password_lenght =  int(input("How many letters would you like in your password?\n"))
password_numbers = int(input("How many numerbers would you like in your password?\n"))
password_symbols = int(input("How many symbols would you like in your password?\n"))

password_list = []
final_password = ''

#Return a random character (Required. A sequence like a list, a tuple, a range of numbers etc):
for i in range(1, password_lenght+1):
    password_list.append(random.choice(letters))

for i in range(1, password_numbers+1):    
    password_list.append(random.choice(numbers))
    
for i in range(1, password_symbols+1):    
    password_list.append(random.choice(symbols))


for i in password_list:
    final_password += i

print(f"Your password is : {final_password}")

