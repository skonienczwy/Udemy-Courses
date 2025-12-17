# from turtle import Turtle, Screen

# donatello = Turtle()



# my_screen = Screen()
# donatello.shape('turtle')
# donatello.color("Coral")
# donatello.forward(100)
# donatello.left(120)
# donatello.forward(100)
# donatello.left(120)
# donatello.forward(100)
# my_screen.exitonclick()



from  prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon',['Pikachu','Squirtle','Charmander','Bulbasaur'])
table.add_column('Type',['Electric','Water','Fire','Grass'])
print(table.align)
table.align="l"
print(table.align)

print(table)


