# import turtle
#
# __Pen = turtle.Pen()
#
#
# def tou():
#
#     __Pen.pensize(5)
#     __Pen.pencolor("#003333")
#     __Pen.penup()
#     __Pen.goto(0, 50)
#     __Pen.pendown()
#     __Pen.circle(50)
#     __Pen.penup()
#     __Pen.goto((-10), 110)
#     __Pen.pendown()
#     __Pen.goto((-20), 110)
#     __Pen.penup()
#     __Pen.goto(10, 110)
#     __Pen.pendown()
#     __Pen.goto(20, 110)
#     __Pen.penup()
#     __Pen.goto(0, 75)
#     __Pen.pendown()
#     __Pen.circle(25, (-45))
#     __Pen.penup()
#     __Pen.setheading(0)
#     __Pen.goto(0, 75)
#     __Pen.pendown()
#     __Pen.circle(25, 45)
#
# def shen():
#
#     __Pen.penup()
#     __Pen.pencolor("#003333")
#     __Pen.goto(0, 50)
#     __Pen.pensize(5)
#     __Pen.pendown()
#     __Pen.goto(0, (-50))
#     __Pen.penup()
#     __Pen.pencolor("#003333")
#     __Pen.goto((-50), 60)
#     __Pen.pensize(5)
#     __Pen.pendown()
#     __Pen.goto(0, 20)
#     __Pen.pendown()
#     __Pen.pencolor("#003333")
#     __Pen.goto(50, 60)
#     __Pen.pensize(5)
#     __Pen.penup()
#     __Pen.goto(0, (-50))
#     __Pen.pendown()
#     __Pen.pencolor("#003333")
#     __Pen.goto((-50), (-100))
#     __Pen.pensize(5)
#     __Pen.penup()
#     __Pen.goto(0, (-50))
#     __Pen.pendown()
#     __Pen.goto(50, (-100))
#     __Pen.pencolor("#003333")
#
# tou()
# shen()


from turtle import *     #把一个模块的所有函数都导入进来，直接调用函数名即可使用

from time import sleep


def go_to(x, y):
    up()

    goto(x, y)

    down()

def head(x,y,r):

    go_to(x,y)

    speed(100)

    circle(r)

    leg(x,y)


def leg(x,y):


    right(90)

    forward(180)

    right(30)

    forward(100)

    left(120)

    go_to(x,y-180)

    forward(100)

    right(120)

    forward(100)

    left(120)

    hand(x,y)



def hand(x,y):

    go_to(x,y-60)

    forward(100)

    left(60)

    forward(100)

    go_to(x, y - 90)

    right(60)

    forward(100)

    right(60)

    forward(100)

    left(60)

    eye(x,y)


def eye(x,y):

    go_to(x-50,y+130)

    right(90)

    forward(50)

    go_to(x+40,y+130)

    forward(50)

    left(90)



def big_Circle(size):

    speed(200)

    for i in range(150):

        forward(size)

        right(0.3)

def line(size):

    speed(100)

    forward(51*size)



def small_Circle(size):

    speed(100)

    for i in range(210):

        forward(size)

        right(0.786)



def heart(x, y, size):

    go_to(x, y)

    left(150)

    begin_fill()

    line(size)

    big_Circle(size)

    small_Circle(size)

    left(120)

    small_Circle(size)

    big_Circle(size)

    line(size)

    end_fill()


def main():


    pensize(2) #笔迹的尺寸

    color('red', 'pink')  #颜色的设置，喜欢什么设置为什么

    head(-120, 100, 100)   #开始调用函数，画火柴人

    heart(250, -80, 1)   #开始调用函数，画爱心

    go_to(200, -250)    #移动着笔点坐标

    #write("送给心思梦绕的那个人", move=True, align="left", font=("宋体", 20, "normal"))
    #go_to(-100, -250)

    #write("作者本尊", move=True, align="left", font=("宋体", 20, "normal"))


    done()



main()
