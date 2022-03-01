# -*- coding: utf-8 -*-
"""
Snake07:
    tail

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
head.goto(10,10)
head.direction = 'stop'

food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(random.randrange(-290, 310, 20), random.randrange(-290, 310, 20))

tails=[]   #尾巴用list管理

def game_reset():
    head.goto(10,10)
    head.direction = 'stop'
    food.goto(random.randrange(-290, 310, 20), random.randrange(-290, 310, 20))
    for tail in tails:   #沒有辦法實際刪除，就移到外面去
        tail.goto(1000,1000)
    tails.clear()  #結束時記得清掉list
    
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
    move_tails() #必須先移動尾巴
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
    
def move_tails():  #尾巴移動的方式，從最後一節往前移
    for i in range(len(tails)-1, 0, -1):
        x = tails[i-1].xcor()
        y = tails[i-1].ycor()
        tails[i].goto(x, y)
    if len(tails) > 0:  #第一節移到head的位置
        x = head.xcor()
        y = head.ycor()
        tails[0].goto(x, y)

def add_tail():    #新加tail的方式
        new_tail = turtle.Turtle()
        new_tail.shape("square")
        new_tail.color("orange")
        new_tail.penup()
        new_tail.goto(head.xcor(), head.ycor())  #先定位到head
        tails.append(new_tail)

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
            add_tail()
        
        time.sleep(delay)

    except:
        turtle.exitonclick()
        break

wn.mainloop()
turtle.done()
turtle.bye()