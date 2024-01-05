# -*- coding:utf-8 -*-

import sys
import pygame

from Player import Player
from Scene import *
from Settings import *
from PopUpBox import *
from Guide import *

class GameManager:
    def __init__(self):
        
        ##### Your Code Here ↓ #####
        #初始游戏状态
        self.state=GameState.MAIN_MENU
        #设置窗口和时钟
        self.window=pygame.display.set_mode((WindowSettings.width,WindowSettings.height))
        pygame.display.set_caption(WindowSettings.name)
        self.clock=pygame.time.Clock()
        #设置碰撞检测器
        #self.collide=Collidable()

        self.scene=StartMenu(self.window) 

        self.player=Player(WindowSettings.width//2,WindowSettings.height//2)  

        self.guideboard=Guideboard(self.window)

        ##### Your Code Here ↑ #####

    def game_reset(self):

        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Necessary game components here ↓
    def tick(self, fps):
        ##### Your Code Here ↓ #####
        self.clock.tick(fps)
        ##### Your Code Here ↑ #####

    def get_time(self):
        ##### Your Code Here ↓ #####
        return pygame.time.get_ticks()
        ##### Your Code Here ↑ #####

    # Scene-related update functions here ↓
    def flush_scene(self, GOTO:SceneType):
        ##### Your Code Here ↓ #####
        if GOTO==SceneType.CITY:
            self.scene=CityScene(self.window)
            self.player.reset_pos()
        if GOTO==SceneType.WILD:
            self.scene=WildScene(self.window)
            self.player.reset_pos()
        if GOTO==SceneType.BOSS:
            self.scene=BossScene(self.window)
            self.player.reset_pos()
        self.player.player_attack_wave.empty()
        ##### Your Code Here ↑ #####

    def update(self):
        ##### Your Code Here ↓ #####
        self.tick(30)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.QUIT()
                sys.exit()
            if event.type==GameEvent.EVENT_SWITCH_CITY:
                self.state=GameState.GAME_PLAY_CITY
                self.flush_scene(SceneType.CITY) 
            if event.type==GameEvent.EVENT_SWITCH_WILD:
                self.state=GameState.GAME_PLAY_WILD
                self.flush_scene(SceneType.WILD) 
            if event.type==GameEvent.EVENT_SWITCH_BOSS:
                self.state=GameState.GAME_PLAY_BOSS
                self.flush_scene(SceneType.BOSS) 
        if self.state==GameState.MAIN_MENU:
            self.update_main_menu()
        else:
            if self.state==GameState.GAME_PLAY_CITY:
                self.update_city()
            if self.state==GameState.GAME_PLAY_WILD:
                self.update_wild()
            if self.state==GameState.GAME_PLAY_BOSS:
                self.update_boss()
            self.player.attack()
            self.update_attack()
            self.guideboard.update()
        ##### Your Code Here ↑ #####

    def update_main_menu(self):
        ##### Your Code Here ↓ #####
        keys=pygame.key.get_pressed()
        if any(keys):
            pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH_CITY))
        ##### Your Code Here ↑ #####

    def update_city(self):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
            
        
        ##### Your Code Here ↑ #####

        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        self.player.try_move()
        self.update_collide(self.player)
        if self.player.collide.is_colliding():
            if self.player.collide.collidingWith["portal"]:
                if self.player.collide.collidingObject["portal"].GOTO==SceneType.WILD:
                    pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH_WILD))
            if self.player.collide.collidingWith["obstacle"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
            if self.player.collide.collidingWith["npc"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
            if self.player.collide.collidingWith["monster"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
        for attack in self.player.player_attack_wave:
            self.update_collide(attack)
            if attack.collide.is_colliding():
                attack.kill()
        self.scene.update_camera(self.player)
        ##### Your Code Here ↑ #####

    def update_wild(self):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        ##### Your Code Here ↑ #####
        
        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        self.player.try_move()
        self.update_collide(self.player)
        if self.player.collide.is_colliding():
            if self.player.collide.collidingWith["portal"]:
                if self.player.collide.collidingObject["portal"].GOTO==SceneType.CITY:
                    pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH_CITY))
                if self.player.collide.collidingObject["portal"].GOTO==SceneType.BOSS:
                    pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH_BOSS))
            if self.player.collide.collidingWith["obstacle"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
            if self.player.collide.collidingWith["npc"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
            if self.player.collide.collidingWith["monster"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
        #检测子弹碰撞
        for attack in self.player.player_attack_wave:
            self.update_collide(attack)
            if attack.collide.is_colliding():
                attack.kill()
        self.scene.update_camera(self.player)
        ##### Your Code Here ↑ #####

    def update_boss(self):
        # Deal with EventQueue First
        ##### Your Code Here ↓ #####
        ##### Your Code Here ↑ #####
        
        # Then deal with regular updates
        ##### Your Code Here ↓ #####
        self.player.try_move()
        self.update_collide(self.player)
        if self.player.collide.is_colliding():
            if self.player.collide.collidingWith["portal"]:
                if self.player.collide.collidingObject["portal"].GOTO==SceneType.WILD:
                    pygame.event.post(pygame.event.Event(GameEvent.EVENT_SWITCH_WILD))
            if self.player.collide.collidingWith["obstacle"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
            if self.player.collide.collidingWith["npc"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
            if self.player.collide.collidingWith["monster"]:
                self.player.rect=self.player.rect.move(-self.player.dx,-self.player.dy)
        for attack in self.player.player_attack_wave:
            self.update_collide(attack)
            if attack.collide.is_colliding():
                attack.kill()
        self.scene.update_camera(self.player)
        ##### Your Code Here ↑ #####
    def update_attack(self):
        for attack in self.player.player_attack_wave:
            attack.update()
            if attack.over_range(self.scene.cameraX,self.scene.cameraY):
                attack.kill()
    # Collision-relate update funtions here ↓
    def update_collide(self,object):
        # object -> Obstacles
        ##### Your Code Here ↓ #####
        if pygame.sprite.spritecollide(object,self.scene.obstacles,False,pygame.sprite.collide_mask):
            object.collide.collidingWith["obstacle"]=True
            for obstacle in self.scene.obstacles.sprites():
                if pygame.sprite.collide_rect(object,obstacle):
                    object.collide.collidingObject["obstacle"].append(obstacle)
        else:
            object.collide.collidingWith["obstacle"]=False
            object.collide.collidingObject["obstacle"]=[]
        ##### Your Code Here ↑ #####

        # object -> NPCs; if multiple NPCs collided, only first is accepted and dealt with.
        ##### Your Code Here ↓ #####
        if pygame.sprite.spritecollide(object,self.scene.npcs,False,pygame.sprite.collide_mask):
            object.collide.collidingWith["npc"]=True
            for npc in self.scene.npcs.sprites():
                if pygame.sprite.collide_rect(object,npc):
                    object.collide.collidingObject["npc"]=npc
                    break
        else:
            object.collide.collidingWith["npc"]=False
            object.collide.collidingObject["npc"]=None
        ##### Your Code Here ↑ #####

        # object -> Monsters
        ##### Your Code Here ↓ #####
        if pygame.sprite.spritecollide(object,self.scene.monsters,False,pygame.sprite.collide_mask):
            object.collide.collidingWith["monster"]=True
            for monster in self.scene.monsters.sprites():
                if pygame.sprite.collide_rect(object,monster):
                    object.collide.collidingObject["monster"]=monster
        else:
            object.collide.collidingWith["monster"]=False
            object.collide.collidingObject["monster"]=None
        ##### Your Code Here ↑ #####
        
        # object -> Portals
        ##### Your Code Here ↓ #####
        if pygame.sprite.spritecollide(object,self.scene.portals,False,pygame.sprite.collide_mask):
            object.collide.collidingWith["portal"]=True
            for portal in self.scene.portals.sprites():
                if pygame.sprite.collide_rect(object,portal):
                    object.collide.collidingObject["portal"]=portal
        else:
            object.collide.collidingWith["portal"]=False
            object.collide.collidingObject["portal"]=None
        ##### Your Code Here ↑ #####
        
        # object -> Boss
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def update_NPCs(self):
        # This is not necessary. If you want to re-use your code you can realize this.
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    # Render-relate update functions here ↓
    def render(self):
        ##### Your Code Here ↓ #####
        if self.state==GameState.MAIN_MENU:
            self.render_main_menu()
        else:
            if self.state==GameState.GAME_PLAY_CITY:
                self.render_city()
            if self.state==GameState.GAME_PLAY_WILD:
                self.render_wild()
            if self.state==GameState.GAME_PLAY_BOSS:
                self.render_boss()
            self.guideboard.draw()
        ##### Your Code Here ↑ #####
    
    def render_main_menu(self):
        ##### Your Code Here ↓ #####
        self.scene.render(self.get_time())
        ##### Your Code Here ↑ #####
    
    def render_city(self):
        ##### Your Code Here ↓ #####
        self.scene.render(self.player)
        ##### Your Code Here ↑ #####

    def render_wild(self):
        ##### Your Code Here ↓ #####
        self.scene.render(self.player)
        ##### Your Code Here ↑ #####

    def render_boss(self):
        ##### Your Code Here ↓ #####
        self.scene.render(self.player)
        ##### Your Code Here ↑ #####


