# -*- coding: utf-8 -*-
"""
Snake01:
    Python Turtle basics

@author: JCM
"""

import turtle

wn = turtle.Screen()
wn.setup(width=600, height=600)

#角度設定為0 代表turtle(指標)朝東方向、90 朝北、180朝西、270朝南。
turtle.setheading(90)
turtle.forward(100)

turtle.mainloop()
turtle.done()    #Spyder要加
turtle.bye()     #Spyder要加