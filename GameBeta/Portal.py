# -*- coding:utf-8 -*-

from Settings import *

import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, GOTO:SceneType):
        super().__init__()

        self.image=pygame.image.load(GamePath.portal)
        self.image=pygame.transform.scale(self.image,(PortalSettings.width,PortalSettings.height))

        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        #设置目的地
        self.GOTO=GOTO

    def draw(self, window, dx=0, dy=0):
  
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)

