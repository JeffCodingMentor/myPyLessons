# -*- coding: utf-8 -*-
"""
Snake04:
    Move the square up/down/right/left

@author: JCM
"""

import turtle
import time

delay = 0.1

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("green")
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("black")
head.goto(0,0)
head.penup()
head.direction = 'stop'   #自己定義方向，初始為stop

#收到按鍵要處理的函式
def up():
    head.direction = "up"
 
def down():
    head.direction = "down"
  
def left():
    head.direction = "left"
 
def right():
    head.direction = "right"

#依照direction移動
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

#對應按鍵按下反應
wn.listen()
wn.onkeypress(up, "Up")
wn.onkeypress(down, "Down")
wn.onkeypress(left, "Left")
wn.onkeypress(right, "Right")

while True:
    try:
        wn.update()
        move()
        
        time.sleep(delay)

    except:
        turtle.exitonclick()
        break

wn.mainloop()
turtle.done()
turtle.bye()