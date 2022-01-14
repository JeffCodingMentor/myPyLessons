# -*- coding: utf-8 -*-
"""
Dodge Ball 12: 
    把球改成使用class
    
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

#球的類別
class Ball:
    def __init__(self):
        self.R = 25         #球所有的的變數全部搬過來
        self.SPEED = 10
        self.ANGLE = random.randint(1, 360)/180*math.pi        
        self.x = random.randint(self.R, SCREEN_WIDTH-self.R)
        self.y = random.randint(self.R, SCREEN_HEIGHT-self.R)
        self.x_speed = self.SPEED * math.sin(self.ANGLE)
        self.y_speed = self.SPEED * math.cos(self.ANGLE)

#主程式
def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Dodge Ball")

    clock = pygame.time.Clock()
    
    ball = Ball()   #建立一顆球
    
    running = True
    while running:
    
        #輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        #計算
        ball.x += ball.x_speed   #所有變數 ball_ 變成 ball.
        ball.y += ball.y_speed
        if ball.x+ball.R > SCREEN_WIDTH or ball.x-ball.R < 0:
            ball.x_speed *= -1
        if ball.y+ball.R > SCREEN_HEIGHT or ball.y-ball.R < 0:
            ball.y_speed *= -1
    
        #更新畫面
        screen.fill(WHITE)
        pygame.draw.circle(screen, BLUE, (ball.x,ball.y), ball.R)
    
        
        clock.tick(30)
        pygame.display.update()
        
        
    pygame.quit()


#程式起點
if __name__ == "__main__":
    main()