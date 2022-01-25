import numpy as np
import math
import pygame

def project(x, y, z, deg_x, deg_y, deg_z):
    angle_x = math.radians(deg_x)
    angle_y = math.radians(deg_y)
    angle_z = math.radians(deg_z)
    
    rotation_x = np.array([[1, 0, 0],
                           [0, math.cos(angle_x), -math.sin(angle_x)],
                           [0, math.sin(angle_x), math.cos(angle_x)]])

    rotation_y =np.array( [[math.cos(angle_y), 0, math.sin(angle_y)],
                           [0, 1, 0],
                           [-math.sin(angle_y), 0, math.cos(angle_y)]])

    rotation_z =np.array([[math.cos(angle_z), -math.sin(angle_z), 0],
                          [math.sin(angle_z), math.cos(angle_z), 0 ],
                          [0, 0, 1]])

    projection_mtrx = np.array([[1,0,0],
                                [0,1,0],
                                [0,0,0]])
        
    xyz_3d = np.array([[x],[y],[z]])
    rotx = np.matmul(rotation_x, xyz_3d)
    roty = np.matmul(rotation_y, rotx)
    rotz = np.matmul(rotation_z, roty)
    xyz_2d = np.matmul(projection_mtrx, rotz)
    
    return xyz_2d[0][0],xyz_2d[1][0],xyz_2d[2][0]
    
if __name__=="__main__":
    
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 400
    pygame.init()
    pygame.display.set_caption("Lorenz Attractor")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    font = pygame.font.Font(None, 20)

    ang_x = 0
    ang_y = 0
    ang_z = 0
    ANG_ROT=3

    running=True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            ang_x += ANG_ROT
            ang_x = 0 if ang_x==360 else ang_x
        if keys[pygame.K_a]:
            ang_x -= ANG_ROT
            ang_x = 0 if ang_x==-360 else ang_x
        if keys[pygame.K_w]:
            ang_y += ANG_ROT
            ang_y = 0 if ang_y==360 else ang_y
        if keys[pygame.K_s]:
            ang_y -= ANG_ROT            
            ang_y = 0 if ang_y==-360 else ang_y
        if keys[pygame.K_e]:
            ang_z += ANG_ROT
            ang_z = 0 if ang_z==360 else ang_z
        if keys[pygame.K_q]:
            ang_z -= ANG_ROT
            ang_z = 0 if ang_z==-360 else ang_z
            
        ax = (100, 0, 0)
        ay = (0, 100, 0)
        az = (0, 0, 100)
        o  = (0,  0,  0)
        
        axx, axy, _ = project(ax[0], ax[1], ax[2], ang_x, ang_y, ang_z)
        ayx, ayy, _ = project(ay[0], ay[1], ay[2], ang_x, ang_y, ang_z)
        azx, azy, _ = project(az[0], az[1], az[2], ang_x, ang_y, ang_z)
        
        axx += SCREEN_WIDTH//2; axy += SCREEN_HEIGHT//2
        ayx += SCREEN_WIDTH//2; ayy += SCREEN_HEIGHT//2
        azx += SCREEN_WIDTH//2; azy += SCREEN_HEIGHT//2
        
        screen.fill((0,0,0))
        pygame.draw.line(screen, (255,0,0), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (axx,axy))
        pygame.draw.line(screen, (0,255,0), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (ayx,ayy))
        pygame.draw.line(screen, (0,0,255), (SCREEN_WIDTH//2, SCREEN_HEIGHT//2), (azx,azy))
        
        ang_x_font = font.render("ang x: "+str(ang_x), True, (255,0,0))
        screen.blit(ang_x_font, (10,10))
        ang_y_font = font.render("ang y: "+str(ang_y), True, (0,255,0))
        screen.blit(ang_y_font, (10,30))
        ang_z_font = font.render("ang z: "+str(ang_z), True, (0,0,255))
        screen.blit(ang_z_font, (10,50))
            
        pygame.display.update()
        clock.tick(60)

    pygame.quit()