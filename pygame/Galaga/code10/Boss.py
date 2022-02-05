# -*- coding: utf-8 -*-
"""
Boss.py
    Boss class

@author: JCM
"""

import pygame
import os
import Config as cfg

WIDTH = 120
HEIGHT = 120

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join("..","res","boss.png")).convert_alpha()
        raw_image = pygame.transform.rotate(raw_image, -90)
        self.image = pygame.transform.scale(raw_image, (WIDTH,HEIGHT))
        self.rect = self.image.get_rect(center=(cfg.SCREEN_WIDTH//2,100))
        self.step = 2
        self.life = 100
    
    def update(self):
        self.rect.x += self.step
        if self.rect.right >= cfg.SCREEN_WIDTH:
            self.step *= -1
        if self.rect.left <= 0:
            self.step *=-1
        