# -*- coding:utf-8 -*-

import pygame
import Maps
from random import randint

from enum import Enum
from Settings import *
from NPCs import *
from PopUpBox import *
from Portal import *
from BgmPlayer import *

class Scene():
    def __init__(self, window):
        ##### Your Code Here ↓ #####
        self.window=window
        self.cameraX=0
        self.cameraY=0
        self.dx=0
        self.dy=0
        self.portals=pygame.sprite.Group()
        self.npcs=pygame.sprite.Group()
        ##### Your Code Here ↑ #####

        

    def trigger_dialog(self, npc):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_dialog(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_battle(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def trigger_shop(self, npc, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def end_shop(self):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_camera(self, player):
        ##### Your Code Here ↓ #####
        self.dx=self.dy=0
        if player.rect.x > WindowSettings.width / 4 * 3:
            self.cameraX += player.speed
            if self.cameraX < WindowSettings.width * WindowSettings.outdoorScale - WindowSettings.width:
                self.dx=-player.speed
            else:
                self.cameraX = WindowSettings.width * WindowSettings.outdoorScale - WindowSettings.width
        elif player.rect.x < WindowSettings.width / 4:
            self.cameraX -= player.speed
            if self.cameraX > 0:
                self.dx=player.speed
            else:
                self.cameraX = 0
        if player.rect.y > WindowSettings.height / 4 * 3:
            self.cameraY += player.speed
            if self.cameraY < WindowSettings.height * WindowSettings.outdoorScale - WindowSettings.height:
                self.dy=-player.speed
            else:
                self.cameraY = WindowSettings.height * WindowSettings.outdoorScale - WindowSettings.height
        elif player.rect.y < WindowSettings.height / 4:
            self.cameraY -= player.speed
            if self.cameraY > 0:
                self.dy=player.speed
            else:
                self.cameraY = 0
        ##### Your Code Here ↑ #####

    def render(self, player):
        ##### Your Code Here ↓ #####
        for i in range(SceneSettings.tileXnum):
            for j in range(SceneSettings.tileYnum):
                self.window.blit(self.map[i][j],(SceneSettings.tileWidth*i-self.cameraX,SceneSettings.tileHeight*j-self.cameraY))
        player.draw(self.window,self.dx,self.dy)
        for attack in player.player_attack_wave:
            attack.draw(self.window,self.dx,self.dy)
        for portal in self.portals.sprites():
            portal.draw(self.window,self.dx,self.dy)
        for obstacle in self.obstacles.sprites():
            obstacle.draw(self.window,self.dx,self.dy)
        for npc in self.npcs.sprites():
            npc.draw(self.window,self.dx,self.dy)
        ##### Your Code Here ↑ #####


class StartMenu():
    def __init__(self, window):
        ##### Your Code Here ↓ #####
        self.window=window
        
        #导入背景图
        self.bg=pygame.image.load(GamePath.menu)
        self.bg=pygame.transform.scale(self.bg,(WindowSettings.width,WindowSettings.height))
        #设置按键提示
        self.text=pygame.image.load(GamePath.menutext)
        ##### Your Code Here ↑ #####

    def render(self, time):
        ##### Your Code Here ↓ #####
        self.window.blit(self.bg,(0,0))
        self.text.set_alpha(int(128*abs(1000-(time%2000))/1000))
        self.window.blit(self.text,(WindowSettings.width//3,WindowSettings.height//4*3))
        ##### Your Code Here ↑ #####

class CityScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        self.gen_CITY()
        
        ##### Your Code Here ↑ #####

    def gen_CITY(self):
        ##### Your Code Here ↓ #####
        self.map=Maps.gen_city_map()
        self.portals.add(Portal(PortalSettings.coordX,PortalSettings.coordY,SceneType.WILD))
        self.obstacles =Maps.gen_city_obstacle()
        self.npcs.add(DialogNPC(100,100,"John",1))
        #self.ShopNpcs.add()
        ##### Your Code Here ↑ #####

class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        self.gen_WILD()
        
        ##### Your Code Here ↑ #####

    def gen_WILD(self):
        ##### Your Code Here ↓ #####
        self.map=Maps.gen_wild_map()
        self.obstacles=Maps.gen_wild_obstacle()
        self.portals.add(Portal(PortalSettings.coordX,PortalSettings.coordY,SceneType.BOSS))
        self.portals.add(Portal(PortalSettings.coordX2,PortalSettings.coordY2,SceneType.CITY))
        ##### Your Code Here ↑ #####

    def gen_monsters(self, num = 10):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

class BossScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        ##### Your Code Here ↓ #####
        self.gen_BOSS()
        ##### Your Code Here ↑ #####

    # Overwrite Scene's function
    def trigger_battle(self, player):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def gen_BOSS(self):
        ##### Your Code Here ↓ #####
        self.map=Maps.gen_boss_map()
        self.portals.add(Portal(PortalSettings.coordX2,PortalSettings.coordY2,SceneType.WILD))
        self.obstacles=Maps.gen_boss_obstacle()
        ##### Your Code Here ↑ #####