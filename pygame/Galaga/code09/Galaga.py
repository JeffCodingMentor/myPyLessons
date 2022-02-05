# -*- coding: utf-8 -*-
"""
Galaga.py
    Galaga main code

@author: JCM
"""

import pygame
import os, random
import Config as cfg
from Player import Player
from Laser import Laser, Enemy_Laser
from Enemy import Enemy, Enemy2

class Game():
    def __init__(self):
        self.game_status = "Logo"
        
        logo_raw_image = pygame.image.load( os.path.join("..","res","Galaga_Logo.png") )
        self.logo_img = pygame.transform.scale(logo_raw_image, (384,190))
        self.logo_rec = self.logo_img.get_rect(center=(cfg.SCREEN_WIDTH//2, 280))
        self.font = pygame.font.Font(None, 25)
        self.font_suf = self.font.render("Press Space to start", False, "white")
        self.font_rec = self.font_suf.get_rect(center=(cfg.SCREEN_WIDTH//2, 440))

        self.laser_grp = pygame.sprite.Group()
        self.enemy_grp = pygame.sprite.Group()
        self.enemy_laser_grp = pygame.sprite.Group()
        self.level = 1
        self.score = 0

    def start_game(self):
        self.player = Player() #((cfg.SCREEN_WIDTH,cfg.SCREEN_HEIGHT))
        self.player_grp = pygame.sprite.GroupSingle(self.player)
        self.shoot_able = True
        self.last_shoot_tick = 0
        self.enemy_step = 1
        self.create_enemy(self.level)
        
        self.last_shoot_tick = pygame.time.get_ticks() - 300
        if self.level == 1: self.score=0
        
    def pass_level(self):
        if self.player_grp: self.player_grp.empty()
        if self.player: self.player.kill()
        if self.enemy_grp: self.enemy_grp.empty()
        if self.laser_grp: self.laser_grp.empty()
        if self.enemy_laser_grp: self.enemy_laser_grp.empty()
        
    def end_game(self):
        self.game_status= "Logo"
        self.level = 1
        if self.player_grp: self.player_grp.empty()
        if self.player: self.player.kill()
        if self.enemy_grp: self.enemy_grp.empty()
        if self.laser_grp: self.laser_grp.empty()
        if self.enemy_laser_grp: self.enemy_laser_grp.empty()
        
    def create_enemy(self, level):
        self.enemy_count = 0        
        for i in range(7):
            enemy = Enemy(i*55+75, 40)
            self.enemy_grp.add(enemy)
            self.enemy_count += 1
        if level > 1:
            for i in range(7):
                enemy = Enemy(i*55+75, 90)
                self.enemy_grp.add(enemy)
                self.enemy_count += 1
        if level > 2:
            for i in range(7):
                enemy = Enemy2(i*55+75, 140)
                self.enemy_grp.add(enemy)
                self.enemy_count += 1
            
    def enemy_check(self):
        for enemy in self.enemy_grp:
            if enemy.rect.right >= cfg.SCREEN_WIDTH or enemy.rect.left <= 0:
                self.enemy_step *= -1
                break
                
    def check_coliision(self):
        if self.laser_grp:
            if pygame.sprite.groupcollide(self.laser_grp, self.enemy_grp, True, True):
                self.enemy_count -= 1
                self.score += 1
                if self.enemy_count == 0:
                    self.level += 1
                    if self.level < 4:
                        self.game_status = "Level"
                        self.pass_level()
                    else:
                        self.game_status = "Logo"
                        self.end_game()                        
                    
        if self.enemy_laser_grp:
            if pygame.sprite.spritecollide(self.player, self.enemy_laser_grp, True):
                self.end_game()
        
        if self.enemy_grp:
            if pygame.sprite.spritecollide(self.player, self.enemy_grp, True):
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

    def pick_enemy_attck(self):
        if self.enemy_grp:
            isAttacking = False
            for enemy in self.enemy_grp:
                if enemy.status == cfg.ENMY_STATUS_ATTCK:
                    isAttacking = True
                    break
            if isAttacking == False:
                enemy_attack = random.choice(self.enemy_grp.sprites())
                if enemy_attack.status == cfg.ENMY_STATUS_READY:
                     enemy_attack.status = cfg.ENMY_STATUS_ATTCK
                     print(type(enemy_attack), enemy_attack.status)
            
    def show_logo(self):
        screen.blit(self.logo_img, self.logo_rec)
        screen.blit(self.font_suf, self.font_rec)
        if self.score != 0:
            self.score_suf = self.font.render(f"Your score:{self.score}", False, "white")
            self.score_rec = self.score_suf.get_rect(center=(cfg.SCREEN_WIDTH//2, 470))                
            screen.blit(self.score_suf, self.score_rec)
    
    def show_level(self):
        self.level_suf = self.font.render(f"Level:{self.level}", False, "white")
        self.level_rec = self.level_suf.get_rect(center=(cfg.SCREEN_WIDTH//2, 400))                
        screen.blit(self.level_suf, self.level_rec)
        

    def run(self):
        if self.game_status == "Run":
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
                
        elif self.game_status == "Logo":
            self.show_logo()
            
        elif self.game_status == "Level":
            self.show_level()

if __name__ == "__main__":
    
    pygame.init()
    screen = pygame.display.set_mode((cfg.SCREEN_WIDTH,cfg.SCREEN_HEIGHT))
    pygame.display.set_caption("Galaga")
    clock = pygame.time.Clock()
    
    ENEMY_LASER_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMY_LASER_EVENT,900)
    ENEMY_ATTACK_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(ENEMY_LASER_EVENT,1500)
    
    
    game = Game()
  
    running = True
    while running:
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if game.game_status == "Logo":
                        game.game_status= "Level"
                    elif game.game_status == "Level":
                        game.start_game()
                        game.game_status = "Run"
                        
            if event.type == ENEMY_LASER_EVENT:
                if game.game_status == "Run":
                    game.shoot_enemy_laser()

            if event.type == ENEMY_ATTACK_EVENT:
                if game.game_status == "Run" and game.level>1:
                    game.pick_enemy_attck()
                    
        screen.fill("black")
        
        game.run()
        
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()