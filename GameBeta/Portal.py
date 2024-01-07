# -*- coding:utf-8 -*-

from Settings import *

import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self, x, y, GOTO:SceneType,attribute):
        super().__init__()
        if attribute=="Water":
            self.image=pygame.image.load(GamePath.portal_water)
            self.image=pygame.transform.scale(self.image,(PortalSettings.width,PortalSettings.height))
        if attribute=="Grass":
            self.image=pygame.image.load(GamePath.portal_grass)
            self.image=pygame.transform.scale(self.image,(PortalSettings.width,PortalSettings.height))
        if attribute=="Fire":
            self.image=pygame.image.load(GamePath.portal_fire)
            self.image=pygame.transform.scale(self.image,(PortalSettings.width,PortalSettings.height))
        if attribute=="WILD" and GOTO==SceneType.BOSS:
            self.image=pygame.image.load(GamePath.bossdoor)
            self.image=pygame.transform.scale(self.image,(SceneSettings.tileWidth,SceneSettings.tileHeight))
        if attribute=="WILD" and GOTO==SceneType.CITY:
            self.image=pygame.image.load(GamePath.portal_grass)
            self.image=pygame.transform.scale(self.image,(80,120))
        if attribute=="BOSS" and GOTO==SceneType.CITY:
            self.image=pygame.image.load(GamePath.portal_grass)
            self.image=pygame.transform.scale(self.image,(PortalSettings.width,PortalSettings.height))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        #设置目的地
        self.GOTO=GOTO

    def draw(self, window, dx=0, dy=0):
  
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)

