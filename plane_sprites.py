import random
from plane_main import *
import pygame


#屏幕大小
SCREEN_RECT = pygame.Rect(0,0,512,768)
#屏幕刷新率
FRAME_PER_SEC = 120
#创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
#英雄子弹间隔
CREATE_HERO_COOL = pygame.USEREVENT +1
#英雄移动速度
HERO_SPEED = 3
#英雄子弹精灵组
hero_bullte_group = pygame.sprite.Group()
#英雄子弹冷却
FIRECOOL = True




class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_name,speed=1):

        super().__init__()

        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class Backgroud(GameSprite):
    #游戏背景精灵
    def update(self):

        #调用父类方法实现
        super().update()

        #判断是否出屏幕
        if self.rect.y>=SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    #敌机精灵类

    def __init__(self):
        #创建敌机精灵，指定图片
        super().__init__("./image/enemy1.png")
        #指定敌机初始速度
        self.speed = random.randint(1,3)
        #随机敌机初始位置
        self.rect.bottom = 0

        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0,max_x)

    def update(self):
        #调用父类方法 保持垂直方向飞行
        super().update()
        #判断是否出屏幕
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机挂了 %s" % self.rect)

class Hero(GameSprite):
    #英雄精灵
    def __init__(self):
        super().__init__("./image/hero0.png",0)

        #设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120



    def update(self,xspeed=0,yspeed=0):

        self.rect.x += xspeed
        self.rect.y += yspeed

        if self.rect.x < 0 :
            self.rect.x = 0
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        elif self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        #创建英雄子弹精灵
        hero_bullte = Bullte("./image/hero_bullet.png",-6)

        #设定位置
        hero_bullte.rect.bottom = self.rect.y - 10
        hero_bullte.rect.centerx  = self.rect.centerx

        hero_bullte.add(hero_bullte_group)

    def __del__(self):
        # 声明静态方法
        @staticmethod
        def __game_over():
            print("游戏结束")
            pygame.quit()
            exit()





class Bullte(GameSprite):

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()


    def __del__(self):
        print("子弹被销毁")

