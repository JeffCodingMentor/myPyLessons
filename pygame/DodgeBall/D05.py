# -*- coding: utf-8 -*-
"""
Dodge Ball 05: 
    圓往右邊移動
    解決移動太快問題
    
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

#加入一個時鐘
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    pygame.draw.circle(screen, BLUE, (ball_x,ball_y), ball_R)
    ball_x += 5  #這裡改成5也沒關係了
    
    clock.tick(30)  #時鐘限制每秒更新30次
    pygame.display.update()
    
    
pygame.quit()