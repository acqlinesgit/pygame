from cProfile import run
from cmath import rect
from tkinter import W
from turtle import width
import pygame

#尺寸大小設定
FPS = 60
WIDTH = 600
HEIGH = 500
SIZE = (WIDTH,HEIGH)

#標題設定
TITLE = 'practice'

#顏色設定
WHITE = (255,255,255)
GREEN = (0,255,0)

#遊戲初始化和創建視窗

pygame.init()
pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


#建立遊戲類別
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        # self.rect.x = 200
        # self.rect.y = 200
        self.rect.center = (WIDTH/2, HEIGH/2)

    def update(self):
        self.rect.x += 2

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)



#遊戲迴圈
running = True
while running:
    #取得輸入
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
             
    #更新遊戲
    all_sprites.update()

    #畫面顯示
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()



pygame.quit()