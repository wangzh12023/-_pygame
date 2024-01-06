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
        self.npc.reset_talkCD()
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
                self.npc.reset_talkCD()
    
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
    def __init__(self, window, npc, player,
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def buy(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def draw(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
