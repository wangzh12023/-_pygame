import pygame
from Settings import *
from random import random, randint

class Obsatacle(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)

    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
        
class Block(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, width=SceneSettings.tileWidth, height=SceneSettings.tileHeight):
        super().__init__()
        self.image=pygame.transform.scale(image,(width,height))
        self.rect=self.image.get_rect()
        self.rect.topleft=(x,y)
        
    def draw(self, window, dx=0, dy=0):
        self.rect=self.rect.move(dx,dy)
        window.blit(self.image,self.rect)
#随机生成地图
'''
def gen_wild_map():
    images=[pygame.transform.scale(pygame.image.load(tile),
                (SceneSettings.tileWidth,SceneSettings.tileHeight)) 
                for tile in GamePath.groundTiles]
    mapObj=[]
    for i in range(SceneSettings.tileXnum):
        tmp=[]
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0,len(images)-1)])
        mapObj.append(tmp)
    return mapObj
'''
'''
def gen_city_map():
    images=[pygame.transform.scale(pygame.image.load(tile),
                (SceneSettings.tileWidth,SceneSettings.tileHeight)) 
                for tile in GamePath.cityTiles]
    mapObj=[]
    for i in range(SceneSettings.tileXnum):
        tmp=[]
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0,len(images)-1)])
        mapObj.append(tmp)
    return mapObj
'''
def gen_boss_map():
    images=[pygame.transform.scale(pygame.image.load(tile),
                (SceneSettings.tileWidth,SceneSettings.tileHeight)) 
                for tile in GamePath.bossTiles]
    mapObj=[]
    for i in range(SceneSettings.tileXnum):
        tmp=[]
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0,len(images)-1)])
        mapObj.append(tmp)
    return mapObj

def gen_city_obstacle():
    image = pygame.image.load(GamePath.cityWall)
    obstacles = pygame.sprite.Group()
    obstacles.add(Obsatacle(image,480,40))
    return obstacles
'''
def gen_wild_obstacle():

    image = pygame.image.load(GamePath.tree)
    obstacles = pygame.sprite.Group()

    midX = SceneSettings.tileXnum // 2
    midY = SceneSettings.tileYnum // 2

    for i in range(SceneSettings.tileXnum):
        for j in range(SceneSettings.tileYnum):
            if random() < SceneSettings.obstacleDensity and \
                ((i not in range(midX - 3, midX + 4))\
                or (j not in range(midY - 3, midY + 4)))\
                and (i > midX or j > midY):
                obstacles.add(Block(image, 
                    SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
                
    return obstacles
'''
def gen_wild_obstacle(cameraX,cameraY):#生成障碍物
    #障碍物包括：隔离boss区的障碍围栏和构成迷宫的随机生成障碍。
    #障碍围栏中有一个特殊的door对象，负责检测碰撞并进行传送
    
    image=pygame.image.load(GamePath.tree)
    #image为障碍物的图片。由于迷宫有7个，每个迷宫用的障碍图片又不相同，所以每个迷宫都设置一个不同的path用来载入对应的不同的图片
    obstacles = pygame.sprite.Group()

    #生成障碍围栏，面积暂定为总画面的九分之一
    xx=SceneSettings.tileXnum//3
    yy=SceneSettings.tileYnum//3
    for i in range(xx+1):
        if i==xx//2:continue#这行是留个空给door
        obstacles.add(Block(image,i*SceneSettings.tileWidth-cameraX,yy*SceneSettings.tileHeight-cameraY))
    for j in range(yy):
        obstacles.add(Block(image,xx*SceneSettings.tileWidth-cameraX,j*SceneSettings.tileHeight-cameraY))
    #以上两个for循环，生成了除door之外的boss区障碍围栏并加入精灵组obstacles

    #随机生成非boss区障碍物
    random_obstacle=gen_random_obstacle(xx,yy)#先 生成一个坐标组。
    for i in range(len(random_obstacle)):#再导入精灵组obstacles
        obstacle_x=random_obstacle[i][0]
        obstacle_y=random_obstacle[i][1]
        obstacles.add(Block(image,obstacle_x*SceneSettings.tileWidth-cameraX,obstacle_y*SceneSettings.tileHeight-cameraY))
    return obstacles


def gen_boss_obstacle():

    image = pygame.image.load(GamePath.bossWall)
    obstacles = pygame.sprite.Group()

    midX = SceneSettings.tileXnum // 2
    midY = SceneSettings.tileYnum // 2

    for i in range(SceneSettings.tileXnum):
        for j in range(SceneSettings.tileYnum):
            if random() < SceneSettings.obstacleDensity and \
                ((i not in range(midX - 3, midX + 4))\
                or (j not in range(midY - 3, midY + 4)))\
                and (i > midX or j > midY):
                obstacles.add(Block(image, 
                    SceneSettings.tileWidth * i, SceneSettings.tileHeight * j))
    return obstacles
#下面是用于随机生成迷宫的函数
def get_random(xx,yy):#生成一组随机的坐标，对应随机生成的障碍物的坐标
    sequence = []#sequence[1]代表x坐标，sequence[2]代表y坐标
    for i in range(SceneSettings.tileXnum):
        for j in range(SceneSettings.tileYnum):
            #两个筛选条件：不可在boss区内生成、不可在迷宫出生点的3单位之内生成
            if i<=xx and j<=yy:continue
            if abs(PlayerSettings.maze_start_x-i)<=3 and abs(PlayerSettings.maze_start_y-j)<=3:continue
            #开始随机生成障碍物
            if random()>=SceneSettings.obstacleDensity:continue
            sequence.append([i,j])
    return sequence

def BFS(random_obstacle,xx,yy):#用搜索算法检验
    step=set()
    for i in range(len(random_obstacle)):#先将随机生成的障碍物全部标记为不可行
        x=random_obstacle[i][0];y=random_obstacle[i][1]
        step.add((x,y))

    step.add((PlayerSettings.maze_start_x,PlayerSettings.maze_start_y))
    sequence=[(PlayerSettings.maze_start_x,PlayerSettings.maze_start_y)]#将迷宫中的起点入队列
    
    while(len(sequence)!=0):
        dx=sequence[0][0];dy=sequence[0][1]
        
        directions=[(0,1),(0,-1),(1,0),(-1,0)]#枚举四个方向
        for dire in directions:
            nx=dx+dire[0];ny=dy+dire[1]
            #三个筛选条件:必须没有被标记、必须不出地图边界、必须不接触BOSS区域的障碍物围栏（door除外）
            if (nx,ny) in step:continue
            if not (0<=dx<SceneSettings.tileXnum and 0<=dy<SceneSettings.tileYnum):continue
            if nx<=xx and ny<=yy and not (nx==xx//2 and ny==yy):continue
            
            if nx==xx//2 and ny==yy:return True#能走到door的位置，判断为可行，结束搜索
            step.add((nx,ny))
            sequence.append((nx,ny))
        
        sequence.pop(0) 

    return False

def gen_random_obstacle(xx,yy):
    random_obstacle=get_random(xx,yy)
    while not BFS(random_obstacle,xx,yy):#如果BFS判为false，即不可从起点到达door，就重新生成
        random_obstacle=get_random(xx,yy)
    return random_obstacle