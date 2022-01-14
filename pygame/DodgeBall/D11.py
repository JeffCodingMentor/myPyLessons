# -*- coding: utf-8 -*-
"""
Dodge Ball 11: 
    加入main()
    
@author: Jeff
"""

import pygame
import math, random

#常數 - 視窗寬、高
SCREEN_WIDTH  = 640
SCREEN_HEIGHT = 480

#常數 - 顏色
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#這裡是主程式函式
def main():

    #球的變數
    ball_R = 25
    ball_x = random.randint(ball_R, SCREEN_WIDTH-ball_R)  #注意要扣掉求半徑
    ball_y = random.randint(ball_R, SCREEN_HEIGHT-ball_R) #注意要扣掉求半徑
    ball_SPEED = 10
    ball_ANGLE = random.randint(1, 360)/180*math.pi
    ball_x_speed = ball_SPEED*math.sin(ball_ANGLE)
    ball_y_speed = ball_SPEED*math.cos(ball_ANGLE)

    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Dodge Ball")

    #加入一個時鐘
    clock = pygame.time.Clock()
    
    running = True
    while running:
    
        #輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        #計算
        ball_x += ball_x_speed
        ball_y += ball_y_speed
        if ball_x+ball_R > SCREEN_WIDTH or ball_x-ball_R < 0:
            ball_x_speed *= -1
        if ball_y+ball_R > SCREEN_HEIGHT or ball_y-ball_R < 0:
            ball_y_speed *= -1
    
        #更新畫面
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (ball_x,ball_y), ball_R)
    
        
        clock.tick(30)
        pygame.display.update()
        
        
    pygame.quit()


#這裡才是程式開始的地方
if __name__ == "__main__":
    main()