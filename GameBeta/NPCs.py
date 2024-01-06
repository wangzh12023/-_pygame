# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class NPC(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y, name):
        # Initialize father classes
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        ##### Your Code Here ↓ #####
        self.name=name
        ##### Your Code Here ↑ #####


    def reset_talkCD(self):
        ##### Your Code Here ↓ #####
        self.talkcd = NPCSettings.talkCD 
        ##### Your Code Here ↑ #####
    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        ##### Your Code Here ↑ #####


class DialogNPC(NPC):
    def __init__(self, x, y, name,dialog):
        ##### Your Code Here ↓ #####
        super().__init__(x, y, name)
        self.image=pygame.image.load(GamePath.npc)
        self.image=pygame.transform.scale(self.image,(NPCSettings.npcWidth,NPCSettings.npcHeight))
        
        self.direction=1

        self.initialPosition=x

        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.speed=NPCSettings.npcSpeed
        self.dialog=dialog
        self.talking=False
        self.talkcd=0

        self.dialog_index=0
        ##### Your Code Here ↑ #####
    def can_talk(self):
        return self.talkcd <= 0
    def reset_talk(self,dialogbox):
        self.reset_talkCD()
        self.dialog_index=0
        dialogbox.update(self.talk_image(),self.dialog[self.dialog_index])
        self.dialog_index+=1
    #对话时的图像
    def talk_image(self):
        if self.direction==1:
            return self.image
        else:
            return pygame.transform.flip(self.image, True, False)
    def update(self,ticks,dialogbox):
        ##### Your Code Here ↓ #####
        if self.talking:
            if not self.can_talk():
                self.talkcd -= 1 
            else:
                keys=pygame.key.get_pressed()
                if any(keys):
                    if self.dialog_index<len(self.dialog):
                        dialogbox.update(self.talk_image(),self.dialog[self.dialog_index])
                        self.dialog_index+=1
                    else:
                        pygame.event.post(pygame.event.Event(GameEvent.EVENT_END_DIALOG))
                        self.talking=False
                    self.reset_talkCD()
        else:
            self.rect.x += self.speed * self.direction
            if abs(self.rect.x - self.initialPosition) > 50:
                self.direction *= -1  # 反转方向
                self.image = pygame.transform.flip(self.image, True, False)
            if not self.can_talk():
                self.talkcd -= 1
        
        
            
        ##### Your Code Here ↑ #####

class ShopNPC(NPC):
    def __init__(self, x, y, name, items, dialog):
        super().__init__(x, y, name)

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    
    def update(self, ticks):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, HP = 10, Attack = 3, Defence = 1, Money = 15):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        self.image=pygame.image.load(GamePath.monster)
        self.image=pygame.transform.scale(self.image,(NPCSettings.npcWidth,NPCSettings.npcHeight))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        ##### Your Code Here ↑ #####

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
