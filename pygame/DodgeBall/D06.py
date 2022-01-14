# -*- coding: utf-8 -*-
"""
Dodge Ball 06: 
    圓往右邊移動
    碰到邊緣....先從另一邊出來吧
    
@author: Jeff
"""

import pygame

#常數 - 視窗寬、高
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480

#常數 - 顏色
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#球的變數
ball_R = 25
ball_x = SCREEN_WIDTH//2
ball_y = SCREEN_HEIGHT//2


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Dodge Ball")

clock = pygame.time.Clock()

running = True
while running:

    #輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #計算
    ball_x += 5
    if ball_x > SCREEN_WIDTH:  #如果球心到了最右邊
        ball_x = 0             #就把球重新定位到最左邊

    #更新畫面
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (ball_x,ball_y), ball_R)

    
    clock.tick(30)
    pygame.display.update()
    
    
pygame.quit()