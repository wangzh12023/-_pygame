import pygame
from Settings import *
from Player import *
class Guideboard:
    def __init__(self,window):
        self.window=window
        self.images=[pygame.transform.scale(pygame.image.load(img),(GuideboardSettings.guideWidth,GuideboardSettings.guideHeight)) for img in GamePath.guide]
        #提高透明度
        for img in self.images:
            img.set_alpha(100)
        #设置状态
        self.state=0
        #设置上次转换状态的时间记录器
        self.last_time=-1
        #设置转换cd
        self.cooldown=GuideboardSettings.change_CD
    def draw(self):
        self.window.blit(self.images[self.state],(300,0))
    #更新提示板状态
    def update(self,current_time):
        keys=pygame.key.get_pressed()
        if current_time - self.last_time > self.cooldown:
            if keys[pygame.K_q]:
                self.state=(self.state+1)%len(self.images)
            self.last_time=current_time

        

        
    