# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)

        ##### Your Code Here ↓ #####
        self.images=[pygame.transform.scale(pygame.image.load(img),(PlayerSettings.playerWidth,PlayerSettings.playerHeight)) for img in GamePath.player]
        self.index=0
        self.image=self.images[self.index]
        
        self.dir=1

        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        self.speed=PlayerSettings.playerSpeed

        self.dx=0
        self.dy=0
        ##### Your Code Here ↑ #####
    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        ##### Your Code Here ↓ #####
        self.rect.topleft=(x,y)
        ##### Your Code Here ↑ #####

    def try_move(self):
        ##### Your Code Here ↓ #####
        keys=pygame.key.get_pressed()
        self.dx=0
        self.dy=0
        if keys[pygame.K_w] and self.rect.top > 0 :
            self.dy -= self.speed
        if keys[pygame.K_s] and self.rect.bottom< WindowSettings.height:
            self.dy += self.speed
        if keys[pygame.K_a] and self.rect.left> 0:
            self.dx -= self.speed
            if self.dir==1:
                self.images=[pygame.transform.flip(img,True,False) for img in self.images]
                self.dir=-1
        if keys[pygame.K_d] and self.rect.right< WindowSettings.width:
            self.dx += self.speed
            if self.dir==-1:
                self.images=[pygame.transform.flip(img,True,False) for img in self.images]
                self.dir=1
        self.rect=self.rect.move(self.dx,self.dy)
        if self.dx!=0 or self.dy!=0:
            self.index=(self.index+1)%len(self.images)
            self.image=self.images[self.index]
        ##### Your Code Here ↑ #####

    def update(self,width,height):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    def draw(self, window,dx=0,dy=0):
        ##### Your Code Here ↓ #####
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        ##### Your Code Here ↑ #####
