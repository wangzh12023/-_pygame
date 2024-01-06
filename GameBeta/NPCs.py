# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class NPC(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y, name,dialog):
        # Initialize father classes
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        #设置名字
        self.name=name
        #记录初始位置
        self.initialPosition=x
        #设置方向
        self.direction=DirectionType.RIGHT
        #设置速度
        self.speed=NPCSettings.npcSpeed
        #设置对话
        self.dialog=dialog
        #设置对话cd
        self.talkcd=0
    #重置对话冷却时间
    def reset_talkCD(self,cdtype):
        ##### Your Code Here ↓ #####
        if cdtype=="Talk":
            self.talkcd = NPCSettings.talkCD 
        if cdtype=="Select":
            self.talkcd = NPCSettings.SelectCD
        ##### Your Code Here ↑ #####
    #检测能否对话
    def can_talk(self):
        return self.talkcd <= 0
    #渲染
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
    def talk_image(self):
        if self.direction==DirectionType.RIGHT:
            return self.image
        else:
            return pygame.transform.flip(self.image, True, False)   

class DialogNPC(NPC):
    def __init__(self, x, y, name,dialog):
        super().__init__(x, y, name,dialog)
        self.image=pygame.transform.scale(pygame.image.load(GamePath.npc),
                                          (NPCSettings.npcWidth,NPCSettings.npcHeight))
        #设置坐标
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.talking=False
    def update(self,cameraX,cameraY):
        ##### Your Code Here ↓ #####
        if not self.talking:
            if self.direction==DirectionType.RIGHT:
                self.rect.x += self.speed 
            else:
                self.rect.x -= self.speed
            #如果超出移动范围，转向
            if abs(cameraX + self.rect.x -self.initialPosition) > 50:
                #翻转图片
                self.image = pygame.transform.flip(self.image, True, False)
                # 反转方向
                if self.direction ==  DirectionType.RIGHT:
                    self.direction=DirectionType.LEFT
                else:
                    self.direction=DirectionType.RIGHT
        #更新冷却
        if not self.can_talk():
            self.talkcd -= 1
class ShopNPC(NPC):
    def __init__(self, x, y, name, dialog,items):
        super().__init__(x, y, name,dialog)
        self.image=pygame.transform.scale(pygame.image.load(GamePath.trader),
                                          (NPCSettings.npcWidth,NPCSettings.npcHeight))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.items=items
        self.shopping=False
    
    def update(self, cameraX,cameraY):
        ##### Your Code Here ↓ #####
        if not self.shopping:
            if self.direction==DirectionType.RIGHT:
                self.rect.x += self.speed 
            else:
                self.rect.x -= self.speed
            #如果超出移动范围，转向
            if abs(cameraX + self.rect.x -self.initialPosition) > 50:
                #翻转图片
                self.image = pygame.transform.flip(self.image, True, False)
                # 反转方向
                if self.direction ==  DirectionType.RIGHT:
                    self.direction=DirectionType.LEFT
                else:
                    self.direction=DirectionType.RIGHT
        #更新冷却
        if not self.can_talk():
            self.talkcd -= 1
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
