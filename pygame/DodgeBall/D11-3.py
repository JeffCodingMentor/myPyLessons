# -*- coding: utf-8 -*-
"""
Dodge Ball 11-3: 
    把"籃球"畫漂亮一點
    1.改用convert_alpha避免把原有黑色變成透明
    2.改用svg檔
    
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
    ball_x = random.randint(ball_R, SCREEN_WIDTH-ball_R)
    ball_y = random.randint(ball_R, SCREEN_HEIGHT-ball_R)
    ball_SPEED = 10
    ball_ANGLE = random.randint(1, 360)/180*math.pi
    ball_x_speed = ball_SPEED*math.sin(ball_ANGLE)
    ball_y_speed = ball_SPEED*math.cos(ball_ANGLE)
    

    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Dodge Ball")

    ball_img = pygame.image.load("res\\basketball.png").convert_alpha() #用convert_alpha也可，就不用設定透明色了
    #ball_img = pygame.image.load("res\\basketball.svg")
    ball_img = pygame.transform.scale(ball_img, (50,50))  #用svg這行就可以拿掉
    ball_rect = ball_img.get_rect()
    
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
        #pygame.draw.circle(screen, BLUE, (ball_x,ball_y), ball_R)
        ball_rect.center = (ball_x, ball_y)            #圖框的中心點設為x, y座標
        screen.blit(ball_img, ball_rect)               #畫圖的時候是以rect為基準
        
        clock.tick(30)
        pygame.display.update()
        
        
    pygame.quit()


#這裡才是程式開始的地方
if __name__ == "__main__":
    main()