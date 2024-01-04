# -*- coding:utf-8 -*-

import pygame

from Settings import *
from Attributes import *

class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        # Must initialize everything one by one here
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)

        ##### Your Code Here ↓ #####
        self.images=[pygame.transform.scale(pygame.image.load(img),(PlayerSettings.playerWidth,PlayerSettings.playerHeight)) for img in GamePath.player]
        self.index=0
        self.image=self.images[self.index]
        self.dir=1
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.speed=PlayerSettings.playerSpeed
        self.dx=0
        self.dy=0
        self.attack_cooldown=PlayerSettings.playerAttackCooldown
        self.attack_speed = PlayerSettings.playerAttackSpeed
        self.player_attack_wave = []
        self.player_attack_range = PlayerSettings.playerAttackRange
        self.player_last_attack_time = 0
        
        ##### Your Code Here ↑ #####
    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        ##### Your Code Here ↓ #####
        self.rect.topleft=(x,y)
        ##### Your Code Here ↑ #####

    def try_move(self):
        ##### Your Code Here ↓ #####
        keys=pygame.key.get_pressed()
        self.dx=0
        self.dy=0
        if keys[pygame.K_w] and self.rect.top > 0 :
            self.dy -= self.speed
        if keys[pygame.K_s] and self.rect.bottom< WindowSettings.height:
            self.dy += self.speed
        if keys[pygame.K_a] and self.rect.left> 0:
            self.dx -= self.speed
            if self.dir==1:
                self.images=[pygame.transform.flip(img,True,False) for img in self.images]
                self.dir=-1
        if keys[pygame.K_d] and self.rect.right< WindowSettings.width:
            self.dx += self.speed
            if self.dir==-1:
                self.images=[pygame.transform.flip(img,True,False) for img in self.images]
                self.dir=1
        self.rect=self.rect.move(self.dx,self.dy)
        if self.dx!=0 or self.dy!=0:
            self.index=(self.index+1)%len(self.images)
            self.image=self.images[self.index]
        ##### Your Code Here ↑ #####

    def update(self,width,height):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    def draw(self, window,dx=0,dy=0):
        ##### Your Code Here ↓ #####
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        ##### Your Code Here ↑ #####
    def change_attack_speed(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_o]:
            self.attack_speed+=5
        if keys[pygame.K_p] and self.attack_speed > 5 :
            self.attack_speed-=5
    def attack(self):
        self.change_attack_speed()
        # 玩家攻击
        player_pos = [self.rect.x,self.rect.y]
        keys=pygame.key.get_pressed()
        if keys[pygame.K_j]:
            current_time = pygame.time.get_ticks() / 1000
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.append([player_pos[0], player_pos[1]+self.rect.height / 2,1])
                self.player_last_attack_time = current_time

        if keys[pygame.K_k]:
            current_time = pygame.time.get_ticks() / 1000
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.append([player_pos[0]+self.rect.width , player_pos[1]+self.rect.height / 2,2])
                self.player_last_attack_time = current_time

        if keys[pygame.K_i]:
            current_time = pygame.time.get_ticks() / 1000.0
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.append([player_pos[0]+self.rect.width / 2, player_pos[1],3])
                self.player_last_attack_time = current_time

        if keys[pygame.K_m]:
            current_time = pygame.time.get_ticks() / 1000.0
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.append([player_pos[0]+self.rect.width / 2, player_pos[1]+self.rect.height,4])
                self.player_last_attack_time = current_time





        #     # 检查是否击中BOSS
        #     if (
        #         boss_pos[0] < attack[0] < boss_pos[0] + boss_size
        #         and boss_pos[1] < attack[1] < boss_pos[1] + boss_size
        #     ):
        #         boss_health -= player_attack
        #         player_attack_wave.remove(attack)