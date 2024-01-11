import pygame
from Settings import *
from Attributes import *
from StatusBar import *
class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        #读取图片
        self.images=[[pygame.transform.scale(
            pygame.image.load(img),(PlayerSettings.playerWidth,PlayerSettings.playerHeight)) 
            for img in GamePath.player[index]] for index in range(len(GamePath.player))]
        #设置初始图片
        self.index=0
        self.image_index=2
        self.image=self.images[self.image_index][self.index]
        #设置方向
        self.direction=DirectionType.RIGHT
        #设置坐标
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        #设置移动速度
        self.speed=PlayerSettings.playerSpeed
        #设置移动量
        self.dx=0
        self.dy=0
        #设置状态
        self.money=PlayerSettings.playerMoney
        self.MaxHP=PlayerSettings.playerHP
        self.HP=PlayerSettings.playerHP
        self.attack=PlayerSettings.playerAttack
        self.defence=PlayerSettings.playerDefence
        #创建状态面板
        self.status=StatusBar(self.MaxHP,self.HP,self.attack,self.defence,self.money)
        #设置对话状态
        self.talking=False
        self.shopping=False
        #创建枪
        self.gun=Gun()
        #设置子弹冷却时间和移动速度
        self.attack_cooldown=PlayerSettings.playerAttackCooldown
        self.attack_speed = PlayerSettings.playerAttackSpeed
        self.attack_range = PlayerSettings.playerAttackRange
        #创建子弹组
        self.attacks=pygame.sprite.Group()
        #记录上次射击时间
        self.last_attack_time = 0
        #创建碰撞检测器
        self.collide=Collidable()
        self.collide_cd=PlayerSettings.collideCD
    def reset_collideCD(self):
        self.collide_cd = PlayerSettings.collideCD
    def can_collide(self):
        return self.collide_cd <= 0
    #更新状态
    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        self.money+=addCoins
        self.MaxHP+=addHP
        self.attack+=addAttack
        self.defence+=addDefence
    #回到画面中心
    def reset_pos(self,state):
        if state==GameState.GAME_PLAY_CITY:
            self.rect.topleft=(PlayerSettings.Citycoodx,PlayerSettings.Citycoody)
        if state==GameState.GAME_PLAY_WILD_GRASS or state==GameState.GAME_PLAY_WILD_WATER or state==GameState.GAME_PLAY_WILD_FIRE:
            self.rect.topleft=(PlayerSettings.Wildcoodx,PlayerSettings.Wildcoody)##44,24
        if state==GameState.GAME_PLAY_BOSS_GRASS or state==GameState.GAME_PLAY_BOSS_WATER or state==GameState.GAME_PLAY_BOSS_FIRE:
            self.rect.topleft=(PlayerSettings.Citycoodx,PlayerSettings.Citycoody)
    def update(self,time):
        #如果正在对话则则不尝试更新
        self.status.update(self.MaxHP,self.HP,self.attack,self.defence,self.money)
        if not self.talking and not self.shopping:
            #尝试移动
            self.try_move()
            #尝试攻击
            self.try_attack(time)
            #尝试更新子弹速度
            self.try_change_attack_speed()
        if not self.can_collide():
            self.collide_cd-=1
            
        
    #尝试移动
    def try_move(self):
        keys=pygame.key.get_pressed()
        #初始化移动量
        self.dx=0
        self.dy=0
        if keys[pygame.K_w] and self.rect.top > 0 + self.speed:
            self.dy -= self.speed
            self.image_index=3
        if keys[pygame.K_s] and self.rect.bottom< WindowSettings.height:
            self.dy += self.speed
            self.image_index=0
        if keys[pygame.K_a] and self.rect.left > 0 + self.speed:
            self.dx -= self.speed
            self.image_index=1
        if keys[pygame.K_d] and self.rect.right < WindowSettings.width - self.speed:
            self.dx += self.speed
            self.image_index=2
        #更新坐标
        self.rect=self.rect.move(self.dx,self.dy)
        #如果发生移动，更换人物图像
        if self.dx!=0 or self.dy!=0:
            self.index=(self.index+1) % 4
            self.image=self.images[self.image_index][self.index]
    def try_attack(self,current_time):
        # 玩家攻击
        player_pos = [self.rect.x,self.rect.y]
        keys=pygame.key.get_pressed()
        if keys[pygame.K_j]:
            if current_time - self.last_attack_time > self.attack_cooldown:
                self.attacks.add(Attack(player_pos[0], player_pos[1]+PlayerSettings.playerHeight//3,DirectionType.LEFT,self.attack_speed))
                self.last_attack_time = current_time
                self.gun.update(DirectionType.LEFT)
        if keys[pygame.K_k]:
            if current_time - self.last_attack_time > self.attack_cooldown:
                #如果可以攻击,生成子弹
                self.attacks.add(Attack(player_pos[0] , player_pos[1]+PlayerSettings.playerHeight//3,DirectionType.RIGHT,self.attack_speed))
                self.last_attack_time = current_time
                #更新枪朝向
                self.gun.update(DirectionType.RIGHT)
        if keys[pygame.K_i]:
            if current_time - self.last_attack_time > self.attack_cooldown:
                self.attacks.add(Attack(player_pos[0], player_pos[1],DirectionType.UP,self.attack_speed))
                self.last_attack_time = current_time
                self.gun.update(DirectionType.UP)
        if keys[pygame.K_m]:
            if current_time - self.last_attack_time > self.attack_cooldown:
                self.attacks.add(Attack(player_pos[0], player_pos[1],DirectionType.DOWN,self.attack_speed))
                self.last_attack_time = current_time
                self.gun.update(DirectionType.DOWN)
    #更新子弹速度
    def try_change_attack_speed(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_o]:
            self.attack_speed+=5
            self.attack_cooldown=self.attack_cooldown*0.8
        if keys[pygame.K_p] and self.attack_speed > 5 :
            self.attack_speed-=5
            self.attack_cooldown=self.attack_cooldown/0.8
    #渲染角色
    def draw(self, window,dx=0,dy=0):
        #根据镜头偏移量更改坐标
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        #渲染枪
        self.gun.draw(window,self.rect)
        #渲染子弹
        for attack in self.attacks:
            attack.draw(window,dx,dy)
        #渲染状态面板
        self.status.draw(window)
class Gun:
    def __init__(self):
        #加载图片
        self.images=[pygame.transform.scale(pygame.image.load(img),(PlayerSettings.playerGunWidth,PlayerSettings.playerGunHeight)) for img in GamePath.gun]    
        #设置初始方向
        self.direction=DirectionType.RIGHT           #0123为上下左右
    def update(self,direction):
        #更新方向
        self.direction=direction
    #渲染枪
    def draw(self,window,rect):
        if self.direction==DirectionType.UP:
            window.blit(self.images[self.direction.value],(rect.x + PlayerSettings.playerWidth * 0.25,rect.y))
        if self.direction==DirectionType.DOWN:
            window.blit(self.images[self.direction.value],(rect.x + PlayerSettings.playerWidth * 0.25,rect.y + PlayerSettings.playerHeight * 0.6))
        if self.direction==DirectionType.RIGHT:
            window.blit(self.images[self.direction.value],(rect.x + PlayerSettings.playerWidth * 0.25,rect.y + PlayerSettings.playerHeight * 0.4))
        if self.direction==DirectionType.LEFT:
            window.blit(self.images[self.direction.value],(rect.x + PlayerSettings.playerWidth * 0.25,rect.y + PlayerSettings.playerHeight * 0.33))

class Attack(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,speed):
        super().__init__()
        #读取图片
        self.images=[pygame.transform.scale(pygame.image.load(img),(PlayerSettings.playerAttackRange,PlayerSettings.playerAttackRange)) for img in GamePath.attack]
        #设置子弹方向
        self.direction=direction
        self.image=self.images[direction.value]
        #设置坐标
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        #设置子弹速度
        self.attack_speed=speed
        #设置碰撞检测
        self.collide=Collidable()
    def update(self):
        #设置偏移量
        dx=dy=0
        if self.direction==DirectionType.LEFT:
            dx -= self.attack_speed
        if self.direction==DirectionType.RIGHT:
            dx += self.attack_speed
        if self.direction==DirectionType.UP:
            dy -= self.attack_speed
        if self.direction==DirectionType.DOWN: 
            dy += self.attack_speed
        #更新坐标
        self.rect=self.rect.move(dx,dy)
    #检测是否超过地图边界
    def over_range(self,cameraX,cameraY):
        #计算实际位置
        real_X=self.rect.x+cameraX
        real_Y=self.rect.y+cameraY
        if real_X<0 or real_Y<0 or real_X>WindowSettings.width * WindowSettings.outdoorScale or real_Y>WindowSettings.height * WindowSettings.outdoorScale:
            return True
        return False
    #渲染子弹
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
