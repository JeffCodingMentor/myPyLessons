# -*- coding: utf-8 -*-
"""
Snake06:
    bondarycheck, game reset

@author: JCM
"""

import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.bgcolor("green")
wn.tracer(0)

head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(10,10)   #這裡要做修改！！
head.direction = 'stop'

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randrange(-290, 310, 20), random.randrange(-290, 310, 20))

def game_reset():
    head.goto(10,10)
    head.direction = 'stop'
    food.goto(random.randrange(-290, 310, 20), random.randrange(-290, 310, 20))
    
#收到按鍵要處理的函式
def up():
    head.direction = "up"
 
def down():
    head.direction = "down"
  
def left():
    head.direction = "left"
 
def right():
    head.direction = "right"
    
def boudarycheck():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        game_reset()

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
        boudarycheck()
        
        if head.distance(food) < 20:
            food.goto(random.randrange(-290, 310, 20), random.randrange(-290, 310, 20))
        
        time.sleep(delay)

    except:
        turtle.exitonclick()
        break

wn.mainloop()
turtle.done()
turtle.bye()