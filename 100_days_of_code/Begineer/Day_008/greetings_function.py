def greet():
    print("Hello")
    print("How Are you doing?")

#greet()    
   
#Functions that allows for inputs

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How Are you doing {name}?")
          
# name = input("What is your name?")

# greet_with_name(name)


#Functions with more than 1 input


def greet_with(name, location):
    print(f"Welcome {name} to The {location}")
#The order should be the same as the variables of the function.
greet_with( "Vitor","Netherlands")    

def greet_with(name, location):
    print(f"Welcome {name} to The {location}")

#The order doesn't matter if define the name of the variables of the function.
greet_with( location="Netherlands",name="Vitor")  