# -*- coding: utf-8 -*-
"""
Lorenz 2D: 
   Lorenz Attractor 2D (xy plane)
    
@author: Jeff
"""

import pygame
import math


def lorenz(x, y, z, s=10, r=28, b=2.667):
    """
    Given:
       x, y, z: a point of interest in three dimensional space
       s, r, b: parameters defining the lorenz attractor
    Returns:
       x_dot, y_dot, z_dot: values of the lorenz attractor's partial
           derivatives at the point x, y, z
    """
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
pygame.init()
pygame.display.set_caption("Lorenz Attractor")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen.fill((0,0,0))

running = True
x, y, z = 0.1, 1., 1.05
dt = 0.01
SCALE = 15
screen_x = int(x*SCALE) + SCREEN_WIDTH//2
screen_y = int(y*SCALE) + SCREEN_HEIGHT//2
min_z = math.inf
max_z = -math.inf

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
    
    min_z = min(min_z, z) # Find min z
    max_z = max(max_z, z) # Find max z
    
    color = pygame.Color(0)
    h = int(z/70*360)     # set color according to z value
    color.hsva = (h, 100, 100, 1)
    
    screen_x = int(x*SCALE) + SCREEN_WIDTH//2
    screen_y = int(y*SCALE) + SCREEN_HEIGHT//2
    pygame.draw.line(screen, color, (prv_x, prv_y), (screen_x,screen_y))
    
    pygame.display.update()
    clock.tick(60)

print(min_z, max_z)
pygame.quit()