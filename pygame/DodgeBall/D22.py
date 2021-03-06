# -*- coding: utf-8 -*-
"""
Dodge Ball 22: 
    喵喵叫了
    
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
class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.R = 25
        self.SPEED = 10
        self.ANGLE = random.randint(1, 360)/180*math.pi        
        self.x_speed = self.SPEED * math.sin(self.ANGLE)
        self.y_speed = self.SPEED * math.cos(self.ANGLE)
        #加入籃球圖片
        self.raw_image = pygame.image.load("res\\basketball.png").convert_alpha()
        self.img = pygame.transform.scale(self.raw_image, (self.R*2,self.R*2))
        self.rect = self.img.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH-self.R*2)
        self.rect.y = random.randint(0, SCREEN_HEIGHT-self.R*2)
        
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.x_speed *= -1
        if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            self.y_speed *= -1


#貓咪的類別
class Cat(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #加入貓咪圖片
        self.raw_image = pygame.image.load("res\\cat.png").convert_alpha()
        self.img = pygame.transform.scale(self.raw_image, (95,100))
        self.rect = self.img.get_rect()
        self.rect.centerx = SCREEN_WIDTH//2
        self.rect.centery = SCREEN_HEIGHT//2
        
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.center = (mouse_pos[0], mouse_pos[1])

#主程式
def main():

    score = 0
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Dodge Ball")

    clock = pygame.time.Clock()
    
    bg_raw_image = pygame.image.load("res\\background.png").convert_alpha()
    bg_img = pygame.transform.scale(bg_raw_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    meow_snd = pygame.mixer.Sound("res\\Meow.wav")  #載入聲音檔
    ball = Ball()
    cat = Cat()
    
    running = True
    while running:
    
        #輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        #計算
        ball.update()
        cat.update()
    
        #更新畫面
        #背景
        screen.blit(bg_img, (0,0))
        #籃球
        screen.blit(ball.img, ball.rect)
        #貓咪
        screen.blit(cat.img, cat.rect)
        
        clock.tick(30)
        pygame.display.update()
        
        if pygame.sprite.collide_rect(ball,cat):
            score += 1
            meow_snd.play()   #碰到了會喵喵叫
            print (score)
    pygame.quit()


#程式起點
if __name__ == "__main__":
    main()