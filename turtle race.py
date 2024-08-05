from turtle import Turtle,Screen
import random
screen=Screen()

colors=["red","green","blue","yellow","purple","orange"]
y_cordinates=[-120,-90,-60,-30,0,30]
all_turtles=[]
user_choice=screen.textinput(title="Select your turtle",prompt="Which turtle will win the race? Enter your Color: ")

is_race_on=False


for turtle_index in range(0,5):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235,y=y_cordinates[turtle_index])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on=True
    
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 250:
            is_race_on=False
            winning_color=turtle.pencolor()
            if winning_color==user_choice:
                print(f"You won!.The {winning_color} is winner.")
            else:
                print(f"you lose! the winning turtle is {winning_color}. ")
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
    
screen=Screen()
screen.setup(width=500,height=400)
screen.exitonclick()
