# -*- coding: utf-8 -*-
"""
Galaga.py
    Galaga main code

@author: JCM
"""

import pygame
import os, random
from Player import Player
from Laser import Laser, Enemy_Laser
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

        self.laser_grp = pygame.sprite.Group()
        self.enemy_grp = pygame.sprite.Group()
        self.enemy_laser_grp = pygame.sprite.Group()
        
        self.score = 0
        
    def start_game(self):
        self.player = Player((SCREEN_WIDTH,SCREEN_HEIGHT))
        self.player_grp = pygame.sprite.GroupSingle(self.player)
        
        self.shoot_able = True
        self.last_shoot_tick = 0

        self.enemy_step = 1
        self.enemy_count = 0
        self.score = 0
        self.create_enemy()
        
        self.last_shoot_tick = pygame.time.get_ticks() - 300
        
    def end_game(self):
        self.game_active=False
        if self.player_grp: self.player_grp.empty()
        if self.player: self.player.kill()
        if self.enemy_grp: self.enemy_grp.empty()
        if self.laser_grp: self.laser_grp.empty()
        if self.enemy_laser_grp: self.enemy_laser_grp.empty()
        
    def create_enemy(self):
        for i in range(7):
            enemy = Enemy(i*55+75, 40)
            self.enemy_grp.add(enemy)
            self.enemy_count += 1
            
    def enemy_check(self):
        for enemy in self.enemy_grp:
            if enemy.rect.right >= SCREEN_WIDTH or enemy.rect.left <= 0:
                self.enemy_step *= -1
                break
                
    def check_coliision(self):
        if self.laser_grp:
            if pygame.sprite.groupcollide(self.laser_grp, self.enemy_grp, True, True):
                self.enemy_count -= 1
                self.score += 1
                if self.enemy_count == 0:
                    self.end_game()
                    
        if self.enemy_laser_grp:
            if pygame.sprite.spritecollide(self.player, self.enemy_laser_grp, True):
                self.end_game()
            
    def shoot_laser(self):
        current_tick = pygame.time.get_ticks()
        if current_tick - self.last_shoot_tick > 500:
            laser = Laser(self.player.rect.center)
            self.laser_grp.add(laser)
            self.last_shoot_tick = current_tick
             
    def shoot_enemy_laser(self):
        if self.enemy_grp:
            enemy_firing = random.choice(self.enemy_grp.sprites())
            enemy_laser = Enemy_Laser(enemy_firing.rect.center)
            self.enemy_laser_grp.add(enemy_laser)
        
    def run(self):
        if self.game_active:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.shoot_laser()
              
            self.player_grp.update()
            self.laser_grp.update()
            self.enemy_laser_grp.update()
            self.check_coliision()
            self.enemy_grp.update(self.enemy_step)
            self.enemy_check()
            self.player_grp.draw(screen)
            self.laser_grp.draw(screen)
            self.enemy_laser_grp.draw(screen)
            self.enemy_grp.draw(screen)
                
        else:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.game_active=True
                self.start_game()
                
            screen.blit(self.logo_img, self.logo_rec)
            screen.blit(self.font_suf, self.font_rec)
            if self.score != 0:
                self.score_suf = self.font.render(f"Your score:{self.score}", False, "white")
                self.score_rec = self.score_suf.get_rect(center=(SCREEN_WIDTH//2, 470))                
                screen.blit(self.score_suf, self.score_rec)

if __name__ == "__main__":
    
    SCREEN_WIDTH  = 480
    SCREEN_HEIGHT = 640
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption("Galaga")
    clock = pygame.time.Clock()
    
    ENEMY_LASER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMY_LASER_EVENT,900)
    
    game = Game()
  
    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == ENEMY_LASER_EVENT:
                if game.game_active:
                    game.shoot_enemy_laser()
            
        screen.fill("black")
        
        game.run()
        
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()