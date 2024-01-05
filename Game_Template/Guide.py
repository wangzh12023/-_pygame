import pygame
from Settings import *
class Guideboard:
    def __init__(self,window):
        self.window=window
        self.images=[pygame.transform.scale(pygame.image.load(img),(GuideboardSettings.guideWidth,GuideboardSettings.guideHeight)) for img in GamePath.guide]
        for img in self.images:
            img.set_alpha(100)
        self.state=0
        self.last_time=-1
        self.cooldown=GuideboardSettings.change_CD
    def draw(self):
        self.window.blit(self.images[self.state],(0,0))
    def update(self):
        current_time = pygame.time.get_ticks() / 1000.0
        if current_time - self.last_time > self.cooldown:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_q]:
                self.state=(self.state+1)%len(self.images)
            self.last_time=current_time