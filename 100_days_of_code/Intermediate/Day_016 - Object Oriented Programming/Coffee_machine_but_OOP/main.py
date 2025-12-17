from menu import Menu, drinks
from machine import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
loop = True

while loop:    
    choice = input(f'What drink would you like?\n{menu.get_items()}\n')
    choice = choice.strip().lower()
    
    if choice == 'off':
        print(machine.off())
        loop = False
                
    elif choice == 'report':
        machine.report()
        money.report()
             
    
    elif choice not in drinks.keys():
        print('Invalid Option.')
       
    else:
        if machine.is_resource_sufficient(choice):      
            if money.coins_prompt(drinks[choice]['price']):
                machine.make_coffe(choice)            

          
            
