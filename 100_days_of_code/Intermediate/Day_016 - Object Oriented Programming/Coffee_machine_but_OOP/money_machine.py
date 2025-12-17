COINS = {'penny': 0.01, 'nickel': 0.05, 'dime': 0.10, 'quarter': 0.25}
CURRENCY = '$'

class MoneyMachine:
    def __init__(self, money = 0):
        self.money = money
    
    def get_valid_int(self, message):
        while True:
            try:
                value = int(input(message))
                if value < 0:
                    print("Please enter a non-negative number.")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number.")

    
       
    def coins_prompt(self, cost):
        print("Please insert coins.")
        quarters = self.get_valid_int('How many quarters? ')
        dimes = self.get_valid_int('How many dimes? ')
        nickel = self.get_valid_int('How many nickels? ')
        pennies = self.get_valid_int('How many pennies? ')   
          
        total = (COINS['quarter'] * quarters) + \
                (COINS['dime'] * dimes) + \
                (COINS['nickel'] * nickel) + \
                (COINS['penny'] * pennies) 
                
        if total >= cost:
         print(f'Here is {CURRENCY}{total-cost:.2f} in change.')
         self.money += cost
         return True
        else:
            print("Sorry that's not enough money. Money refunded")
            return False
        
    def report(self):
        return print(f'{CURRENCY}{self.money:.2f}')
