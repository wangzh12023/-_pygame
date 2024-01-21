import pygame
import Maps
from random import randint
from enum import Enum
from Settings import *
from NPCs import *
#NPC, DialogNPC, ShopNPC, Monster, BOSS
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
        self.bossShow = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()

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
        for portal in self.portals.sprites():
            portal.draw(self.window,self.dx,self.dy)
        #渲染障碍物
        for obstacle in self.obstacles.sprites():
            obstacle.draw(self.window,self.dx,self.dy)
        #渲染NPC
        for npc in self.npcs.sprites():
            npc.draw(self.window,self.dx,self.dy)
        #渲染怪物
        for monster in self.monsters.sprites():
            monster.draw(self.window,self.dx,self.dy)
        player.draw(self.window,self.dx,self.dy)
        for boss in self.bosses.sprites():
            boss.draw(self.window,self.dx,self.dy)
        #渲染BOSS略缩图
        for boss in self.bossShow.sprites():
            boss.draw(self.window,self.dx,self.dy)
        
    def render_map(self):
        self.window.blit(self.bg,(-self.cameraX,-self.cameraY))
class StartCG():
    def __init__(self, window):
        self.window=window
        #导入背景图
        self.bg=pygame.image.load(GamePath.whiteBg)
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
        self.text=pygame.image.load(GamePath.menuText)

    def render(self, time):
        self.window.blit(self.bg,(0,0))
        self.text.set_alpha(int(255*abs(1-(time%2))))
        self.window.blit(self.text,(WindowSettings.width//3,WindowSettings.height//4*3))

class CityScene(Scene):
    def __init__(self, window,isKilled):
        super().__init__(window=window)
        self.cameraX=320
        self.cameraY=0
        self.gen_city(isKilled)

    def gen_city(self,isKilled):
        self.bg=pygame.image.load(GamePath.cityBg)

        if not isKilled[0]:
            self.portals.add(Portal(GamePath.portalGrass,1140,200,SceneType.WILD_GRASS))
        if not isKilled[1]:
            self.portals.add(Portal(GamePath.portalWater,-160,200,SceneType.WILD_WATER))
        if not isKilled[2]:
            self.portals.add(Portal(GamePath.portalFire,480,600,SceneType.WILD_FIRE))
        
        self.obstacles =Maps.gen_city_obstacle()

        self.npcs.add(DialogNPC(GamePath.chair,GamePath.chair,NpcSettings.chairCoodX,
                                NpcSettings.chairCoodY,"凳子",NpcSettings.chairDialog))
        
        self.npcs.add(DialogNPC(GamePath.diary,GamePath.diary,NpcSettings.diaryCoodX,
                                NpcSettings.diaryCoodY,"日记",NpcSettings.diaryDialog))
        self.npcs.add(DialogNPC(GamePath.elf,GamePath.elf,NpcSettings.elfCoodX,
                                NpcSettings.elfCoodY,"精灵游侠",NpcSettings.elfDialog))
        self.npcs.add(DialogNPC(GamePath.sister,GamePath.sister,NpcSettings.sisterCoodX,
                                NpcSettings.sisterCoodY,"治疗师",NpcSettings.sisterDialog))
        self.npcs.add(Chest(GamePath.chest,GamePath.chest,NpcSettings.chestCoodX,
                                NpcSettings.chestCoodY,"宝箱",NpcSettings.chestDialog))

        self.npcs.add(DialogNPC(GamePath.soldier,GamePath.soldier,NpcSettings.soldierOneCoodX,
                                NpcSettings.soldierOneCoodY,"狱卒甲",NpcSettings.soldierOneDialog))
        self.npcs.add(DialogNPC(GamePath.soldierTwo,GamePath.soldier,NpcSettings.soldierTwoCoodX,
                                NpcSettings.soldierTwoCoodY,"狱卒乙",NpcSettings.soldierTwoDialog))
        
        self.npcs.add(DialogNPC(GamePath.caroline,GamePath.carolineTalk,NpcSettings.carolineCoodX,
                                NpcSettings.carolineCoodY,"卡萝莉娜",NpcSettings.carolineDialog))
        
        self.npcs.add(DialogNPC(GamePath.justine,GamePath.justineTalk,NpcSettings.justineCoodX,
                                NpcSettings.justineCoodY,"芮丝汀娜",NpcSettings.justineDialog))

        self.npcs.add(ShopNPC(GamePath.igor,GamePath.igorTalk,NpcSettings.igorCoodX,
                              NpcSettings.igorCoodY,"伊格尔",NpcSettings.igorDialog,NpcSettings.igorShop))
        
class WildScene(Scene):
    def __init__(self, window,killedBossNum):
        super().__init__(window=window)
        self.cameraX=SceneSettings.wildCameraX
        self.cameraY=SceneSettings.wildCameraY
        self.killedBossNum=killedBossNum
        
    def gen_wild(self,
                 imagePathObstacle,imagePathBossDorr,imagePathCityPortal,
                 GOTO):
        
        self.obstacles,self.map=Maps.gen_wild_obstacle(imagePathObstacle,self.cameraX,self.cameraY)
        self.portals.add(Portal(imagePathBossDorr,PortalSettings.bossDoorCoodX,
                                PortalSettings.bossDoorCoodY,GOTO))
        self.portals.add(Portal(imagePathCityPortal,PortalSettings.wildCoodX,PortalSettings.wildCoodY,SceneType.CITY))
    def gen_chest(self,num = SceneSettings.chestNum):
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
                self.npcs.add(Chest(GamePath.chest,GamePath.chest,SceneSettings.tileWidth * x-self.cameraX, 
                                        SceneSettings.tileHeight * y-self.cameraY,"宝箱",NpcSettings.chestDialog))
                i+=1
    def gen_monsters(self,imagePath,imagePathBOSS,killedBossNum,num = NpcSettings.monsterNum):
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
                self.monsters.add(Monster(imagePath,SceneSettings.tileWidth * x-self.cameraX, 
                                          SceneSettings.tileHeight * y-self.cameraY,killedBossNum))
                i+=1
                
        self.monsters.add(BossShow(imagePathBOSS,SceneSettings.tileWidth * SceneSettings.tileXnum//6-self.cameraX, 
                                    SceneSettings.tileHeight * SceneSettings.tileYnum//6-self.cameraY,killedBossNum))
class WildGrassScene(WildScene):
    def __init__(self,window,killedBossNum):
        super().__init__(window=window,killedBossNum=killedBossNum)
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.grassWildBg),
                                       (SceneSettings.wildWidth,SceneSettings.wildHeight))
        self.gen_wild(GamePath.tree,GamePath.grassBossDoor,GamePath.portalGrass,SceneType.BOSS_GRASS)
        self.gen_chest()
        self.gen_monsters(GamePath.grassMonster,GamePath.boss[0][0],killedBossNum)
class WildWaterScene(WildScene):
    def __init__(self,window,killedBossNum):
        super().__init__(window=window,killedBossNum=killedBossNum)
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.waterWildBg),
                                       (SceneSettings.wildWidth,SceneSettings.wildHeight))
        self.gen_wild(GamePath.ice,GamePath.waterBossDoor,GamePath.portalWater,SceneType.BOSS_WATER)
        self.gen_chest()
        self.gen_monsters(GamePath.blueMonster,GamePath.boss[1][0],killedBossNum)
class WildFireScene(WildScene):
    def __init__(self,window,killedBossNum):
        super().__init__(window=window,killedBossNum=killedBossNum)
        self.bg=pygame.transform.scale(pygame.image.load(GamePath.fireWildBg),
                                       (SceneSettings.wildWidth,SceneSettings.wildHeight))
        self.gen_wild(GamePath.fire,GamePath.fireBossDoor,GamePath.portalFire,SceneType.BOSS_FIRE)
        self.gen_chest()
        self.gen_monsters(GamePath.redMonster,GamePath.boss[2][0],killedBossNum)



class BossScene(Scene):
    def __init__(self,window,killedBossNum):
        super().__init__(window=window)
        self.cameraX=320
        self.cameraY=0
        
        #self.obstacles=Maps.gen_BOSS_obstacle()
    def gen_boss(self,imagePathBoss,bossMap,imagePathPortal,imagePathBg,killedBossNum):
        self.boss=Boss(imagePathBoss,bossMap,WindowSettings.width//2+200,WindowSettings.height//2+200,killedBossNum)
        self.bosses.add(self.boss)
        self.bg=pygame.transform.scale(pygame.image.load(imagePathBg),
                                       (SceneSettings.wildWidth,SceneSettings.wildHeight))
        self.portals.add(Portal(imagePathPortal,-200,-200,SceneType.CITY))  

class BossGrassScene(BossScene):
    def __init__(self,window,killedBossNum):
        super().__init__(window=window,killedBossNum=killedBossNum)
        self.gen_boss(GamePath.boss[0],BossType.GRASS,GamePath.portalGrass,GamePath.grassBossBg,killedBossNum)
        self.bossIndex=0
        
class BossWaterScene(BossScene):
    def __init__(self,window,killedBossNum):
        super().__init__(window=window,killedBossNum=killedBossNum)
        self.gen_boss(GamePath.boss[1],BossType.WATER,GamePath.portalWater,GamePath.waterBossBg,killedBossNum)
        self.bossIndex=1
        
class BossFireScene(BossScene):
    def __init__(self,window,killedBossNum):
        super().__init__(window=window,killedBossNum=killedBossNum)
        self.gen_boss(GamePath.boss[2],BossType.FIRE,GamePath.portalFire,GamePath.fireBossBg,killedBossNum)
        self.bossIndex=2
        
class GameOverScene():
    def __init__(self, window):
        self.window=window
        #导入背景图
        self.bg=pygame.image.load(GamePath.gameover)
        self.bg=pygame.transform.scale(self.bg,(WindowSettings.width,WindowSettings.height))
        self.text=pygame.image.load(GamePath.gameoverText)
        self.text=pygame.transform.scale(self.text,(WindowSettings.width,WindowSettings.height))
    def render(self, time):
        self.window.blit(self.bg,(0,0))
        self.text.set_alpha(int(255*abs(1-(time%2))))
        self.window.blit(self.text,(0,0))
class GameClearScene():
    def __init__(self, window,time):
        self.window=window
        #导入背景图
        self.bg=pygame.image.load(GamePath.gameClear)
        self.bg=pygame.transform.scale(self.bg,(WindowSettings.width,WindowSettings.height))
        self.bgText=pygame.image.load(GamePath.gameClearText)
        self.bgText2=pygame.image.load(GamePath.gameClearText2)
        self.startTime=time
        # self.text=pygame.image.load(GamePath.gameover_text)
        # self.text=pygame.transform.scale(self.text,(WindowSettings.width,WindowSettings.height))
    def render(self,time):
        self.window.blit(self.bg,(0,0))
        #从14-19秒透明度变低
        if time-self.startTime<=10:
            if 0<time-self.startTime<=5:
                self.bgText.set_alpha(int(51*(time-self.startTime)))
            #19-20秒透明度变高
            if 5<time-self.startTime<=10:
                self.bgText.set_alpha(int(51*(10-(time-self.startTime))))
            self.window.blit(self.bgText,(0,0))
        else:
            self.bgText2.set_alpha(int(255*abs(1-(time%2))))
            self.window.blit(self.bgText2,(0,0))