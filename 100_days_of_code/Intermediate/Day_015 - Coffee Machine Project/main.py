import resources

loop = True

def coins_prompt(beverage):
    print("Please insert coins.")
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickles = int(input('How many nickles? '))
    pennies = int(input('How many pennies? '))
    
    price = resources.drinks[beverage]['price']    
    total = (resources.coins['quarter'] * quarters) + (resources.coins['dime'] * dimes) + (resources.coins['nickle'] * nickles) + (resources.coins['penny'] * pennies)
    
    if total >= price:
        change = total - price
        print(f'Here is ${change:.2f} in change.')
        return True   
    
    else:    
        # print("Sorry that's not enough money. Money refunded")
        return False


def manage_coffee_machine(beverage):
    
    if  beverage == 'espresso':
        
        if  resources.resource_machine['Water'] < resources.drinks[beverage]['water'] :
            return "Sorry there is not enough water."
        elif resources.resource_machine['Coffee'] < resources.drinks[beverage]['coffee']:
            return "Sorry there is not enough coffee."  
              
        else:
            if coins_prompt(beverage): #only proceed if payment succeeded   
                resources.resource_machine['Water'] -= resources.drinks[beverage]['water']       
                resources.resource_machine['Coffee'] -= resources.drinks[beverage]['coffee']
                resources.resource_machine['Money'] += resources.drinks[beverage]['price']
                return f"Here is your {beverage}. Enjoy!"
            else:
                  return "Sorry that's not enough money. Money refunded"
        
    else:
        if  resources.resource_machine['Water'] < resources.drinks[beverage]['water']:
            return "Sorry there is not enough water."
        elif resources.resource_machine['Coffee'] < resources.drinks[beverage]['coffee']:
            return "Sorry there is not enough coffee."  
        elif resources.resource_machine['Milk'] < resources.drinks[beverage]['milk']:
            return "Sorry there is not enough milk." 
        else:
            if coins_prompt(beverage): #only proceed if payment succeeded           
                resources.resource_machine['Water'] -= resources.drinks[beverage]['water']
                resources.resource_machine['Milk'] -= resources.drinks[beverage]['milk']
                resources.resource_machine['Coffee'] -= resources.drinks[beverage]['coffee']
                resources.resource_machine['Money'] += resources.drinks[beverage]['price']
                return f"Here is your {beverage}. Enjoy!"
            else:
                  return "Sorry that's not enough money. Money refunded"
                
        
        


while loop:
    choise = input('What would you like? (espresso/latte/cappuccino): ')
    if choise.lower() == 'report':
        for i in resources.resource_machine:
            unit = resources.units.get(i, "")
            if resources.units == '$':
                print(f'{i} : {unit}{resources.resource_machine[i]}')
            else:
                print(f'{i} : {resources.resource_machine[i]}{unit}')
            
    elif choise.lower() == 'espresso':        
        print(manage_coffee_machine(choise.lower()))
        
     
    elif choise.lower() == 'latte':       
        print(manage_coffee_machine(choise.lower()))


    elif choise.lower() == 'cappuccino':        
        print(manage_coffee_machine(choise.lower()))
        
       
    elif choise.lower() == 'off':
        print('Shutting down for maintenance')
        loop = False
        
    else:
        print('Invalid Option.')   
