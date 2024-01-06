# -*- coding:utf-8 -*-

import pygame

from typing import *
from Settings import *

class DialogBox:
    def __init__(self, window, 
                 fontSize: int = DialogSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), 
                 bgColor: Tuple[int, int, int, int] = (0, 0, 0, 150)):
        ##### Your Code Here ↓ #####
        self.window = window
        self.fontSize = fontSize
        self.fontColor = fontColor
        self.font = pygame.font.Font(None, self.fontSize)

        self.bg = pygame.Surface((DialogSettings.boxWidth,
            DialogSettings.boxHeight), pygame.SRCALPHA)
        self.bg.fill(bgColor)
        ##### Your Code Here ↑ #####
    def update(self,npc_image,texts):
        self.npc_image=pygame.transform.scale(npc_image,(DialogSettings.npcWidth,DialogSettings.npcHeight))
        self.texts=texts
    def draw(self):
        ##### Your Code Here ↓ #####
        self.window.blit(self.bg, (DialogSettings.boxStartX,
            DialogSettings.boxStartY))
        self.window.blit(self.npc_image, (DialogSettings.npcCoordX,
            DialogSettings.npcCoordY))
        
        offset = 0
        for text in self.texts:
            self.window.blit(self.font.render(text,
                True, self.fontColor),
                (DialogSettings.textStartX, DialogSettings.textStartY + offset))
            offset += DialogSettings.textVerticalDist
        ##### Your Code Here ↑ #####
        

class BattleBox:
    def __init__(self, window, player, monster, fontSize: int = BattleSettings.textSize, 
                 fontColor: Tuple[int, int, int] = (255, 255, 255), bgColor: Tuple[int, int, int, int] = (0, 0, 0, 200)) :
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


    def draw(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

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
