#draw a square
from turtle import Turtle, Screen

new_turtle = Turtle()
screen = Screen()

new_turtle.shape('turtle')

for _ in range(4):
    new_turtle.forward(100)
    new_turtle.left(90)
    
#Without for but same solution
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
# new_turtle.left(90)
# new_turtle.forward(100)
# new_turtle.left(90)

