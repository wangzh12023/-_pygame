# -*- coding:utf-8 -*-

import pygame

from typing import *
from Settings import *

class DialogBox:
    def __init__(self, window, 
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        self.window = window
        #设置字体参数
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)
        #设置背景
        self.bg = pygame.Surface((DialogSettings.boxWidth,
            DialogSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)
        #设置状态
        self.open=False
    #根据所给信息更新
    def set_npc(self,npc):
        self.npc=npc
        self.npc.reset_talkCD("Talk")
        self.npc_image=pygame.transform.scale(npc.talk_image(),(DialogSettings.npcWidth,DialogSettings.npcHeight))
        self.dialogs=npc.dialog
        self.dialog_index=0
        self.open=True
    def update(self):
        #如果可以说话,则检测是否按下按键，如有则更新
        if self.npc.can_talk():
            keys=pygame.key.get_pressed()
            if any(keys):
                if self.dialog_index<len(self.dialogs)-1:
                    self.dialog_index+=1
                else:
                    self.open=False
                    pygame.event.post(pygame.event.Event(GameEvent.EVENT_END_DIALOG))
                self.npc.reset_talkCD("Talk")
    
    def draw(self):
        self.window.blit(self.bg, (DialogSettings.boxStartX,
            DialogSettings.boxStartY))
        self.window.blit(self.npc_image, (DialogSettings.npcCoordX,
            DialogSettings.npcCoordY))
        
        offset = 0
        for text in self.dialogs[self.dialog_index]:
            self.window.blit(self.font.render(text,
                True, self.fontColor),
                (DialogSettings.textStartX, DialogSettings.textStartY + offset))
            offset += DialogSettings.textVerticalDist
        

class ShoppingBox:
    def __init__(self, window,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        self.window = window
        #设置字体参数
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)
        #设置背景
        self.bg = pygame.Surface((DialogSettings.boxWidth,
            DialogSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)
        #设置状态
        self.state="Close"
        #设置初始指向商品的ID
        self.selectedID=0
        ##### Your Code Here ↑ #####
    
    def set_npc(self,npc,player):
        self.npc=npc
        self.npc_image=pygame.transform.scale(npc.talk_image(),(DialogSettings.npcWidth,DialogSettings.npcHeight))
        self.npc.reset_talkCD("Talk")
        
        self.player=player
        
        self.dialogs=npc.dialog
        self.dialog_index=0
        
        self.items=npc.items
        self.selectedID=0
        self.state="Talking"
    def update(self):
        #如果可以说话,则检测是否按下按键，如有则更新
        if self.npc.can_talk():
            keys=pygame.key.get_pressed()
            if self.state=="Shopping":
                if keys[pygame.K_w]:
                    self.selectedID = max(0, 
                        self.selectedID - 1)
                    self.npc.reset_talkCD("Select")
                elif keys[pygame.K_s]:
                    self.selectedID = min(4, 
                        self.selectedID + 1)
                    self.npc.reset_talkCD("Select")
                elif keys[pygame.K_RETURN]:
                    if self.selectedID == 4:
                        pygame.event.post(pygame.event.Event(GameEvent.EVENT_END_SHOP))
                        self.state="Close"
                        self.npc.reset_talkCD("Select")
                    else:
                        self.buy() 
                        self.npc.reset_talkCD("Talk")
            if self.state=="Talking":
                keys=pygame.key.get_pressed()
                if any(keys):
                    if self.dialog_index<len(self.dialogs)-1:
                        self.dialog_index+=1
                    else:
                        self.state="Shopping"
                    self.npc.reset_talkCD("Select")
    def buy(self):
        ##### Your Code Here ↓ #####
        if self.selectedID == 0:
            self.player.attr_update(addCoins = -15, addAttack = 1)
        elif self.selectedID == 1:
            self.player.attr_update(addCoins = -15, addDefence = 1)
        elif self.selectedID == 2:
            self.player.attr_update(addCoins = -15, addHP = 1)
        elif self.selectedID == 3:
            self.player.attr_update(addHP = -5)
        ##### Your Code Here ↑ #####

    def draw(self):
        if self.state=="Talking":
            self.window.blit(self.bg, (DialogSettings.boxStartX,
            DialogSettings.boxStartY))
            self.window.blit(self.npc_image, (DialogSettings.npcCoordX,
                DialogSettings.npcCoordY))
            
            offset = 0
            for text in self.dialogs[self.dialog_index]:
                self.window.blit(self.font.render(text,
                    True, self.fontColor),
                    (DialogSettings.textStartX, DialogSettings.textStartY + offset))
                offset += DialogSettings.textVerticalDist
        if self.state=="Shopping":
            self.window.blit(self.bg, 
            (ShopSettings.boxStartX, ShopSettings.boxStartY))
            self.window.blit(self.npc_image,
                (DialogSettings.npcCoordX, DialogSettings.npcCoordY))
            
            offset = 0
            for id, item in enumerate(list(self.items.keys())):
                if id == self.selectedID:
                    text = '-->' + item + ' ' + self.items[item]
                else:
                    text = '      ' + item + ' ' + self.items[item]
                self.window.blit(self.font.render(text, True, self.fontColor),
                    (ShopSettings.textStartX, ShopSettings.textStartY + offset))
                offset += DialogSettings.textVerticalDist

            
            texts = ["Coins: " + str(self.player.money),
                    "HP: " + str(self.player.HP),
                    "Attack: " + str(self.player.attack),
                    "Defence: " + str(self.player.defence)]
        
            offset = 0
            for text in texts:
                self.window.blit(self.font.render(text, True, self.fontColor),
                    (ShopSettings.textStartX + ShopSettings.boxWidth * 3 / 4, ShopSettings.textStartY + offset))
                offset += DialogSettings.textVerticalDist