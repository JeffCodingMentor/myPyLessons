# -*- coding: utf-8 -*-
"""
Dodge Ball 01: 
    pygame範本
    
@author: Jeff
"""

import pygame

pygame.init()
screen = pygame.display.set_mode((640,480))  #設定視窗
pygame.display.set_caption("Dodge Ball")     #視窗名稱

running = True
while running:                #重複直到running變成False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #收到視窗Ｘ
            running = False
            
    screen.fill((255,255,255))            #視窗填滿白色
    pygame.display.update()               #更新畫面
    
    
pygame.quit()                 #停止全部