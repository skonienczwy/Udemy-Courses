resource_machine = {'water':300, 'milk':200, 'coffee':100}
test = str(resource_machine.values())

# for i in resource_machine:
#     print(f'{i} : {resource_machine[i]}')

drinks = {
    'espresso':
    {
    'price':  1.50,
    'water':  50, 
    'coffee': 18
    },
    
    'latte':
    {
    'price':  2.50,
    'water':  200,
    'coffee': 24,
    'milk':   150
    },
    'capuccino':
    {
    'price': 3.00,
    'water': 250,
    'coffee': 24,
    'milk' : 100        
    }
    }

print(drinks['espresso'])