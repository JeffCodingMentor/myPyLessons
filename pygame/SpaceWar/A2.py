# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:17:46 2021

@author: ManaTsao
"""

import pygame

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
        self.rect.x = 0
        self.rect.y = 400
        #self.rect.center = (WIDTH/2, HEIGHT/2)
        
    def update(self):
        self.rect.x +=2
        if self.rect.left > WIDTH:
            self.rect.right = 0

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


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
            
    # Update
    all_sprites.update()
    
    # Render
    screen.fill((255,255,255))
    all_sprites.draw(screen)
    pygame.display.update()
    
pygame.quit()
