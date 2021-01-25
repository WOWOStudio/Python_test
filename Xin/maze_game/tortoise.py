#小乌龟模型
from turtle import Turtle
class Tortoise(Turtle):
    def __init__(self,maze_list,start_m,start_n,end_m,end_n):
        Turtle.__init__(self)
        self.maze_list = maze_list
        self.m = start_m
        self.n = start_n
        self.end_m = end_m
        self.end_n = end_n
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.goto(self.n*20-120,120-self.m*20)
        self.shape('turtle')
        self.color('#28bea0')
        self.setheading(270)
        self.showturtle()
        screen = self.getscreen()
        screen.addshape('tortoise.gif')

    def reach_exit(self, m, n):
        if m == self.end_m and n == self.end_n:
            self.shape('tortoise.gif')

    def move(self,m,n):
        self.m = m
        self.n = n
        self.goto(self.n*20-120,120-self.m*20)
        self.reach_exit(m,n)

    def go_up(self):
        if self.canmove(self.m-1,self.n):
            self.setheading(90)
            self.move(self.m-1,self.n)

    def go_down(self):
        if self.canmove(self.m+1,self.n):
            self.setheading(270)
            self.move(self.m+1,self.n)

    def go_left(self):
        if self.canmove(self.m,self.n-1):
            self.setheading(180)
            self.move(self.m,self.n-1)

    def go_right(self):
        if self.canmove(self.m,self.n+1):
            self.setheading(0)
            self.move(self.m,self.n+1)

    def canmove(self,m,n):
        return self.maze_list[m][n] == 0
