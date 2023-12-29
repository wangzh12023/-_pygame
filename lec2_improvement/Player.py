# -*- coding:utf-8 -*-

from Settings import *
import pygame


class Player(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load(GamePath.cai)
        self.image = pygame.transform.scale(self.image, (PlayerSettings.playerWidth//2, PlayerSettings.playerHeight//2))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = PlayerSettings.playerSpeed
        
        #新增方向属性
        self.direction=-1
    def update(self, keys, scene):
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= self.speed
        elif keys[pygame.K_s] and self.rect.bottom < WindowSettings.height:
            self.rect.y += self.speed
        elif keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= self.speed

        elif keys[pygame.K_d] and self.rect.right < WindowSettings.width:
            self.rect.x += self.speed
        
        if keys[pygame.K_j] and self.speed < 15:
            self.speed+=2
        if keys[pygame.K_k] and self.speed > 1:
            self.speed-=1
            
        if keys[pygame.K_b]:
            if self.direction==-1:
                self.image=pygame.transform.scale(pygame.image.load(GamePath.cai), (PlayerSettings.playerWidth*2, PlayerSettings.playerHeight*2))
            elif self.direction==1:
                self.image=pygame.transform.flip(
                           pygame.transform.scale(
                           pygame.image.load(GamePath.cai), (PlayerSettings.playerWidth*2,PlayerSettings.playerHeight*2)), True, False)
        if keys[pygame.K_n]:
            if self.direction==-1:
                self.image=pygame.transform.scale(pygame.image.load(GamePath.cai), (PlayerSettings.playerWidth/2, PlayerSettings.playerHeight/2))
            elif self.direction==1:
                self.image=pygame.transform.flip(
                           pygame.transform.scale(
                           pygame.image.load(GamePath.cai), (PlayerSettings.playerWidth/2,PlayerSettings.playerHeight/2)), True, False)
        #判断方向并改变
        if self.direction==-1 and keys[pygame.K_d]:
            self.image=pygame.transform.flip(self.image, True, False)
            self.direction=1
        if self.direction==1 and keys[pygame.K_a]:
            self.image=pygame.transform.flip(self.image, True, False)
            self.direction=-1


        
        

    def fix_to_middle(self, dx, dy):
        self.rect.x -= dx
        self.rect.y -= dy
