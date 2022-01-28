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
from Enemy import Enemy

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
        
        self.shoot_able = True
        self.last_shoot_tick = 0
        self.laser_grp = pygame.sprite.Group()
        
        self.enemy_step = 1
        self.create_enemy()
        
    def create_enemy(self):
        self.enemy_grp = pygame.sprite.Group()
        for i in range(7):
            enemy = Enemy(i*55+75, 40)
            self.enemy_grp.add(enemy)
            
    def enemy_check(self):
        for enemy in self.enemy_grp:
            if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                self.enemy_step *= -1
                break
                
    def check_coliision(self):
        if self.laser_grp:
            pygame.sprite.groupcollide(self.laser_grp, self.enemy_grp, True, True)
            
    def shoot_laser(self):
        current_tick = pygame.time.get_ticks()
        if current_tick - self.last_shoot_tick > 500:
            laser = Laser(self.player.rect.center)
            self.laser_grp.add(laser)
            self.last_shoot_tick = current_tick
              
        
    def run(self):
        
        if self.game_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.shoot_laser()
              
            self.player_grp.update()
            self.laser_grp.update()
            self.check_coliision()
            self.enemy_grp.update(self.enemy_step)
            self.enemy_check()
            self.player_grp.draw(screen)
            self.laser_grp.draw(screen)
            self.enemy_grp.draw(screen)
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.game_active=True
                self.last_shoot_tick = pygame.time.get_ticks() - 300

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