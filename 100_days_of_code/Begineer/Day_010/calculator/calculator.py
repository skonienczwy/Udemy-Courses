import art

print(art.logo)



def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2




operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}


print(operations["*"](4, 8))

calc1 = True


while calc1:
    calc2 = True
    print(art.logo)
    number = int(input("What is the first number?: "))
    while calc2:
        print("+\n-\n*\n/")

        op = input("Pick an operation: ")
        number2 = int(input("What is the next number?: "))

        result = operations[op](number, number2)       
        print(f"{number} {op} {number2} = {result}")
        choose = input(f"Type 'Y' to continue calculating with {result}, or type 'N' to start a new calculation: ").lower()
        if choose ==  'n':
            calc2 = False
        else:
            number = result



