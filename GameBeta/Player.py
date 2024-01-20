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
        self.imageIndex=2
        self.image=self.images[self.imageIndex][self.index]
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
        self.maxHp=PlayerSettings.playerHp
        self.hp=PlayerSettings.playerHp
        self.attack=PlayerSettings.playerAttack
        self.defence=PlayerSettings.playerDefence
        #创建状态面板
        self.status=StatusBar(self.maxHp,self.hp,self.attack,self.defence,self.money)
        #设置对话状态
        self.talking=False
        self.shopping=False
        #创建枪
        self.gun=Gun()
        #设置子弹冷却时间和移动速度
        self.attackCooldown=PlayerSettings.playerAttackCooldown
        self.attackSpeed = PlayerSettings.playerAttackSpeed
        self.attackRange = PlayerSettings.playerAttackRange
        #创建子弹组
        self.attacks=pygame.sprite.Group()
        #记录上次射击时间
        self.lastAttackTime = 0
        #创建碰撞检测器
        self.collide=Collidable()
        self.collideCd=PlayerSettings.collideCd
    def reset_collide_cd(self):
        self.collideCd = PlayerSettings.collideCd
    def reset_hp(self):
        self.hp=self.maxHp
    def can_collide(self):
        return self.collideCd <= 0
    #更新状态
    def attr_update(self, addCoins = 0, addMaxHp = 0,addHp = 0,addAttack = 0, addDefence = 0):
        self.money+=addCoins
        self.maxHp+=addMaxHp
        self.hp+=addHp
        self.attack+=addAttack
        self.defence+=addDefence
    #回到画面中心
    def reset_pos(self,state):
        if state==GameState.GAME_PLAY_CITY:
            self.rect.topleft=(PlayerSettings.cityCoodx,PlayerSettings.cityCoody)
        if state==GameState.GAME_PLAY_WILD_GRASS or state==GameState.GAME_PLAY_WILD_WATER or state==GameState.GAME_PLAY_WILD_FIRE:
            self.rect.topleft=(PlayerSettings.wildCoodx,PlayerSettings.wildCoody)
        if state==GameState.GAME_PLAY_BOSS_GRASS or state==GameState.GAME_PLAY_BOSS_WATER or state==GameState.GAME_PLAY_BOSS_FIRE:
            self.rect.topleft=(PlayerSettings.bossCoodx,PlayerSettings.bossCoody)
    def update(self,time):
        #如果正在对话则则不尝试更新
        self.status.update(self.maxHp,self.hp,self.attack,self.defence,self.money)
        if not self.talking and not self.shopping:
            #尝试移动
            self.try_move()
            #尝试攻击
            self.try_attack(time)
            #尝试更新子弹速度
            #self.try_change_attack_speed()
        if not self.can_collide():
            self.collideCd-=1
            
        
    #尝试移动
    def try_move(self):
        keys=pygame.key.get_pressed()
        #初始化移动量
        self.dx=0
        self.dy=0
        if keys[pygame.K_w] and self.rect.top > 0 + self.speed:
            self.dy -= self.speed
            self.imageIndex=3
        if keys[pygame.K_s] and self.rect.bottom< WindowSettings.height:
            self.dy += self.speed
            self.imageIndex=0
        if keys[pygame.K_a] and self.rect.left > 0 + self.speed:
            self.dx -= self.speed
            self.imageIndex=1
        if keys[pygame.K_d] and self.rect.right < WindowSettings.width - self.speed:
            self.dx += self.speed
            self.imageIndex=2
        #更新坐标
        self.rect=self.rect.move(self.dx,self.dy)
        #如果发生移动，更换人物图像
        if self.dx!=0 or self.dy!=0:
            self.index=(self.index+1) % 4
            self.image=self.images[self.imageIndex][self.index]
    def try_attack(self,currentTime):
        # 玩家攻击
        playerPos = [self.rect.x,self.rect.y]
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if currentTime - self.lastAttackTime > self.attackCooldown:
                self.attacks.add(Attack(playerPos[0], playerPos[1]+PlayerSettings.playerHeight//3,DirectionType.LEFT,self.attackSpeed))
                self.lastAttackTime = currentTime
                self.gun.update(DirectionType.LEFT)
        if keys[pygame.K_RIGHT]:
            if currentTime - self.lastAttackTime > self.attackCooldown:
                #如果可以攻击,生成子弹
                self.attacks.add(Attack(playerPos[0] , playerPos[1]+PlayerSettings.playerHeight//3,DirectionType.RIGHT,self.attackSpeed))
                self.lastAttackTime = currentTime
                #更新枪朝向
                self.gun.update(DirectionType.RIGHT)
        if keys[pygame.K_UP]:
            if currentTime - self.lastAttackTime > self.attackCooldown:
                self.attacks.add(Attack(playerPos[0], playerPos[1],DirectionType.UP,self.attackSpeed))
                self.lastAttackTime = currentTime
                self.gun.update(DirectionType.UP)
        if keys[pygame.K_DOWN]:
            if currentTime - self.lastAttackTime > self.attackCooldown:
                self.attacks.add(Attack(playerPos[0], playerPos[1],DirectionType.DOWN,self.attackSpeed))
                self.lastAttackTime = currentTime
                self.gun.update(DirectionType.DOWN)
    #更新子弹速度
    def try_change_attack_speed(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_o]:
            self.attackSpeed+=5
            self.attackCooldown=self.attackCooldown*0.8
        if keys[pygame.K_p] and self.attackSpeed > 5 :
            self.attackSpeed-=5
            self.attackCooldown=self.attackCooldown/0.8
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
        self.attackSpeed=speed
        #设置碰撞检测
        self.collide=Collidable()
    def update(self):
        #设置偏移量
        dx=dy=0
        if self.direction==DirectionType.LEFT:
            dx -= self.attackSpeed
        if self.direction==DirectionType.RIGHT:
            dx += self.attackSpeed
        if self.direction==DirectionType.UP:
            dy -= self.attackSpeed
        if self.direction==DirectionType.DOWN: 
            dy += self.attackSpeed
        #更新坐标
        self.rect=self.rect.move(dx,dy)
    #检测是否超过地图边界
    def over_range(self,cameraX,cameraY):
        #计算实际位置
        realX=self.rect.x+cameraX
        realY=self.rect.y+cameraY
        if realX<0 or realY<0 or realX>WindowSettings.width * WindowSettings.outdoorScale or realY>WindowSettings.height * WindowSettings.outdoorScale:
            return True
        return False
    #渲染子弹
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
