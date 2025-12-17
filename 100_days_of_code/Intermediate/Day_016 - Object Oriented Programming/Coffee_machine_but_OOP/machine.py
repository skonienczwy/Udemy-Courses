from menu import drinks

class CoffeeMaker:
    def __init__(self, water = 300, milk = 200, coffee = 100 ):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        
    def report(self):
        print(f'Water: {self.water}ml')
        print(f'Milk: {self.milk}ml')
        print(f'Coffee: {self.coffee}g')            
    
    def is_resource_sufficient(self, drink):
        ingredients = drinks[drink]['ingredients']
        for item, amount_needed in ingredients.items():
            current_amount = getattr(self, item)
            if amount_needed > current_amount:
                print(f'Sorry there is not enough {item}.')
                return False
        return True
            
    def make_coffe(self, order):
        ingredients = drinks[order]['ingredients']
        for item, amount in ingredients.items():
            current_value = getattr(self, item)
            setattr(self, item, current_value - amount )
        print(f'Here is your {order}. Enjoy!') 
     
    def off(self):
        return 'Shutting down for maintenance'
         
