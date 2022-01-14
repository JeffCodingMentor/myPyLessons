# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:17:46 2021

@author: ManaTsao
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

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
    
    # Render
    screen.fill((255,255,255))
    pygame.display.update()
    
pygame.quit()
