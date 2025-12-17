drinks = {
    'espresso':
    {
    'price':  1.50,
    'ingredients': {'water': 50, 'coffee': 18, 'milk': 0}
    },
    
    'latte':
    {
    'price':  2.50,
    'ingredients': {'water': 200, 'coffee': 24, 'milk': 150}
    },
    'cappuccino':
    {
    'price': 3.00,
    'ingredients': {'water': 250, 'coffee': 24, 'milk': 100}    
    }
    } 

        
class Menu:
    def __init__(self):
        self.items = list(drinks.keys())
    
    def get_items(self):
        return "/".join(self.items)
    
    def find_drink(self, drink):
        if drink in self.items:
            return drink
        return None
       

