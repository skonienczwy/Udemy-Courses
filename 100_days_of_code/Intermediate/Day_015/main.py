import resources
# print(resources.drinks)

loop = True

while loop:
    choise = input('What would you like? (espresso/latte/capuccino):\n')
    if choise.lower() == 'report':
        for i in resources.resource_machine:
            print(f'{i} : {resources.resource_machine[i]}')
    elif choise.lower() == 'espresso':
        print(resources.drinks['espresso'])
    elif choise.lower() == 'latte':
        print(resources.drinks['latte'])
    elif choise.lower() == 'capuccino':
        print(resources.drinks['capuccino'])
    elif choise.lower() == 'off':
        print('Shutting down for maintenance')
        loop = False
        break
    else:
        print('Invalid Option.')   
            
    # print(resources.resource_machine.fromkeys())