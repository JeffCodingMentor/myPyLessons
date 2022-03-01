# -*- coding: utf-8 -*-
"""
Snake09:
    score

@author: JCM
"""

import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

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

sc = turtle.Turtle()
sc.penup()
sc.hideturtle()
sc.goto(0, 250)
sc.color("white")
sc.write(f"Score : {score}  High Score : {high_score}", align="center",
          font=("Courier New", 20, "bold"))

def game_reset():
    global score
    head.goto(10,10)
    head.direction = 'stop'
    food.goto(random.randrange(-290, 310, 20), random.randrange(-290, 310, 20))
    for tail in tails:   #沒有辦法實際刪除，就移到外面去
        tail.goto(1000,1000)
    tails.clear()  #結束時記得清掉list
    score=0  #score歸零
    update_score()  #更新score

def update_score():
    sc.clear()
    sc.write(f"Score : {score}  High Score : {high_score}", align="center",
              font=("Courier New", 20, "bold"))

#收到按鍵要處理的函式
#不能回頭，不然就碰到尾巴了
def up():
    if head.direction != "down":    
        head.direction = "up"
 
def down():
    if head.direction != "up":
        head.direction = "down"
  
def left():
    if head.direction != "right":
        head.direction = "left"
 
def right():
    if head.direction != "left":   
        head.direction = "right"
    
def boudarycheck():
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        game_reset()

#檢查的方式是：是否有尾巴碰到身體
def tailcollidcheck():
    if len(tails) > 0:
        for tail in tails:
            if tail.distance(head)<20:
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
        tailcollidcheck()

        if head.distance(food) < 20:
            score+=1        #加1分
            if score > high_score: high_score = score
            update_score()  #更新score
            food.goto(random.randrange(-290, 310, 20), random.randrange(-290, 310, 20))
            add_tail()
        
        time.sleep(delay)

    except:
        turtle.exitonclick()
        break

wn.mainloop()
turtle.done()
turtle.bye()