# -*- coding: utf-8 -*-
"""
Snake03:
    Move the square up

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
head.penup()              #不用畫出筆跡
head.setheading(90)

while True:
    try:                  #關閉視窗時發生錯誤
        wn.update()
        head.forward(20)

        time.sleep(delay) #讓迴圈0.1秒跑一圈
        
    except:
        turtle.exitonclick() #正確關閉視窗
        break

wn.mainloop()
turtle.done()    #Spyder要加
turtle.bye()     #Spyder要加