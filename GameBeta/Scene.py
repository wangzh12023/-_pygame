import pygame
import Maps
from random import randint
from enum import Enum
from Settings import *
from NPCs import *
#NPC, DialogNPC, ShopNPC, Monster, Boss
from PopUpBox import *          
#DialogBox, ShoppingBox
from Portal import *
#Portal
from BgmPlayer import *
from Player import Player

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
        self.boss_show = pygame.sprite.Group()
        self.boss=None
        self.if_can_generate_portals = True

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
        self.render_map()
        #渲染传送门
        if self.if_can_generate_portals:
            for portal in self.portals.sprites():
                if self.boss==None:
                    portal.draw(self.window,self.dx,self.dy)
                else:
                    portal.rect.x=self.boss.rect.x+130
                    portal.rect.y=self.boss.rect.y+120
        #渲染障碍物
        for obstacle in self.obstacles.sprites():
            obstacle.draw(self.window,self.dx,self.dy)
        #渲染NPC
        for npc in self.npcs.sprites():
            npc.draw(self.window,self.dx,self.dy)
        #渲染怪物
        for monster in self.monsters.sprites():
            monster.draw(self.window,self.dx,self.dy)
        if self.boss!=None:
            self.boss.draw(self.window,self.dx,self.dy)
        #渲染boss略缩图
        for boss in self.boss_show.sprites():
            boss.draw(self.window,self.dx,self.dy)
        player.draw(self.window,self.dx,self.dy)
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
        if 6.2<time<=7.2:
            self.cg.set_alpha(int(255*(time-6.2)))
        #19-20秒透明度变高
        if 13<time<15:
            self.cg.set_alpha(int(255*(15-time)))
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
    def __init__(self, window,is_killed):
        super().__init__(window=window)
        self.cameraX=320
        self.cameraY=0
        self.gen_CITY(is_killed)

    def gen_CITY(self,is_killed):
        self.bg=pygame.image.load(GamePath.city_bg)

        if not is_killed[0]:
            self.portals.add(Portal(GamePath.portal_grass,1140,200,SceneType.WILD_GRASS))
        if not is_killed[1]:
            self.portals.add(Portal(GamePath.portal_water,-160,200,SceneType.WILD_WATER))
        if not is_killed[2]:
            self.portals.add(Portal(GamePath.portal_fire,480,600,SceneType.WILD_FIRE))
        
        self.obstacles =Maps.gen_city_obstacle()
        
        self.npcs.add(DialogNPC(GamePath.Caroline,GamePath.Caroline_Talk,680,280,"卡萝莉娜",[["喂，犯人，","休息得够久了吧？","快去干活!"]]))
        self.npcs.add(DialogNPC(GamePath.Justine,GamePath.Justine_Talk,560,280,"芮丝汀娜",[["你需要解决的怪物一共有三个,"],["火焰之地的凤凰,","极寒之地的急冻鸟,","以及扭曲森林中的鹰身女妖。"],["祝你“冤申”愉快。"]]))

        self.npcs.add(ShopNPC(GamePath.Igor,GamePath.Igor_Talk,620,500,"伊格尔",[["呵呵，看起来你的“冤申”进行的很成功呢。"],["如果你从怪物身上的得到了金币,","可以来我这里换取力量。"]],{"Attack +1": "Coin -15", "Defence +1": "Coin -15",
            "HP +1": "Coin -15", "Coin +50": "HP -5", "Exit": ""}))
class WildScene(Scene):
    def __init__(self, window,killedBOSSnum):
        super().__init__(window=window)
        self.cameraX=640
        self.cameraY=360
        self.killedBOSSnum=killedBOSSnum
        
    def gen_WILD(self,
                 image_path_obstacle,image_path_boss_door,image_path_city_portal,
                 GOTO):
        
        self.obstacles,self.map=Maps.gen_wild_obstacle(image_path_obstacle,self.cameraX,self.cameraY)
        self.portals.add(Portal(image_path_boss_door,SceneSettings.tileXnum//3//2*SceneSettings.tileWidth-self.cameraX,
                                SceneSettings.tileYnum//3*SceneSettings.tileHeight-self.cameraY,GOTO))
        self.portals.add(Portal(image_path_city_portal,1200,600,SceneType.CITY))

    def gen_monsters(self,image_path,image_path_boss,killedBOSSnum,num = NPCSettings.monsterNum):
        i=0
        while i<num:
            x=randint(1,SceneSettings.tileXnum-2)
            y=randint(1,SceneSettings.tileYnum-2)
            if (x<=16 and y <=9) or (x>=41 and x>=20):
                continue
            flag=True
            for obstacle in self.map:
                if obstacle[0]==x and obstacle[1]==y: 
                    flag=False
            if flag:
                self.map.append([x,y])
                self.monsters.add(Monster(image_path,SceneSettings.tileWidth * x-self.cameraX, 
                                          SceneSettings.tileHeight * y-self.cameraY,killedBOSSnum))
                i+=1
                
        self.monsters.add(Boss_show(image_path_boss,SceneSettings.tileWidth * SceneSettings.tileXnum//6-self.cameraX, 
                                    SceneSettings.tileHeight * SceneSettings.tileYnum//6-self.cameraY,killedBOSSnum))
class WildGrassScene(WildScene):
    def __init__(self,window,killedBOSSnum):
        super().__init__(window=window,killedBOSSnum=killedBOSSnum)
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.grass_wild_bg),
                                       (SceneSettings.Wildwidth,SceneSettings.Wildheight))
        self.gen_WILD(GamePath.tree,GamePath.grass_bossdoor,GamePath.portal_grass,SceneType.BOSS_GRASS)
        self.gen_monsters(GamePath.grass_monster,GamePath.boss[0][0],killedBOSSnum)
class WildWaterScene(WildScene):
    def __init__(self,window,killedBOSSnum):
        super().__init__(window=window,killedBOSSnum=killedBOSSnum)
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.water_wild_bg),
                                       (SceneSettings.Wildwidth,SceneSettings.Wildheight))
        self.gen_WILD(GamePath.ice,GamePath.water_bossdoor,GamePath.portal_water,SceneType.BOSS_WATER)
        self.gen_monsters(GamePath.blue_monster,GamePath.boss[1][0],killedBOSSnum)
class WildFireScene(WildScene):
    def __init__(self,window,killedBOSSnum):
        super().__init__(window=window,killedBOSSnum=killedBOSSnum)
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.fire_wild_bg),
                                       (SceneSettings.Wildwidth,SceneSettings.Wildheight))
        self.gen_WILD(GamePath.fire,GamePath.fire_bossdoor,GamePath.portal_fire,SceneType.BOSS_FIRE)
        self.gen_monsters(GamePath.red_monster,GamePath.boss[2][0],killedBOSSnum)



class BossScene(Scene):
    def __init__(self,window,killedBOSSnum):
        super().__init__(window=window)
        self.cameraX=320
        self.cameraY=0
        
        #self.obstacles=Maps.gen_boss_obstacle()
    def gen_BOSS(self,image_path_boss,image_path_portal,image_path_bg,killedBOSSnum):
        self.boss=Boss(image_path_boss,WindowSettings.width//2+200,WindowSettings.height//2+200,killedBOSSnum)
        self.bg=pygame.transform.scale(pygame.image.load(image_path_bg),
                                       (SceneSettings.Wildwidth,SceneSettings.Wildheight))
        self.portals.add(Portal(image_path_portal,WindowSettings.width//2+200,WindowSettings.height//2+200,SceneType.CITY))  

class BossGrassScene(BossScene):
    def __init__(self,window,killedBOSSnum):
        super().__init__(window=window,killedBOSSnum=killedBOSSnum)
        self.gen_BOSS(GamePath.boss[0],GamePath.portal_grass,GamePath.grass_boss_bg,killedBOSSnum)
        self.boss_index=0
        
    
class BossWaterScene(BossScene):
    def __init__(self,window,killedBOSSnum):
        super().__init__(window=window,killedBOSSnum=killedBOSSnum)
        self.gen_BOSS(GamePath.boss[1],GamePath.portal_water,GamePath.water_boss_bg,killedBOSSnum)
        self.boss_index=1
class BossFireScene(BossScene):
    def __init__(self,window,killedBOSSnum):
        super().__init__(window=window,killedBOSSnum=killedBOSSnum)
        self.gen_BOSS(GamePath.boss[2],GamePath.portal_fire,GamePath.fire_boss_bg,killedBOSSnum)
        self.boss_index=2
class GameOverScene():
    def __init__(self, window):
        self.window=window
        #导入背景图
        self.bg=pygame.image.load(GamePath.gameover)
        self.bg=pygame.transform.scale(self.bg,(WindowSettings.width,WindowSettings.height))
        self.text=pygame.image.load(GamePath.gameover_text)
        self.text=pygame.transform.scale(self.text,(WindowSettings.width,WindowSettings.height))
    def render(self, time):
        self.window.blit(self.bg,(0,0))
        self.text.set_alpha(int(255*abs(1-(time%2))))
        self.window.blit(self.text,(0,0))
class GameClearScene():
    def __init__(self, window):
        self.window=window
        #导入背景图
        self.bg=pygame.image.load(GamePath.gameclear)
        self.bg=pygame.transform.scale(self.bg,(WindowSettings.width,WindowSettings.height))
        # self.text=pygame.image.load(GamePath.gameover_text)
        # self.text=pygame.transform.scale(self.text,(WindowSettings.width,WindowSettings.height))
    def render(self):
        self.window.blit(self.bg,(0,0))
        # self.text.set_alpha(int(255*abs(1-(time%2))))
        # self.window.blit(self.text,(0,0))