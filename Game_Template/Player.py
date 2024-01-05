import pygame
from Settings import *
from Attributes import *
class Player(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.images=[[pygame.transform.scale(
            pygame.image.load(img),(PlayerSettings.playerWidth,PlayerSettings.playerHeight)) 
            for img in GamePath.player[index]] for index in range(len(GamePath.player))]
        self.index=0
        self.list_index = 2
        self.image=self.images[self.list_index][self.index]
        self.width=PlayerSettings.playerWidth
        self.height=PlayerSettings.playerHeight
        self.dir= "right"
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.speed=PlayerSettings.playerSpeed
        self.dx=0
        self.dy=0
        self.attack_cooldown=PlayerSettings.playerAttackCooldown
        self.attack_speed = PlayerSettings.playerAttackSpeed
        self.player_attack_wave=pygame.sprite.Group()  
        self.attack_dir = None
        self.player_attack_range = PlayerSettings.playerAttackRange
        self.player_last_attack_time = 0
        self.gun = [pygame.transform.scale(pygame.image.load(img),(PlayerSettings.playerGunWidth,PlayerSettings.playerGunHeight)) for img in GamePath.gun]
        self.gun_index = 3
        self.gun_rect = self.image.get_rect()
        self.gun_rect.x=self.rect.x + self.width*0.25
        self.gun_rect.y=self.rect.y + self.height*0.33
        

    def attr_update(self, addCoins = 0, addHP = 0, addAttack = 0, addDefence = 0):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####

    def reset_pos(self, x=WindowSettings.width // 2, y=WindowSettings.height // 2):
        self.rect.topleft=(x,y)
    def try_move(self):
        ##### Your Code Here ↓ #####
        keys=pygame.key.get_pressed()
        self.dx=0
        self.dy=0
        if keys[pygame.K_w] and self.rect.top > 0 :
            self.dy -= self.speed
            self.dir = "up"
            self.list_index = 3
        if keys[pygame.K_s] and self.rect.bottom< WindowSettings.height:
            self.dy += self.speed
            self.dir = "down"
            self.list_index = 0
        if keys[pygame.K_a] and self.rect.left> 0:
            self.dx -= self.speed
            self.dir = "left"
            self.list_index = 1
        if keys[pygame.K_d] and self.rect.right< WindowSettings.width:
            self.dx += self.speed
            self.dir = "right"
            self.list_index = 2
        self.rect=self.rect.move(self.dx,self.dy)
        if self.dx!=0 or self.dy!=0:
            self.index=(self.index+1)%len(self.images)
            self.image=self.images[self.list_index][self.index]
    def update(self,width,height):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
    def draw(self, window,dx=0,dy=0):
        self.try_move()
        window.blit(self.image,self.rect)
        self.change_gun_dir()
        window.blit(self.gun[self.gun_index],self.gun_rect)
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
            self.attack_dir = "left"
            current_time = pygame.time.get_ticks() / 1000
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.add(Attack(player_pos[0], player_pos[1]+self.rect.height*0.4,0,self.attack_speed))
                self.player_last_attack_time = current_time
        if keys[pygame.K_k]:
            self.attack_dir = "right"
            current_time = pygame.time.get_ticks() / 1000
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.add(Attack(player_pos[0]+self.rect.width , player_pos[1]+self.rect.height * 0.35,1,self.attack_speed))
                self.player_last_attack_time = current_time
        if keys[pygame.K_i]:
            self.attack_dir = "up"
            current_time = pygame.time.get_ticks() / 1000
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.add(Attack(player_pos[0]+self.rect.width*0.55, player_pos[1],2,self.attack_speed))
                self.player_last_attack_time = current_time
        if keys[pygame.K_m]:
            self.attack_dir = "down"
            current_time = pygame.time.get_ticks() / 1000
            if current_time - self.player_last_attack_time > self.attack_cooldown:
                self.player_attack_wave.add(Attack(player_pos[0]+self.rect.width / 2, player_pos[1]+self.rect.height,3,self.attack_speed))
                self.player_last_attack_time = current_time

    def change_gun_dir(self):
        self.try_move()
        keys=pygame.key.get_pressed()
        if not keys[pygame.K_j] and not keys[pygame.K_k] and not keys[pygame.K_i] and not keys[pygame.K_m]:
            if self.dir == 'up' :
                self.gun_index =0
                self.gun_rect.x=self.rect.x + self.width*0.25
                self.gun_rect.y=self.rect.y 
            if self.dir == 'down':
                self.gun_index =1
                self.gun_rect.x=self.rect.x + self.width*0.25
                self.gun_rect.y=self.rect.y + self.height*0.6
            if self.dir == 'left':
                self.gun_index =2
                self.gun_rect.x=self.rect.x - self.width*0.1
                self.gun_rect.y=self.rect.y + self.height*0.4
            if self.dir == 'right':
                self.gun_index =3
                self.gun_rect.x=self.rect.x + self.width*0.25
                self.gun_rect.y=self.rect.y + self.height*0.33
        else:
            if self.attack_dir == 'up' :
                self.list_index = 3
                self.gun_index =0
                self.gun_rect.x=self.rect.x + self.width*0.25
                self.gun_rect.y=self.rect.y 
            if self.attack_dir == 'down':
                self.list_index = 0
                self.gun_index =1
                self.gun_rect.x=self.rect.x + self.width*0.25
                self.gun_rect.y=self.rect.y + self.height*0.6
            if self.attack_dir == 'left':
                self.list_index = 1
                self.gun_index =2
                self.gun_rect.x=self.rect.x - self.width*0.1
                self.gun_rect.y=self.rect.y + self.height*0.4
            if self.attack_dir == 'right':
                self.list_index = 2
                self.gun_index =3
                self.gun_rect.x=self.rect.x + self.width*0.25
                self.gun_rect.y=self.rect.y + self.height*0.33
        #     # 检查是否击中BOSS
        #     if (
        #         boss_pos[0] < attack[0] < boss_pos[0] + boss_size
        #         and boss_pos[1] < attack[1] < boss_pos[1] + boss_size
        #     ):
        #         boss_health -= player_attack
        #         player_attack_wave.remove(attack)


class Attack(pygame.sprite.Sprite):
    def __init__(self,x,y,index,speed):
        super().__init__()
        ##### Your Code Here ↓ #####
        self.images=[pygame.transform.scale(pygame.image.load(img),(PlayerSettings.playerAttackRange,PlayerSettings.playerAttackRange)) for img in GamePath.attack]
        self.index=index
        self.image=self.images[index]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.attack_speed=speed
        ##### Your Code Here ↑ #####
    def update(self):
        dx=dy=0
        if self.index==0:
            dx -= self.attack_speed
        if self.index==1:
            dx += self.attack_speed
        if self.index==2:
            dy -= self.attack_speed
        if self.index==3: 
            dy += self.attack_speed
        self.rect=self.rect.move(dx,dy)
    def over_range(self,cameraX,cameraY):
        real_X=self.rect.x+cameraX
        real_Y=self.rect.y+cameraY
        if real_X<0 or real_Y<0 or real_X>WindowSettings.width * WindowSettings.outdoorScale or real_Y>WindowSettings.height * WindowSettings.outdoorScale:
            return True
        return False
    def draw(self, window, dx=0, dy=0):
        ##### Your Code Here ↓ #####
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        ##### Your Code Here ↑ #####
        
