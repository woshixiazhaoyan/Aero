import pygame
from pygame.locals import *
from plane_sprites import *

screen = pygame.display.set_mode((480 , 800))
pygame.init()
clock = pygame.time.Clock()

"""bg = pygame.image.load("./image/078.jpg")
screen.blit(bg,(0,0))"""
hero = pygame.image.load("./image/hero0.png")
screen.blit(hero, (200, 600))

#英雄
hero_rect = pygame.Rect(200,600,140,178)

#敌人
enemy = GameSprite("./image/enemy1.png")
enemy1 = GameSprite("./image/enemy1.png",2)

#背景
bg = Backgroud("./image/078.jpg")
bg1 = Backgroud("./image/078.jpg")
bg1.rect.y = -SCREEN_RECT.height

#添加敌机，背景精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)
backgroud_group = pygame.sprite.Group(bg,bg1)

while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            pygame.quit()
            exit()
    clock.tick(60)
    if(hero_rect.y <= -178):
        hero_rect.y = 800
    hero_rect.y -= 3

    # 绘制背景
    backgroud_group.update()
    backgroud_group.draw(screen)

    # 绘制精灵组
    enemy_group.update()
    enemy_group.draw(screen)

    #绘制英雄
    screen.blit(hero,hero_rect)

    pygame.display.update()