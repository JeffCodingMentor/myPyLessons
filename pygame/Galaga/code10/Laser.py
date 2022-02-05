# -*- coding: utf-8 -*-
"""
Laser.py
    Laser class

@author: JCM
"""
import pygame

WIDTH = 5
HEIGHT = 10

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.SPEED = 5
        self.image = pygame.Surface((WIDTH,HEIGHT))
        self.image.fill("red")
        self.rect = self.image.get_rect(center=pos)
    
    def update(self):
        self.rect.y -= self.SPEED
        if self.rect.y <= -10: self.kill()
        
class Enemy_Laser(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.SPEED = 5
        self.image = pygame.Surface((WIDTH,HEIGHT))
        self.image.fill("yellow")
        self.rect = self.image.get_rect(center=pos)
    
    def update(self):
        self.rect.y += self.SPEED
        if self.rect.y >= 650: self.kill()  #magic number