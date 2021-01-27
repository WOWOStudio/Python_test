#控制器模型
from turtle import Turtle

class controller(Turtle):
    def __init__(self, go_up, go_down, go_left, go_right):
        Turtle.__init__(self)
        self.go_up = go_up
        self.go_down = go_down
        self.go_left = go_left
        self.go_right = go_right
        self.hideturtle()
        self.speed(0)
        self.draw_btn('上', -162, 130)
        self.draw_btn('下', 132, 130)
        self.draw_btn('左', -162, -100)
        self.draw_btn('右', 132, -100)
        screen = self.getscreen()
        screen.onclick(self.handlescreenclik)

    def draw_btn(self, name, x, y):
        self.penup()
        self.goto(x,y)
        self.begin_fill()
        self.color('#000000')
        for i in range(4):
            self.forward(30)
            self.right(90)
        self.end_fill()
        self.color('#ffffff')
        self.goto(x+7, y-20)
        self.write(name, font = ('Simhei', 12, 'normal'))

    def handlescreenclik(self, x, y):
        if x < 0 and y > 0:
            self.go_up()
        if x > 0 and y > 0:
            self.go_down()
        if x < 0 and y < 0:
            self.go_left()
        if x > 0 and y < 0:
            self.go_right()
