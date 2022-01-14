# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:17:46 2021

@author: ManaTsao
"""

import pygame
import random
import os

WIDTH = 500
HEIGHT = 600

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

# Loading images
background_img = pygame.image.load(os.path.join("img","background.png")).convert()
player_img = pygame.image.load(os.path.join("img","player.png")).convert()
#rock_img = pygame.image.load(os.path.join("img","rock.png")).convert()
bullet_img = pygame.image.load(os.path.join("img","bullet.png")).convert()
rock_imgs = []
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img",f"rock{i}.png")).convert())
    
expl_anim = {}
expl_anim['lg']=[]
expl_anim['sm']=[]
for i in range(9):
    expl_img = pygame.image.load(os.path.join("img",f"expl{i}.png")).convert()
    expl_img.set_colorkey((0,0,0))
    expl_anim['lg'].append(pygame.transform.scale(expl_img, (75,75)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img, (30,30)))
    
# Loading music
shoot_sound = pygame.mixer.Sound(os.path.join("sound","shoot.wav"))
expl_sounds = [
    pygame.mixer.Sound(os.path.join("sound","expl0.wav")),
    pygame.mixer.Sound(os.path.join("sound","expl1.wav"))
    ]
pygame.mixer.music.load(os.path.join("sound","background.ogg"))
pygame.mixer.music.set_volume(0.2)
    
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)
    
def new_rock():
    r=Rock()
    all_sprites.add(r)
    rocks.add(r)
    
def draw_health(surf, hp, x, y):
    if hp < 0:
        hp = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (hp/100)*BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, (0,255,0), fill_rect)
    pygame.draw.rect(surf, (255,255,255), outline_rect, 2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #self.image = player_img
        self.image = pygame.transform.scale(player_img, (50,38))
        self.image.set_colorkey((0,0,0)) #Jeff:Make black to transparent
        self.rect = self.image.get_rect()
        self.radius = 20 #Jeff: for collide_circle
        # pygame.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
        # self.rect.x = 0
        # self.rect.y = 400
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT-10
        
        self.speedx = 8 #Jeff: ??
        self.health = 100
        
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        # self.rect.x +=2
        # if self.rect.left > WIDTH:
        #     self.rect.right = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
            
    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play() 
            
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_ori = random.choice(rock_imgs)
        self.image_ori.set_colorkey((0,0,0))
        self.image = self.image_ori.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width*0.8/2) #Jeff: for collide_circle
        # pygame.draw.circle(self.image, (255,0,0), self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH-self.rect.width)
        self.rect.y = random.randrange(-180, -100)
        self.speedy = random.randrange(2, 10)
        self.speedx = random.randrange(-3, 3)
        self.total_degree = 0
        self.rot_degree = random.randrange(-2, 2)
        
    def roate(self):
        self.total_degree += self.rot_degree
        self.total_degree %= 360
        self.image = pygame.transform.rotate(self.image_ori, self.total_degree)
        center = self.rect.center
        self.rect = self.image.get_rect()
        self.rect.center = center
        
    def update(self):
        self.roate() #Jeff: image 失真
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH-self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(2, 10)
            self.speedx = random.randrange(-3, 3)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speedy = -10
        
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = expl_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks() #Jeff:初始化到現在的毫秒數
        self.frame_rate = 50 #Jeff:至少經過幾毫秒才會更新下一秒圖片
        
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame +=1
            if self.frame == len(expl_anim[self.size]):
                self.kill()
            else:
                self.image = expl_anim[self.size][self.frame]
                center = self.rect.center
                self.rect = self.image.get_rect()
                self.rect.center = center

all_sprites = pygame.sprite.Group()
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)
for i in range(8):
    new_rock()
score = 0
pygame.mixer.music.play(-1)

# Jeff: Same with here
# screen.fill((255,255,255))
# pygame.display.flip() #Not in video!

running = True

while running:
    clock.tick(60)
    
    # Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            
    # Update
    all_sprites.update()
    hits = pygame.sprite.groupcollide(rocks, bullets, True, True) 
    #Jeff: hits is a Dict (key is rock)
    for hit in hits:
        #random.choice(expl_sounds).play()
        expl_sounds[0].play() #Jeff: Revise
        score += hit.radius
        expl = Explosion(hit.rect.center, 'lg')
        all_sprites.add(expl)
        new_rock()
        
    hits = pygame.sprite.spritecollide(player, rocks, True, pygame.sprite.collide_circle)
    #Jeff: hits is a List of rocks                    --!
    for hit in hits:
        expl_sounds[1].play() #Jeff: Revise
        new_rock()
        player.health -= hit.radius
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        if player.health <=0:
            running = False
    
    # Render
    screen.fill((0,0,0))
    screen.blit(background_img, (0,0))
    all_sprites.draw(screen)
    draw_text(screen, str(score), 18, WIDTH/2, 10)
    draw_health(screen, player.health, 5, 15)
    pygame.display.update()
    
pygame.quit()
