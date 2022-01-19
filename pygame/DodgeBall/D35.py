# -*- coding: utf-8 -*-
"""
Dodge Ball 35: 
    慢慢消失不見
    
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

CDTIMEUP = pygame.USEREVENT + 1
ONESTIMEUP = pygame.USEREVENT + 2

#球的類別
class Ball(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.R = 25
        self.SPEED = 10
        self.ANGLE = random.randint(16, 75)/180*math.pi
        self.x_speed = self.SPEED * math.sin(self.ANGLE) * random.choice([-1,1])
        self.y_speed = self.SPEED * math.cos(self.ANGLE) * random.choice([-1,1])
        #加入籃球圖片
        self.raw_image = pygame.image.load("res\\basketball.png").convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (self.R*2,self.R*2))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH-self.R*2)
        self.rect.y = random.randint(0, SCREEN_HEIGHT-self.R*2)
        
    def update(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.x_speed *= -1
        if self.rect.bottom > SCREEN_HEIGHT or self.rect.top < 0:
            self.y_speed *= -1

    def speedup(self):
        self.SPEED +=2
        if self.x_speed>0:
            self.x_speed = self.SPEED* math.sin(self.ANGLE)
        else:
            self.x_speed = -self.SPEED* math.sin(self.ANGLE)
        if self.y_speed>0:   
            self.y_speed = self.SPEED* math.cos(self.ANGLE)
        else:
            self.y_speed = -self.SPEED* math.cos(self.ANGLE)
        print(self.SPEED)
        
#貓咪的類別
class Cat(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        #加入貓咪圖片
        self.raw_image = pygame.image.load("res\\cat.png").convert_alpha()
        self.raw_image2 = pygame.image.load("res\\cat2.png").convert_alpha()
        self.image = pygame.transform.scale(self.raw_image, (95,100))
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH//2
        self.rect.centery = SCREEN_HEIGHT//2
        self.status = 1  #1:alive, 0:dying, -1:dead
        self.alpha = 255 #透明度 255:不透明， 0:全透明
    
    def update(self):
        if self.status == 1:   #活著就跟著滑鼠
            mouse_pos = pygame.mouse.get_pos()
            self.rect.center = (mouse_pos[0], mouse_pos[1])
        elif self.status == 0: #要死了就慢慢消失
            if self.alpha > 0:
                self.alpha -=5
                self.image.set_alpha(self.alpha)
                if self.alpha <= 0:
                    self.status = -1   #完全消失就死掉了
            
    def green(self):
        self.image = pygame.transform.scale(self.raw_image2, (95,100))
    
    def normal(self):
        self.image = pygame.transform.scale(self.raw_image, (95,100))
         

#顯示生命數
def drawLife(screen, font, life):
        life_surf = font.render("Life: "+str(life), True, RED)
        life_rect = life_surf.get_rect()
        life_rect.x = 520
        life_rect.y = 10
        screen.blit(life_surf, life_rect)
        
#顯示遊戲時間
def drawTimer(screen, font, timer):
        timer_surf = font.render("Time: "+str(timer), True, BLUE)
        timer_rect = timer_surf.get_rect()
        timer_rect.x = 50
        timer_rect.y = 10
        screen.blit(timer_surf, timer_rect)
        

#主程式
def main():

    life = 10
    timer = 0
    cooldowntime = 0 
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Dodge Ball")

    clock = pygame.time.Clock()
    pygame.time.set_timer(ONESTIMEUP, 1000)
    
    bg_raw_image = pygame.image.load("res\\background.png").convert_alpha()
    bg_img = pygame.transform.scale(bg_raw_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    meow_snd = pygame.mixer.Sound("res\\Meow.wav")
    life_font = pygame.font.SysFont(None, 30)
    timer_font = pygame.font.SysFont(None, 30)
    ball = Ball()
    cat = Cat()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(cat)
    all_sprites.add(ball)
    ball_sprites = pygame.sprite.Group()
    ball_sprites.add(ball)
    
    running = True
    while running:
    
        #輸入
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == CDTIMEUP:
                cooldowntime = 0
                cat.normal()
                pygame.time.set_timer(CDTIMEUP, 0)
            elif event.type == ONESTIMEUP:
                timer += 1
                if timer%10==0:
                    for aball in ball_sprites:
                        aball.speedup()
                if timer==20:
                    ball2=Ball()
                    all_sprites.add(ball2)
                    ball_sprites.add(ball2)
    
        #計算
        all_sprites.update()
    
        #更新畫面
        #背景
        screen.blit(bg_img, (0,0))
        all_sprites.draw(screen)
        
        #生命數
        drawLife(screen, life_font, life)
        #遊戲時間
        drawTimer(screen, timer_font, timer)
        
        clock.tick(30)
        pygame.display.update()
        
        hit = pygame.sprite.spritecollide(cat, ball_sprites, False, pygame.sprite.collide_mask)
        if cooldowntime==0 and len(hit)!=0 :
            pygame.time.set_timer(CDTIMEUP, 3000)
            cooldowntime = 1
            life -= 1
            cat.green()
            meow_snd.play()
            if life==0: 
                cat.status = 0    #沒命時只改變貓咪的狀態
        
        if cat.status == -1:      #最後由貓咪的狀態來判斷是否結束遊戲
            running = False
    
    pygame.quit()


#程式起點
if __name__ == "__main__":
    main()