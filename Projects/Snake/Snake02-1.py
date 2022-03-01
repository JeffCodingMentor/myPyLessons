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

for x in range(-300, 320, 20):
    turtle.penup()
    turtle.goto(x,300)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(600)
    turtle.penup()

for y in range(-300, 320, 20):
    turtle.goto(-300,y)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(600)
    turtle.penup()


wn.update()      #更新畫面

wn.mainloop()
turtle.done()    #Spyder要加
turtle.bye()     #Spyder要加