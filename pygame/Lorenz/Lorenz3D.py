# -*- coding: utf-8 -*-
"""
Lorenz 3D: 
   Lorenz Attractor 3D
    
@author: Jeff
"""

import pygame
import projection as pj

def lorenz(x, y, z, s=10, r=28, b=2.667):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
pygame.init()
pygame.display.set_caption("Lorenz Attractor")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((0,0,0))

dt = 0.01
SCALE = 10

ang_x = 60
ang_y = 45
ang_z = -20

x, y, z = 0.1, 1., 1.05
x_2d, y_2d, _ = pj.project(x, y, z, ang_x, ang_y, ang_z)
screen_x = int(x_2d*SCALE) + SCREEN_WIDTH//2
screen_y = int(y_2d*SCALE) + (SCREEN_HEIGHT//2)*1.7

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    dx, dy, dz = lorenz(x, y, z)

    x = x + dx*dt
    y = y + dy*dt
    z = z + dz*dt
    
    prv_x = screen_x
    prv_y = screen_y
    
    color = pygame.Color(0)
    h = int(z/70*360)
    color.hsva = (h, 100, 100, 1)
    
    x_2d, y_2d, _ = pj.project(x, y, z, ang_x, ang_y, ang_z)
    screen_x = int(x_2d*SCALE) + SCREEN_WIDTH//2
    screen_y = int(y_2d*SCALE) + (SCREEN_HEIGHT//2)*1.7

    pygame.draw.line(screen, color, (prv_x, prv_y), (screen_x,screen_y))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()