import sys,pygame
from pygame.locals import *

screen = pygame.display.set_mode((600,800))
paodan = pygame.image.load("./image/img_bullet.png")
rect = Rect(100,100,100,100)
paodan = paodan.subsurface(rect)

while True:
    for event in pygame.event.get():
        # 判断退出游戏
        if event.type == pygame.QUIT:
            sys.exit()
        screen.blit(paodan,(200,200))
    pygame.display.update()