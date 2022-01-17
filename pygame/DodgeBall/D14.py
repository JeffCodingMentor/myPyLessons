# -*- coding: utf-8 -*-
"""
Dodge Ball 14: 
    改用籃球 (參考D11-1, D11-2)
    
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
        #加入籃球圖片
        self.raw_image = pygame.image.load("res\\basketball.png").convert_alpha()
        self.img = pygame.transform.scale(self.raw_image, (50,50))
        self.rect = self.img.get_rect()
        
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x+self.R > SCREEN_WIDTH or self.x-self.R < 0:
            self.x_speed *= -1
        if self.y+self.R > SCREEN_HEIGHT or self.y-self.R < 0:
            self.y_speed *= -1

#主程式
def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Dodge Ball")

    clock = pygame.time.Clock()
    
    ball = Ball()
    
    running = True
    while running:
    
        #輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        #計算
        ball.move()
    
        #更新畫面
        screen.fill(WHITE)
        #換成籃球圖片
        ball.rect.center = (ball.x, ball.y)
        screen.blit(ball.img, ball.rect)
        
        clock.tick(30)
        pygame.display.update()
        
        
    pygame.quit()


#程式起點
if __name__ == "__main__":
    main()