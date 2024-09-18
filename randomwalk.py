from turtle import Turtle,Screen
import random

color_list = ['red', 'orange', 'yellow', 'green', 'blue','purple', 'pink', 'brown', 'gray', 'gold', 'cyan', 'Gainsboro','dimgray', 'LightSlateGray','AliceBlue', 'LimeGreen', 'DarkKhaki', 'Khaki']
moves = [0,90,180,270]
t = Turtle()
t.shape("arrow")
t.pensize(15)
t.speed('fastest')
screen = Screen()
screen.bgcolor("black")
for i in range(1,510):
    move = random.choice(moves)
    t.color(random.choice(color_list))
    t.forward(50)
    t.setheading(move)



t.home()
screen.exitonclick()