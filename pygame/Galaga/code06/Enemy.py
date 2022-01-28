# -*- coding: utf-8 -*-
"""
Enemy.py
    Enemy class

@author: JCM
"""

import pygame
import os

WIDTH = 45
HEIGHT = 45

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        raw_image = pygame.image.load(os.path.join("..","res","enemy1.png")).convert_alpha()
        raw_image = pygame.transform.rotate(raw_image, 90)
        self.image = pygame.transform.scale(raw_image, (WIDTH,HEIGHT))
        self.rect = self.image.get_rect(center=(x,y))
        
    def update(self, step):
        self.rect.x += step