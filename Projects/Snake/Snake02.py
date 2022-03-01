# -*- coding: utf-8 -*-
"""
Snake02:
    Python Turtle draw a square

@author: JCM
"""

import turtle

wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.tracer(0)   #畫完再更新畫面

#角度設定為0 代表turtle(指標)朝東方向、90 朝北、180朝西、270朝南。
#畫x, y軸
turtle.penup()
turtle.goto(-300,0)
turtle.setheading(0)
turtle.pendown()
turtle.forward(600)
turtle.penup()

turtle.goto(0,-300)
turtle.pendown()
turtle.setheading(90)
turtle.forward(600)
turtle.penup()

#建立一個方形黑色的畫筆，預設大小20x20，定位到中心(0,0)
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.goto(0,0)

wn.update()      #更新畫面

wn.mainloop()
turtle.done()    #Spyder要加
turtle.bye()     #Spyder要加