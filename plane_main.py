import pygame
from plane_sprites import *
from pygame.locals import *


class PlaneGame(object):

    #主程序
    def __init__(self):
        print("游戏初始化")

        #创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_RECT.size))
        #游戏时钟
        self.clock = pygame.time.Clock()
        #创建精灵组
        self.__create_sprites()
        #设置定时器时间——创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(CREATE_HERO_COOL, 200)

    def __create_sprites(self):
        #背景精灵
        self.bg1 = Backgroud("./image/078.jpg")
        self.bg2 = Backgroud("./image/078.jpg")
        self.bg2.rect.y = -SCREEN_RECT.height

        #创建精灵组
        self.back_goup = pygame.sprite.Group(self.bg1, self.bg2)

        #敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        #英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def start_game(self):
        print("游戏开始")

        while True:

            #刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            #监听
            self.__event_handler()
            #碰撞检测
            self.__check_collide()
            #更新，绘制精灵组
            self.__update_sprites()
            #更新显示
            pygame.display.update()


    def  __event_handler(self):
        #监听类
        global FIRECOOL

        for event in pygame.event.get():
            #判断退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                #创建敌机精灵
                enemy = Enemy()
                #添加到精灵组
                self.enemy_group.add(enemy)
            elif event.type == CREATE_HERO_COOL:
                FIRECOOL = True

        #英雄精灵组控制
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_w]:
            if keys_pressed[pygame.K_a]:
                self.hero_group.update(-HERO_SPEED, -HERO_SPEED)
            elif keys_pressed[pygame.K_d]:
                self.hero_group.update(HERO_SPEED, -HERO_SPEED)
            else:
                self.hero_group.update(0,-HERO_SPEED)
        elif keys_pressed[pygame.K_s]:
            if keys_pressed[pygame.K_a]:
                self.hero_group.update(-HERO_SPEED, HERO_SPEED)
            elif keys_pressed[pygame.K_d]:
                self.hero_group.update(HERO_SPEED, HERO_SPEED)
            else:
                self.hero_group.update(0,HERO_SPEED)
        elif keys_pressed[pygame.K_a]:
            if keys_pressed[pygame.K_w]:
                self.hero_group.update(-HERO_SPEED, -HERO_SPEED)
            elif keys_pressed[pygame.K_s]:
                self.hero_group.update(-HERO_SPEED, HERO_SPEED)
            else:
                self.hero_group.update(-HERO_SPEED,0)
        elif keys_pressed[pygame.K_d]:
            if keys_pressed[pygame.K_w]:
                self.hero_group.update(HERO_SPEED, -HERO_SPEED)
            elif keys_pressed[pygame.K_s]:
                self.hero_group.update(HERO_SPEED, HERO_SPEED)
            else:
                self.hero_group.update(HERO_SPEED,0)

        #英雄子弹控制
        if keys_pressed[pygame.K_j]:
            if FIRECOOL == True:
                print('射出子弹')
                self.hero.fire()
                FIRECOOL = False
            else:
                pass


    def __check_collide(self):
        pygame.sprite.groupcollide(hero_bullte_group,self.enemy_group,True,True)
        #判断敌机是否撞毁英雄
        enemies = pygame.sprite.groupcollide(self.hero_group , self.enemy_group , False,False)
        #判断是否与英雄发生碰撞
        if len(enemies) > 0 :
            self.hero.kill()
            self.__game_over()


    def __update_sprites(self):
        self.back_goup.update()
        self.back_goup.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        hero_bullte_group.update()
        hero_bullte_group.draw(self.screen)

    #声明静态方法
    @staticmethod
    def __game_over():
        print("你死了,游戏结束")
        pygame.quit()
        exit()

if __name__ == '__main__':
    game = PlaneGame()
    game.start_game()
