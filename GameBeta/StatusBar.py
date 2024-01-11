import pygame
from typing import *
from Settings import *

class StatusBar:
    def __init__(self, MaxHP,HP,attack,defence,money,
                 fontSize_hp: int = StatusBarSettings.Hpsize,
                 fontSize_resource: int = StatusBarSettings.ResourceSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255)):
        #设置字体参数
        self.font_path=GamePath.font
        self.fontColor = fontColor
        
        self.fontSize_hp= fontSize_hp
        self.font_hp= pygame.font.Font(self.font_path, self.fontSize_hp)


        self.fontSize_resource= fontSize_resource
        self.font_resource= pygame.font.Font(self.font_path, self.fontSize_resource)
        
        #设置图像
        self.image=pygame.transform.scale(pygame.image.load(GamePath.statusbar),
                                       (StatusBarSettings.BarWidth,StatusBarSettings.BarHeight))
        self.scale=pygame.transform.scale(pygame.image.load(GamePath.hpscale),
                                       (StatusBarSettings.ScaleWidth,StatusBarSettings.ScaleHeight))
        self.HP=HP
        self.attack=attack
        self.defence=defence
        self.money=money
        #设置状态40,13
    #根据所给信息更新
    def update(self,MaxHP,HP,attack,defence,money):
        self.MaxHP=MaxHP
        self.HP=HP
        self.attack=attack
        self.defence=defence
        self.money=money
        self.scale=pygame.transform.scale(self.scale,
                            (int(self.HP/self.MaxHP*StatusBarSettings.ScaleWidth)
                                ,StatusBarSettings.ScaleHeight))

    def draw(self,window):
        window.blit(self.image, (0,0))
        window.blit(self.font_hp.render(str(self.HP),
            True, self.fontColor),
            (20,20))
        window.blit(self.font_resource.render(str(self.attack),
            True, self.fontColor),
            (60,60))
        window.blit(self.font_resource.render(str(self.defence),
            True, self.fontColor),
            (150,60))
        window.blit(self.font_resource.render(str(self.money),
            True, self.fontColor),
            (230,60))
        window.blit(self.scale,(40,13))
class BossHPScale:
    def __init__(self,MaxHP,HP):
        self.MaxHP=MaxHP
        self.HP=HP
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.boss_scale_bg),
                                       (StatusBarSettings.BossScaleBgWidth,StatusBarSettings.BossScaleBgHeight))
        self.scale=pygame.transform.scale(pygame.image.load(GamePath.hpscale),
                                       (StatusBarSettings.BossScaleWidth,StatusBarSettings.BossScaleHeight))
    def update(self,HP):
        self.HP=HP
    def draw(self,window):
        window.blit(self.bg,(256,634))
        self.scale=pygame.transform.scale(self.scale,
                                    (int(self.HP/self.MaxHP*StatusBarSettings.BossScaleWidth)
                                        ,StatusBarSettings.BossScaleHeight))
        window.blit(self.scale,(350,650))