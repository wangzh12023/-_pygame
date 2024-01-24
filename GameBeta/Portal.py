from Settings import *
import pygame

class Portal(pygame.sprite.Sprite):
    def __init__(self,image_path,x, y, GOTO:SceneType):
        super().__init__()
        
        if GOTO==SceneType.CITY:
            self.image=pygame.image.load(image_path)
            self.image=pygame.transform.scale(self.image,(PortalSettings.cityWidth,PortalSettings.cityHeight))

        if GOTO==SceneType.WILD_FIRE or GOTO==SceneType.WILD_GRASS or GOTO==SceneType.WILD_WATER:
            self.image=pygame.image.load(image_path)
            self.image=pygame.transform.scale(self.image,(PortalSettings.width,PortalSettings.height))
            
        if GOTO==SceneType.BOSS_FIRE or GOTO==SceneType.BOSS_GRASS or GOTO==SceneType.BOSS_WATER:
            self.image=pygame.image.load(image_path)
            self.image=pygame.transform.scale(self.image,(SceneSettings.tileWidth,SceneSettings.tileHeight))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        #设置目的地
        self.GOTO=GOTO

    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)

