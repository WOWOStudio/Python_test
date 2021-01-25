import turtle
from random import randint

def draw_star():
  turtle.color('black')
  turtle.hideturtle()
  turtle.begin_fill()
  for i in range(5):
    turtle.forward(10)
    turtle.right(144)
  turtle.end_fill()

for i in range(50):
  turtle.speed(0)
  turtle.penup()
  x = randint(-150, 150)
  y = randint(-100, 100)
  turtle.goto(x, y)
  turtle.pendown()
  draw_star()

turtle.penup()
turtle.goto(0, -130)
turtle.pendown()
turtle.write('By 黄帮主',  font = ('SimHei', 12, 'bold'))
turtle.done()
