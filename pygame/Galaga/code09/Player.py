# -*- coding: utf-8 -*-
"""
Player.py
    Player class

@author: JCM
"""
import pygame
import os
import Config as cfg

WIDTH = 45
HEIGHT = 50

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        raw_image = pygame.image.load(os.path.join("..","res","player.png")).convert_alpha()
        self.image = pygame.transform.scale(raw_image, (WIDTH,HEIGHT))
        self.rect = self.image.get_rect(bottom=cfg.SCREEN_HEIGHT-10)
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.centerx = (mouse_pos[0])
        if self.rect.left < 0: self.rect.left=0
        if self.rect.right > cfg.SCREEN_WIDTH: self.rect.right = cfg.SCREEN_WIDTH