import pygame
from Settings import *
from Attributes import *
import random
class NPC(pygame.sprite.Sprite, Collidable):
    def __init__(self, x, y, name,dialog):
        # Initialize father classes
        pygame.sprite.Sprite.__init__(self)
        Collidable.__init__(self)
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
        ##### Your Code Here ↓ #####
        if cdtype=="Talk":
            self.talkcd = NPCSettings.talkCD 
        if cdtype=="Select":
            self.talkcd = NPCSettings.SelectCD
        ##### Your Code Here ↑ #####
    #检测能否对话
    def can_talk(self):
        return self.talkcd <= 0
    #渲染
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
    def talk_image(self):
        if self.direction==DirectionType.RIGHT:
            return self.image
        else:
            return pygame.transform.flip(self.image, True, False)   

class DialogNPC(NPC):
    def __init__(self, x, y, name,dialog):
        super().__init__(x, y, name,dialog)
        if name=="Caroline":
            self.image=pygame.transform.scale(pygame.image.load(GamePath.Caroline),
                                            (NPCSettings.npcWidth,NPCSettings.npcHeight))
        if name=="Justine":
            self.image=pygame.transform.scale(pygame.image.load(GamePath.Justine),
                                            (NPCSettings.npcWidth,NPCSettings.npcHeight))
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
    def __init__(self, x, y, name, dialog,items):
        super().__init__(x, y, name,dialog)
        self.image=pygame.transform.scale(pygame.image.load(GamePath.trader),
                                          (NPCSettings.npcWidth,NPCSettings.npcHeight))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        self.items=items
        self.shopping=False
    
    def update(self, cameraX,cameraY):
        ##### Your Code Here ↓ #####
        if not self.shopping:
            if self.direction==DirectionType.RIGHT:
                self.rect.x += self.speed 
            else:
                self.rect.x -= self.speed
            #如果超出移动范围，转向
            if abs(cameraX + self.rect.x -self.initialPosition) > 50:
                #翻转图片
                self.image = pygame.transform.flip(self.image, True, False)
                # 反转方向
                if self.direction ==  DirectionType.RIGHT:
                    self.direction=DirectionType.LEFT
                else:
                    self.direction=DirectionType.RIGHT
        #更新冷却
        if not self.can_talk():
            self.talkcd -= 1
        ##### Your Code Here ↑ #####
    

class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, HP = 10, Attack = 3, Defence = 1, Money = 15):
        super().__init__()
        
        ##### Your Code Here ↓ #####
        self.image=pygame.image.load(GamePath.monster)
        self.image=pygame.transform.scale(self.image,(NPCSettings.npcWidth,NPCSettings.npcHeight))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

        self.dire = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.direindex = random.randint(0, 3)
        self.collide=Collidable()
        self.check = False
        self.dx=0
        self.dy=0
        ##### Your Code Here ↑ #####
    def update(self):
        self.dx, self.dy = self.dire[self.direindex][0]*10,self.dire[self.direindex][1]*10
        self.rect = self.rect.move(self.dx, self.dy)
    def fix(self,cameraX,cameraY):
        if self.collide.is_colliding() or self.over_range(cameraX,cameraY):
            self.direindex = random.randint(0, 3)
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

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.map=0
        self.images=[[pygame.transform.scale(
            pygame.image.load(img),(BossSettings.bossWidth,BossSettings.bossHeight)) 
            for img in GamePath.boss[self.map][index]] for index in range(4)]

        self.dir=DirectionType.LEFT
        self.speed=BossSettings.bossSpeed
        self.image_index=2
        self.index=0
        self.image=self.images[self.image_index][self.index]
        self.rect=self.image.get_rect()
        self.rect.x=None
        self.rect.y=None
        self.width=BossSettings.bossWidth
        self.height=BossSettings.bossHeight

    def choose_map(self):
        pass

    def boss_try_move(self, x, y):
        dis_x=x-self.rect.x
        dis_y=y-self.rect.y
        move=False
        if abs(dis_y) <= abs(dis_x) and abs(dis_y) > 3*(self.height+PlayerSettings.playerWidth):
            move=True
            if dis_y > 0:
                self.dir=DirectionType.UP
                self.rect.y -= self.speed
            else:
                self.dir=DirectionType.DOWN
                self.rect.y += self.speed
        if abs(dis_x) < abs(dis_y) and abs(dis_x) > 3*(self.width+PlayerSettings.playerWidth):
            move=True
            if dis_x > 0:
                self.dir=DirectionType.RIGHT
                self.rect.x += self.speed
            else:
                self.dir=DirectionType.LEFT
        if self.dir == DirectionType.DOWN:
            self.image_index=0
        if self.dir == DirectionType.RIGHT:
            self.image_index=1
        if self.dir == DirectionType.RIGHT:
            self.image_index=2
        if self.dir == DirectionType.LEFT:
            self.image_index=3
        if move:
            self.index=(self.index+1) % 4
            self.image=self.images[self.image_index][self.index]
    


    def draw(self, window, dx=0, dy=0):
        window.blit(self.images[self.image_index][self.index],(dx,dy))
        
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####
class BossAttack(pygame.sprite.Sprite):
    pass
