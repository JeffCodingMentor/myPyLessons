# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:17:46 2021

@author: ManaTsao
"""

import pygame
import random

WIDTH = 500
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        
        # self.rect.x = 0
        # self.rect.y = 400
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-10
        
        self.speedx = 8 #Jeff: ??
        
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        # self.rect.x +=2
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
            
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-3, 3)
        
    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))
        self.image.fill((255,255,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()


all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
for i in range(8):
    r = Rock()
    all_sprites.add(r)
    rocks.add(r)


# Jeff: Same with here
# screen.fill((255,255,255))
# pygame.display.flip() #Not in video!

running = True

while running:
    clock.tick(60)
    
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            
    # Update
    all_sprites.update()
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True) 
    #Jeff: hits is a Dict
    for hit in hits:
        r=Rock()
        all_sprites.add(r)
        rocks.add(r)
        
    hits = pygame.sprite.spritecollide(player, rocks, False)
    #Jeff: hits is a List
    if hits:
        running = False
    
    # Render
    screen.fill((0,0,0))
    all_sprites.draw(screen)
    pygame.display.update()
    
pygame.quit()
