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
        self.window=window
        #设置镜头位置
        
        #设置偏移量
        self.dx=0
        self.dy=0
        #生成传送门
        self.portals=pygame.sprite.Group()
        #生成NPC
        self.npcs=pygame.sprite.Group()
        #生成怪物
        self.monsters=pygame.sprite.Group()
        self.obstacles=pygame.sprite.Group()
    def get_width(self):
        return int(WindowSettings.width * WindowSettings.outdoorScale)
    def get_height(self):
        return int(WindowSettings.height * WindowSettings.outdoorScale)
    def update_camera(self, player):
        
        self.dx=self.dy=0
        if player.rect.x > WindowSettings.width / 4 * 3:
            self.cameraX += player.speed
            if self.cameraX < self.get_width() - WindowSettings.width:
                self.dx=-player.speed
            else:
                self.dx=(self.cameraX - player.speed)-(self.get_width() - WindowSettings.width)
                self.cameraX = self.get_width() - WindowSettings.width
        elif player.rect.x < WindowSettings.width / 4:
            self.cameraX -= player.speed
            if self.cameraX > 0:
                self.dx=player.speed
            else:
                self.dx=self.cameraX+player.speed
                self.cameraX = 0
        if player.rect.y > WindowSettings.height / 4 * 3:
            self.cameraY += player.speed
            if self.cameraY < self.get_height() - WindowSettings.height:
                self.dy=-player.speed
            else:
                self.dy=(self.cameraY-player.speed)-(self.get_height() - WindowSettings.height)
                self.cameraY = self.get_height() - WindowSettings.height
        elif player.rect.y < WindowSettings.height / 4:
            self.cameraY -= player.speed
            if self.cameraY > 0:
                self.dy=player.speed
            else:
                self.dy=self.cameraY+player.speed
                self.cameraY = 0
    def render(self, player):
       #渲染地图
        # for i in range(SceneSettings.tileXnum):
        #     for j in range(SceneSettings.tileYnum):
        #         self.window.blit(self.map[i][j],(SceneSettings.tileWidth*i-self.cameraX,SceneSettings.tileHeight*j-self.cameraY))
        self.render_map()
        #渲染主人公
        player.draw(self.window,self.dx,self.dy)
        #渲染传送门
        for portal in self.portals.sprites():
            portal.draw(self.window,self.dx,self.dy)
        #渲染障碍物
        for obstacle in self.obstacles.sprites():
            obstacle.draw(self.window,self.dx,self.dy)
        #渲染NPC
        for npc in self.npcs.sprites():
            npc.draw(self.window,self.dx,self.dy)
        # #渲染怪物
        # for monster in self.monsters.sprites():
        #     monster.draw(self.window,self.dx,self.dy)
    def render_map(self):
        self.window.blit(self.bg,(-self.cameraX,-self.cameraY))
class StartCG():
    def __init__(self, window):
        self.window=window
        #导入背景图
        self.bg=pygame.image.load(GamePath.white_bg)
        self.bg=pygame.transform.scale(self.bg,(WindowSettings.width,WindowSettings.height))

        self.cg=pygame.image.load(GamePath.cg)
        self.cg=pygame.transform.scale(self.cg,(WindowSettings.width,WindowSettings.height))
        self.cg.set_alpha(0)
    def render(self, time):
        self.window.blit(self.bg,(0,0))
        #从14-19秒透明度变低
        if 14<time<=15:
            self.cg.set_alpha(int(255*(time-14)))
        #19-20秒透明度变高
        if 19<time<20:
            self.cg.set_alpha(int(255*(20-time)))
        self.window.blit(self.cg,(0,0))

class StartMenu():
    def __init__(self, window):
        self.window=window
        
        #导入背景图
        self.bg=pygame.image.load(GamePath.menu)
        self.bg=pygame.transform.scale(self.bg,(WindowSettings.width,WindowSettings.height))
        #设置按键提示
        self.text=pygame.image.load(GamePath.menutext)

    def render(self, time):
        self.window.blit(self.bg,(0,0))
        self.text.set_alpha(int(255*abs(1-(time%2))))
        self.window.blit(self.text,(WindowSettings.width//3,WindowSettings.height//4*3))

class CityScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.cameraX=320
        self.cameraY=0
        self.gen_CITY()

    def gen_CITY(self):
        self.bg=pygame.image.load(GamePath.city_bg)

        self.portals.add(Portal(-160,200,SceneType.WILD,"Water"))
        self.portals.add(Portal(1140,200,SceneType.WILD,"Grass"))
        self.portals.add(Portal(480,600,SceneType.WILD,"Fire"))
        
        self.obstacles =Maps.gen_city_obstacle()
        
        self.npcs.add(DialogNPC(680,280,"Caroline",[["喂，犯人，","休息得够久了吧？","快去干活!"]]))
        self.npcs.add(DialogNPC(560,280,"Justine",[["Hello","2024"],["I'm fine","Tkx"]]))

        # self.npcs.add(ShopNPC(100,500,"Jack",[["Have a look"]],{"Attack +1": "Coin -15", "Defence +1": "Coin -15",
        #      "HP +1": "Coin -15", "???": "HP -5", "Exit": ""}))
class WildScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.cameraX=640
        self.cameraY=360
        self.gen_WILD()
        #self.gen_monsters()


    def gen_WILD(self):

        self.bg=pygame.image.load(GamePath.wild_bg)
        
        self.obstacles=Maps.gen_wild_obstacle(self.cameraX,self.cameraY)

        self.portals.add(Portal(SceneSettings.tileXnum//3//2*SceneSettings.tileWidth-self.cameraX,
                                SceneSettings.tileYnum//3*SceneSettings.tileHeight-self.cameraY,
                                SceneType.BOSS,"WILD"))
        self.portals.add(Portal(1200,600,SceneType.CITY,"WILD"))


    def gen_monsters(self, num = 10):
        for i in range(num):
            x=randint(0,SceneSettings.tileXnum-1)
            y=randint(0,SceneSettings.tileYnum-1)
            self.monsters.add(Monster(SceneSettings.tileWidth * x, SceneSettings.tileHeight * y))

class BossScene(Scene):
    def __init__(self, window):
        super().__init__(window=window)
        self.cameraX=320
        self.cameraY=0
        self.gen_BOSS()

    def gen_BOSS(self):
        
        self.bg=pygame.image.load(GamePath.boss_bg)
        
        self.portals.add(Portal(PortalSettings.coordX2,PortalSettings.coordY2,SceneType.CITY,"BOSS"))
        
        #self.obstacles=Maps.gen_boss_obstacle()