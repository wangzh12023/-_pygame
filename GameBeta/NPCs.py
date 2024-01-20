import pygame
from Settings import *
from Attributes import *
import random
from StatusBar import *

class NPC(pygame.sprite.Sprite, Collidable):
    def __init__(self,image_path,image_path_talk,x, y, name,dialog):
        # Initialize father classes
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
        self.image=pygame.transform.scale(pygame.image.load(image_path),
                                        (NPCSettings.npcWidth,NPCSettings.npcHeight))
        self.image_talk=pygame.image.load(image_path_talk)
        #设置名字
        self.name=name
        #记录初始位置
        self.initialPosition=x
        #设置方向
        self.direction=DirectionType.RIGHT
        #设置速度
        self.speed=NPCSettings.npcSpeed
        #设置对话
        self.dialog=dialog
        #设置对话cd
        self.talkcd=0
    #重置对话冷却时间
    def reset_talkCD(self,cdtype):
        if cdtype==CDType.LONG:
            self.talkcd = NPCSettings.talkCD 
        if cdtype==CDType.SHORT:
            self.talkcd = NPCSettings.SelectCD
        if cdtype==CDType.MEDIUM:
            self.talkcd = NPCSettings.shopCD
    #检测能否对话
    def can_talk(self):
        return self.talkcd <= 0
    #渲染
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
    def talk_image(self):
        return pygame.transform.scale(self.image_talk,
                                        (DialogSettings.npcWidth,DialogSettings.npcHeight))
class DialogNPC(NPC):
    def __init__(self,image_path,image_path_talk, x, y, name,dialog):
        super().__init__(image_path,image_path_talk,x, y, name,dialog)
        
        #设置坐标
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.talking=False
    def update(self,cameraX,cameraY):
        ##### Your Code Here ↓ #####
        # if not self.talking:
        #     if self.direction==DirectionType.RIGHT:
        #         self.rect.x += self.speed 
        #     else:
        #         self.rect.x -= self.speed
        #     #如果超出移动范围，转向
        #     if abs(cameraX + self.rect.x -self.initialPosition) > 50:
        #         #翻转图片
        #         self.image = pygame.transform.flip(self.image, True, False)
        #         # 反转方向
        #         if self.direction ==  DirectionType.RIGHT:
        #             self.direction=DirectionType.LEFT
        #         else:
        #             self.direction=DirectionType.RIGHT
        #更新冷却
        if not self.can_talk():
            self.talkcd -= 1
class ShopNPC(NPC):
    def __init__(self,image_path,image_path_talk, x, y, name, dialog,items):
        super().__init__(image_path,image_path_talk,x, y, name,dialog)
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.items=items
        self.shopping=False
    
    def update(self, cameraX,cameraY):
        ##### Your Code Here ↓ #####
        # if not self.shopping:
        #     if self.direction==DirectionType.RIGHT:
        #         self.rect.x += self.speed 
        #     else:
        #         self.rect.x -= self.speed
        #     #如果超出移动范围，转向
        #     if abs(cameraX + self.rect.x -self.initialPosition) > 50:
        #         #翻转图片
        #         self.image = pygame.transform.flip(self.image, True, False)
        #         # 反转方向
        #         if self.direction ==  DirectionType.RIGHT:
        #             self.direction=DirectionType.LEFT
        #         else:
        #             self.direction=DirectionType.RIGHT
        #更新冷却
        if not self.can_talk():
            self.talkcd -= 1
        ##### Your Code Here ↑ #####
    

class Monster(pygame.sprite.Sprite):
    def __init__(self,image_path,x, y,killedBOSSnum,HP = 10, Attack = 3, Defence = 1, Money = 15,Speed=2):
        super().__init__()
        self.images=[pygame.transform.scale(
        pygame.image.load(img),(NPCSettings.npcWidth,NPCSettings.npcHeight)) 
        for img in image_path]

        self.image_index=0
        self.image=self.images[self.image_index]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        self.money=Money*(killedBOSSnum+1)
        self.HP=HP*(killedBOSSnum+1)
        self.attack=Attack*(killedBOSSnum+1)
        self.defence=Defence*(killedBOSSnum+1)
        self.speed=Speed*(killedBOSSnum+1)
    
        self.dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.direindex = random.randint(0, 3)

        if self.direindex==2:
            self.direction=DirectionType.LEFT
            self.images=[pygame.transform.flip(img,True,False) for img in self.images]
        else:
            self.direction=DirectionType.RIGHT

        self.collide=Collidable()
        self.check = False
        self.dx=0
        self.dy=0
    def update(self):
        self.image_index=(self.image_index+1)%len(self.images)
        self.image=self.images[self.image_index]
        self.dx, self.dy = self.dire[self.direindex][0]*self.speed,self.dire[self.direindex][1]*self.speed
        self.rect = self.rect.move(self.dx, self.dy)
        
    def fix(self,cameraX,cameraY):
        if self.collide.is_colliding() or self.over_range(cameraX,cameraY):
            self.direindex = random.randint(0, 3)
            if self.direction ==DirectionType.RIGHT and self.direindex==2:
                self.direction=DirectionType.LEFT
                self.images=[pygame.transform.flip(img,True,False) for img in self.images]
            if self.direction ==DirectionType.LEFT and self.direindex==0:
                self.direction=DirectionType.RIGHT
                self.images=[pygame.transform.flip(img,True,False) for img in self.images]
            self.rect = self.rect.move(-self.dx,-self.dy)

    def over_range(self,cameraX,cameraY):
        #计算实际位置
        real_X=self.rect.x+cameraX
        real_Y=self.rect.y+cameraY
        if real_X<0 or real_Y<0 or real_X>=1880 or real_Y>=1040:
            return True
        return False
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)

class Boss_show(Monster):
    def __init__(self,image_path,x, y,killedBOSSnum,HP = 10, Attack = 3, Defence = 1, Money = 15):
        super().__init__(image_path,x,y,killedBOSSnum)
        self.images=[pygame.transform.scale(
        img,(NPCSettings.npcWidth*3,NPCSettings.npcHeight*3)) 
        for img in self.images]
class Boss(pygame.sprite.Sprite):
    def __init__(self,image_path,x, y,killedBOSSnum,HP = 50, Attack = 5, Defence = 2, Money = 100):
        super().__init__()

        self.images=[[pygame.transform.scale(
            pygame.image.load(img),(BossSettings.bossWidth,BossSettings.bossHeight)) 
            for img in image_path[index]] for index in range(4)]
        
        self.image_index=2
        self.index=0
        self.image=self.images[self.image_index][self.index]
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        self.money=Money*(killedBOSSnum+1)
        self.MaxHP=HP*(killedBOSSnum+1)
        self.HP=HP*(killedBOSSnum+1)
        self.attack=Attack*(killedBOSSnum+1)
        self.defence=Defence*(killedBOSSnum+1)

        self.scale=BossHPScale(self.MaxHP,self.HP)
        self.dir=DirectionType.LEFT
        self.speed=BossSettings.bossSpeed*(killedBOSSnum+1)

        self.width=BossSettings.bossWidth
        self.height=BossSettings.bossHeight

    def boss_try_move(self, player_x, player_y):
        dis_x=player_x-self.rect.x-self.width//2
        dis_y=player_y-self.rect.y-self.height//2
        if abs(dis_x) < abs(dis_y) :
            if dis_y > 0:
                self.dir=DirectionType.DOWN
                self.rect.y += self.speed
            else:
                self.dir=DirectionType.UP
                self.rect.y -= self.speed
        if abs(dis_y) <= abs(dis_x) :  #abs(dis_x)+abs(dis_y) >  self.width
            if dis_x > 0:
                self.dir=DirectionType.RIGHT
                self.rect.x += self.speed
            else:
                self.dir=DirectionType.LEFT
                self.rect.x -= self.speed

        if self.dir == DirectionType.DOWN:
            self.image_index=0
        if self.dir == DirectionType.RIGHT:
            self.image_index=2
        if self.dir == DirectionType.UP:
            self.image_index=3
        if self.dir == DirectionType.LEFT:
            self.image_index=1
        self.index=(self.index+1) % 4
        self.image=self.images[self.image_index][self.index]

    def update(self,x,y):
        self.boss_try_move(x,y)
        self.scale.update(self.HP)
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        self.scale.draw(window)

class BossAttack(pygame.sprite.Sprite):
    def __init__(self,x,y,direction,speed):
        super().__init__()
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
