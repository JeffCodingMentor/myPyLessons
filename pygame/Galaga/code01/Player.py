# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 14:25:35 2022

@author: ManaTsao
"""
import pygame
import os

WIDTH = 45
HEIGHT = 50

class Player(pygame.sprite.Sprite):

    def __init__(self, screen_size):
        super().__init__()
        self.screen_size = screen_size
        raw_image = pygame.image.load(os.path.join("..","res","player.png")).convert_alpha()
        self.image = pygame.transform.scale(raw_image, (WIDTH,HEIGHT))
        self.rect = self.image.get_rect(bottom=self.screen_size[1]-10)
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = (mouse_pos[0])
        if self.rect.left < 0: self.rect.left=0
        if self.rect.right > self.screen_size[0]: self.rect.right = self.screen_size[0]
        