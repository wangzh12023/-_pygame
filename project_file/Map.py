'''
需要用到的Settings声明:
SceneSettings.tileWidth, SceneSettings.tileHeight:同上课内容：方块的长和宽
WindowSettings.width,WindowSettings.height:同上课内容：窗口总大小
SceneSettings.tileXnum,SceneSettings.tileYnum:同上课内容:窗口中xy方向总像素数量
SceneSettings.obstacleDensity:同上课内容。用于随机障碍生成
PlayerSettings.maze_start_x,PlayerSettings.maze_start_y:新增参数。表示迷宫中玩家的出生点。  
SceneSettings.statue_x[i],SceneSettings.statue_y[i]:新增参数。表示主地图中传送石雕的7个坐标。x,y分别储存在2个列表中。  
GamePath.statue_image:新增参数。表示主地图中石雕图片的调用路径
GamePath.MainMapTile:新增参数。表示主地图的背景图片调用路径   
GamePath.bossDoor:新增参数。表示boss区传送门的图片调用路径   
GamePath.groundTiles:同上课内容。表示迷宫区像素砖块的图片调用路径
def gen_Obstacles(obstacle_path):obstacle_path是一个传递来的参数,表示障碍物图片的路径。这个路径应该在SceneManager的调用步骤中设定出来。
'''
from Settings import *
import pygame
from random import random,randint


class Block(pygame.sprite.Sprite):#创建一个精灵组为Block，参数为图像、xy坐标
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

def gen_statues():#生成主地图上的7个传送石雕
    statues=pygame.sprite.Group()
    statue_image=pygame.image.load(GamePath.statue_image)#载入图片
    for i in range(7):
        statue_x=SceneSettings.statue_x[i]
        statue_y=SceneSettings.statue_y[i]
        statue.add(Block(statue_image,statue_x,statue_y))
    return statues

def gen_MainMap():#生成主地图
    #可以考虑主地图不用像素拼接构成，而是一张高分辨率的大图，如下
    background=pygame.image.load(GamePath.MainMapTile)
    background=pygame.transform.scale(background,(WindowSettings.width,WindowSettings.height))
    return background

def gen_MazeMap():#生成迷宫地图的像素背景
    images=[pygame.image.load(tile) for tile in GamePath.groundTiles]
    images=[pygame.transform.scale(image,(SceneSettings.tileWidth,SceneSettings.tileHeight)) for image in images]
    
    mapObj=[]
    for i in range(SceneSettings.tileXnum):
        tmp=[]
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0,len(images)-1)])
        mapObj.append(tmp)
    
    return mapObj    

def get_random(xx,yy):#生成一组随机的坐标，对应随机生成的障碍物的坐标
    sequence = [[] for _ in range(3)]#sequence[1]代表x坐标，sequence[2]代表y坐标
    for i in range(SceneSettings.tileXnum):
        for j in range(SceneSettings.tileYnum):
            #两个筛选条件：不可在boss区内生成、不可在迷宫出生点的3单位之内生成
            if i<=xx and j<=yy:continue
            if PlayerSettings.maze_start_x-3<=i<=PlayerSettings.maze_start_x+3 and PlayerSettings.maze_start_y-3<=i<=PlayerSettings.maze_start_y+3:continue
            #开始随机生成障碍物
            if random()>=SceneSettings.obstacleDensity:continue
            sequence[1].append(i)
            sequence[2].append(j)
    return sequence

def BFS(random_obstacle,xx,yy):#用搜索算法检验
    step=set()
    for i in range(len(random_obstacle)):#先将随机生成的障碍物全部标记为不可行
        x=random_obstacle[1][i];y=random_obstacle[2][i]
        step.add((x,y))

    step.add((PlayerSettings.maze_start_x,PlayerSettings.maze_start_y))
    sequence=[[PlayerSettings.maze_start_x],[PlayerSettings.maze_start_y]]#将迷宫中的起点入队列
    
    while(len(sequence)!=0):
        dx=sequence[0][0];dy=sequence[1][0]
        
        directions=[(0,1),(0,-1),(1,0),(-1,0)]#枚举四个方向
        for dire in directions:
            nx=dx+dire[0];ny=dy+dire[1]
            #三个筛选条件:必须没有被标记、必须不出地图边界、必须不接触BOSS区域的障碍物围栏（door除外）
            if (nx,ny) in step:continue
            if not (0<=dx<=SceneSettings.tileXnum and 0<=dy<=SceneSettings.tileYnum):continue
            if nx<=xx and ny<=yy and not (nx==xx//2 and ny==yy):continue
            
            if nx==xx//2 and ny==yy:return True#能走到door的位置，判断为可行，结束搜索
            step.add((nx,ny))
            sequence[0].append(nx);sequence[1].append(ny)
        
        sequence[0].pop(0);sequence[1].pop(0)   

    return False

def gen_random_obstacle(xx,yy):
    random_obstacle=get_random(xx,yy)
    while not BFS(random_obstacle,xx,yy):#如果BFS判为false，即不可从起点到达door，就重新生成
        random_obstacle=get_random(xx,yy)
    return random_obstacle

def gen_Obstacles(obstacle_path):#生成障碍物
    #障碍物包括：隔离boss区的障碍围栏和构成迷宫的随机生成障碍。
    #障碍围栏中有一个特殊的door对象，负责检测碰撞并进行传送
    
    image=pygame.image.load(obstacle_path)
    #image为障碍物的图片。由于迷宫有7个，每个迷宫用的障碍图片又不相同，所以每个迷宫都设置一个不同的path用来载入对应的不同的图片
    Boss_door=pygame.image.load(GamePath.bossDoor)
    #Boss_door为door专属的图片
    obstacles = pygame.sprite.Group()

    #生成障碍围栏，面积暂定为总画面的九分之一
    xx=SceneSettings.tileXnum//3
    yy=SceneSettings.tileYnum//3
    for i in range(xx):
        if i==xx//2:continue#这行是留个空给door
        obstacles.add(Block(image,i*SceneSettings.tileWidth,yy*SceneSettings.tileHidth))
    for j in range(yy):
        obstacles.add(Block(image,xx*SceneSettings.tileWidth,j*SceneSettings.tileHidth))
    #以上两个for循环，生成了除door之外的boss区障碍围栏并加入精灵组obstacles
    obstacles.add(Block(Boss_door,xx//2*SceneSettings.tileWidth,yy*SceneSettings.tileHidth))
    #上面这一行是生成door并加入精灵组obstacles-=

    #随机生成非boss区障碍物
    random_obstacle=gen_random_obstacle(xx,yy)#先 生成一个坐标组。
    for i in range(len(random_obstacle)):#再导入精灵组obstacles
        obstacle_x=random_obstacle[1][i]
        obstacle_y=random_obstacle[2][i]
        obstacles.add(Block(image,obstacle_x,obstacle_y))

    return obstacles