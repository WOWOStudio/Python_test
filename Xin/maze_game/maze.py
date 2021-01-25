from turtle import Turtle
class Maze(Turtle):
    size = 20

    def __init__(self,maze_list):
        Turtle.__init__(self)
        self.maze_list = maze_list
        self.hideturtle()
        self.speed(0)
        self.draw_walls()

    def draw_wall(self):
        self.pendown()
        self.begin_fill()
        self.color('#7392f6')
        for i in range(4):
            self.forward(self.size)
            self.right(90)
        self.end_fill()
        self.penup()

    def draw_walls(self):
        self.penup()
        self.goto(-130,130)
        for row in range(13):
            for col in range(13):
                if self.maze_list[row][col]:
                    self.draw_wall()
                self.goto(self.size*(col+1)-130,130-self.size*row)
            self.goto(-130,130-self.size*(row+1))
