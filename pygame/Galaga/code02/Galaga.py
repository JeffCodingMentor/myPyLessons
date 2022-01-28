# -*- coding: utf-8 -*-
"""
Galaga.py
    Galaga main code

@author: JCM
"""

import pygame
import os
from Player import Player
from Laser import Laser

class Game():
    def __init__(self):
        self.game_active = False
        
        logo_raw_image = pygame.image.load( os.path.join("..","res","Galaga_Logo.png") )
        self.logo_img = pygame.transform.scale(logo_raw_image, (384,190))
        self.logo_rec = self.logo_img.get_rect(center=(SCREEN_WIDTH//2, 280))
        self.font = pygame.font.Font(None, 25)
        self.font_suf = self.font.render("Press Space to start", False, "white")
        self.font_rec = self.font_suf.get_rect(center=(SCREEN_WIDTH//2, 440))
        
        self.player = Player((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.player_grp = pygame.sprite.GroupSingle(self.player)
        
        self.laser_grp = pygame.sprite.Group()
        
    def run(self):
        
        if self.game_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                laser = Laser(self.player.rect.center)
                self.laser_grp.add(laser)
              
            self.player_grp.update()
            self.laser_grp.update()
            self.player_grp.draw(screen)
            self.laser_grp.draw(screen)
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.game_active=True

            screen.blit(self.logo_img, self.logo_rec)
            screen.blit(self.font_suf, self.font_rec)
            

if __name__ == "__main__":
    
    SCREEN_WIDTH  = 480
    SCREEN_HEIGHT = 640
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Galaga")
    clock = pygame.time.Clock()
    
    game = Game()
  
    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        screen.fill("black")
        
        game.run()
        
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()