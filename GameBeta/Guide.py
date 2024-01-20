import pygame
from Settings import *
from Player import *
class GuideBoard:
    def __init__(self,window):
        self.window=window
        self.images=[pygame.transform.scale(pygame.image.load(img),(GuideboardSettings.guideWidth,GuideboardSettings.guideHeight)) for img in GamePath.guide]
        #提高透明度
        for img in self.images:
            img.set_alpha(100)
        #设置状态
        self.state=0
        #设置上次转换状态的时间记录器
        self.lastTime=-1
        #设置转换cd
        self.cooldown=GuideboardSettings.changeCd
    def draw(self):
        self.window.blit(self.images[self.state],(GuideboardSettings.startCoorX,GuideboardSettings.startCoorY))
    #更新提示板状态
    def update(self,currentTime):
        keys=pygame.key.get_pressed()
        if currentTime - self.lastTime > self.cooldown:
            if keys[pygame.K_q]:
                self.state=(self.state+1)%len(self.images)
            self.lastTime=currentTime

        

        
    