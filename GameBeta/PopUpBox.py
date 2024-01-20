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
        self.fontPath=GamePath.font
        self.font = pygame.font.Font(self.fontPath, self.fontSize)
        #设置背景
        self.bg = pygame.image.load(GamePath.dialogBox)
        #设置状态
        self.open=False
    #根据所给信息更新
    def set_npc(self,npc):
        self.npc=npc
        self.npc.reset_talk_cd(CdType.SHORT)
        self.npc_image=pygame.transform.scale(npc.talk_image(),(DialogSettings.npcWidth,DialogSettings.npcHeight))
        self.dialogs=npc.dialog
        self.dialogIndex=0
        self.open=True
    def update(self):
        #如果可以说话,则检测是否按下按键，如有则更新
        if self.npc.can_talk():
            keys=pygame.key.get_pressed()
            if any(keys):
                if self.dialogIndex<len(self.dialogs)-1:
                    self.dialogIndex+=1
                else:
                    self.open=False
                    pygame.event.post(pygame.event.Event(GameEvent.EVENT_END_DIALOG))
                self.npc.reset_talk_cd(CdType.LONG)
    
    def draw(self):
        self.window.blit(self.bg, (DialogSettings.boxStartX,
            DialogSettings.boxStartY))
        self.window.blit(self.npc_image, (DialogSettings.npcCoordX,
            DialogSettings.npcCoordY))
        
        self.window.blit(self.font.render(self.npc.name,
                True, self.fontColor),
                (DialogSettings.nameStartX,DialogSettings.nameStartY))
        
        offset = 0
        for text in self.dialogs[self.dialogIndex]:
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
        self.fontPath=GamePath.font
        self.font = pygame.font.Font(self.fontPath, self.fontSize)
        #设置背景
        self.bgTalk = pygame.image.load(GamePath.dialogBox)
        self.bgShop = pygame.transform.scale(pygame.image.load(GamePath.shopBox),
                                          (ShopSettings.boxWidth,ShopSettings.boxHeight))
        #设置状态
        self.state=ShopType.CLOSE
        #设置初始指向商品的ID
        self.selectedID=0
        ##### Your Code Here ↑ #####
    
    def set_npc(self,npc,player):
        self.npc=npc
        self.npcImage=npc.talk_image()
        self.npc.reset_talk_cd(CdType.LONG)
        
        self.player=player
        
        self.dialogs=npc.dialog
        self.dialogIndex=0
        
        self.items=npc.items
        self.selectedID=0
        self.state=ShopType.TALK
    def update(self):
        #如果可以说话,则检测是否按下按键，如有则更新
        if self.npc.can_talk():
            keys=pygame.key.get_pressed()
            if self.state==ShopType.SHOP:
                if keys[pygame.K_w]:
                    self.selectedID = max(0, 
                        self.selectedID - 1)
                    self.npc.reset_talk_cd(CdType.SHORT)
                elif keys[pygame.K_s]:
                    self.selectedID = min(4, 
                        self.selectedID + 1)
                    self.npc.reset_talk_cd(CdType.SHORT)
                elif keys[pygame.K_RETURN]:
                    if self.selectedID == 4:
                        pygame.event.post(pygame.event.Event(GameEvent.EVENT_END_SHOP))
                        self.state=ShopType.CLOSE
                        self.npc.reset_talk_cd(CdType.LONG)
                    else:
                        self.buy() 
                        self.npc.reset_talk_cd(CdType.MEDIUM)
            if self.state==ShopType.TALK:
                keys=pygame.key.get_pressed()
                if any(keys):
                    if self.dialogIndex<len(self.dialogs)-1:
                        self.dialogIndex+=1
                    else:
                        self.state=ShopType.SHOP
                    self.npc.reset_talk_cd(CdType.SHORT)
    def buy(self):
        if self.selectedID == 0:
            if self.player.money>=15:
                self.player.attr_update(addCoins = -15, addAttack = 1)

        elif self.selectedID == 1:
            if self.player.money>=15:
                self.player.attr_update(addCoins = -15, addDefence = 1)

        elif self.selectedID == 2:
            if self.player.money>=15:
                self.player.attr_update(addCoins = -15, addMaxHp = 1, addHp =1 )

        elif self.selectedID == 3:
            if self.player.maxHp>5:
                self.player.attr_update(addCoins = 50, addMaxHp = -5, addHp = -5)

    def draw(self):
        if self.state==ShopType.TALK:
            self.window.blit(self.bgTalk, (DialogSettings.boxStartX,
            DialogSettings.boxStartY))
            self.window.blit(self.npcImage, (DialogSettings.npcCoordX,
                DialogSettings.npcCoordY))
            self.window.blit(self.font.render(self.npc.name,
                True, self.fontColor),
                (DialogSettings.nameStartX,DialogSettings.nameStartY))
            
            offset = 0
            for text in self.dialogs[self.dialogIndex]:
                self.window.blit(self.font.render(text,
                    True, self.fontColor),
                    (DialogSettings.textStartX, DialogSettings.textStartY + offset))
                offset += DialogSettings.textVerticalDist
        if self.state==ShopType.SHOP:
            self.window.blit(self.bgShop, 
            (ShopSettings.boxStartX, ShopSettings.boxStartY))
            self.window.blit(self.npcImage,
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