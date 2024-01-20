import pygame
from typing import *
from Settings import *

class StatusBar:
    def __init__(self, maxHp,hp,attack,defence,money,
                 fontSizeHp: int = StatusBarSettings.hpSize,
                 fontSizeResource: int = StatusBarSettings.resourceSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255)):
        #设置字体参数
        self.fontPath=GamePath.font
        self.fontColor = fontColor
        
        self.fontSizeHp= fontSizeHp
        self.fontHp= pygame.font.Font(self.fontPath, self.fontSizeHp)


        self.fontSizeResource= fontSizeResource
        self.fontResource= pygame.font.Font(self.fontPath, self.fontSizeResource)
        
        #设置图像
        self.image=pygame.transform.scale(pygame.image.load(GamePath.statusBar),
                                       (StatusBarSettings.barWidth,StatusBarSettings.barHeight))
        self.scale=pygame.transform.scale(pygame.image.load(GamePath.hpScale),
                                       (StatusBarSettings.scaleWidth,StatusBarSettings.scaleHeight))
        self.hp=hp
        self.attack=attack
        self.defence=defence
        self.money=money
        #设置状态40,13
    #根据所给信息更新
    def update(self,maxHp,hp,attack,defence,money):
        self.maxHp=maxHp
        self.hp=hp
        self.attack=attack
        self.defence=defence
        self.money=money
        self.scale=pygame.transform.scale(self.scale,
                            (int(self.hp/self.maxHp*StatusBarSettings.scaleWidth)
                                ,StatusBarSettings.scaleHeight))

    def draw(self,window):
        window.blit(self.image, (0,0))
        window.blit(self.fontHp.render(str(self.hp),
            True, self.fontColor),
            (StatusBarSettings.hpCoodX,StatusBarSettings.hpCoodY))
        window.blit(self.fontResource.render(str(self.attack),
            True, self.fontColor),
            (StatusBarSettings.attackCoodX,StatusBarSettings.attackCoodY))
        window.blit(self.fontResource.render(str(self.defence),
            True, self.fontColor),
            (StatusBarSettings.defenceCoodX,StatusBarSettings.defenceCoodY))
        window.blit(self.fontResource.render(str(self.money),
            True, self.fontColor),
            (StatusBarSettings.moneyCoodX,StatusBarSettings.moneyCoodY))
        window.blit(self.scale,(StatusBarSettings.scaleCoodX,StatusBarSettings.scaleCoodY))
class BossHpScale:
    def __init__(self,maxHp,hp):
        self.maxHp=maxHp
        self.hp=hp
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.bossScaleBg),
                                       (StatusBarSettings.bossScaleBgWidth,StatusBarSettings.bossScaleBgHeight))
        self.scale=pygame.transform.scale(pygame.image.load(GamePath.hpScale),
                                       (StatusBarSettings.bossScaleWidth,StatusBarSettings.bossScaleHeight))
    def update(self,hp):
        self.hp=hp
    def draw(self,window):
        window.blit(self.bg,(StatusBarSettings.bossHpScaleBgCoodX,StatusBarSettings.bossHpScaleBgCoody))
        self.scale=pygame.transform.scale(self.scale,
                                    (int(self.hp/self.maxHp*StatusBarSettings.bossScaleWidth)
                                        ,StatusBarSettings.bossScaleHeight))
        window.blit(self.scale,(StatusBarSettings.bossHpScaleBgCoodX,StatusBarSettings.bossHpScaleBgCoody))