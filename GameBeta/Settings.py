from enum import Enum
import pygame

class WindowSettings:
    name = "冤申"
    width = 1280
    height = 720
    outdoorScale = 1.5 

class BGMSettings:
    StartBGM_length=22
    Test=15

class SceneSettings:
    tileXnum = 48 # 64
    tileYnum = 27 # 36
    tileWidth = tileHeight = 40
    obstacleDensity=0.1
    Wildwidth=1920
    Wildheight=1080
    Bosswidth=1920
    Bossheight=1080
    

class PlayerSettings:
    playerSpeed = 7
    playerWidth = 33
    playerHeight = 33
    playerHP = 4
    playerAttack = 5
    playerDefence = 1
    playerMoney = 100
    playerAttackCooldown = 0.3
    playerAttackSpeed = 15
    playerAttackRange = 20
    playerGunWidth = 25
    playerGunHeight = 25
    maze_start_x= 44
    maze_start_y= 23
    Wildcoodx= 1120
    Wildcoody= 560
    Citycoodx= 640
    Citycoody= 360
    collideCD= 30

class NPCSettings:
    npcSpeed = 1
    npcWidth = 40
    npcHeight = 40
    talkCD = 30
    SelectCD = 5

class NPCType(Enum):
    DIALOG = 1
    MONSTER = 2
    SHOP = 3

class DirectionType(Enum):
    UP = 0 
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class BossSettings:
    bossWidth = 1000
    bossHeight = 1000
    bossSpeed = 4
    bossHP = 100
    bossAttack = 10
    bossDefence = 1
    bossAttackCooldown = 0.5
    bossAttackSpeed = 10
    bossAttackRange = 20
    width = 300
    height = 300
    coordX = (SceneSettings.tileXnum / 2) * SceneSettings.tileWidth - width / 2
    coordY = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight - height / 2

class SceneType(Enum):
    CITY = 1
    WILD_GRASS = 2
    WILD_WATER = 3
    WILD_FIRE = 4
    BOSS_GRASS = 5
    BOSS_WATER = 6
    BOSS_FIRE = 7
    MENU = 8
    

class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20 # Coordinate Y of the box

    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 + 10         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize               # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

class ShopSettings:
    boxWidth = 800
    boxHeight = 200
    boxStartX = WindowSettings.width // 4   # Coordinate X of the box
    boxStartY = WindowSettings.height // 3  # Coordinate Y of the box

    textSize = 56 # Default font size
    textStartX = boxStartX + 10         # Coordinate X of the first line of dialog
    textStartY = boxStartY + 25    # Coordinate Y of the first line of dialog
class GuideboardSettings:
    guideWidth=250
    guideHeight=125
    change_CD=0.15

class StatusBarSettings:
    BarWidth=300
    BarHeight=100
    ScaleWidth=227
    ScaleHeight=22
    BossScaleWidth=600
    BossScaleHeight=30
    BossScaleBgWidth=720
    BossScaleBgHeight=67
    ResourceSize=20
    Hpsize=10
class GamePath:
    bgm = [r".\assets\bgm\start_bgm.mp3",
           r".\assets\bgm\city.mp3",
           r".\assets\bgm\wild.mp3",
           r".\assets\bgm\boss.mp3",
           ]
    font = r".\assets\font\simhei.ttf"
    # Window related path
    white_bg=r".\assets\background\white.png"
    cg=r".\assets\background\cg.png"

    menu = r".\assets\background\menu.png"
    menutext = r".\assets\background\menutext.png"

    guide =[ r".\assets\background\GuideClose.png",
            r".\assets\background\GuideOpen.png"]
    guide_attention = r".\assets\background\guide_attention.png"
    guied_return = r".\assets\background\return_attention.png"
    statusbar=r".\assets\background\StatusBar.png"
    hpscale=r".\assets\background\HealthScale.png"
    boss_scale_bg=r".\assets\background\HealthScaleBG.png"

    wild = r".\assets\background\wild.png"
    mapBlock = r".\assets\background\map.png"

    # player/npc related path
    npc = r".\assets\npc\npc.png"
    Caroline = r".\assets\npc\Caroline.png"
    Justine = r".\assets\npc\Justine.png"
    trader = r".\assets\npc\trader.png"
    player = [
        [r".\assets\player\1.png", r".\assets\player\1.png",
        r".\assets\player\2.png", r".\assets\player\2.png", 
        r".\assets\player\3.png", r".\assets\player\3.png", 
        r".\assets\player\4.png", r".\assets\player\4.png"], 
        [r".\assets\player\5.png", r".\assets\player\5.png",
        r".\assets\player\6.png", r".\assets\player\6.png", 
        r".\assets\player\7.png", r".\assets\player\7.png", 
        r".\assets\player\8.png", r".\assets\player\8.png"],
        [r".\assets\player\9.png", r".\assets\player\9.png", 
        r".\assets\player\10.png", r".\assets\player\10.png", 
        r".\assets\player\11.png", r".\assets\player\11.png", 
        r".\assets\player\12.png", r".\assets\player\12.png"],
        [r".\assets\player\13.png", r".\assets\player\13.png", 
        r".\assets\player\14.png", r".\assets\player\14.png", 
        r".\assets\player\15.png", r".\assets\player\15.png", 
        r".\assets\player\16.png", r".\assets\player\16.png"]
    ]
    grass_monster = [r".\assets\npc\monster\green\green1.png",
                     r".\assets\npc\monster\green\green1.png",
                     r".\assets\npc\monster\green\green2.png",
                     r".\assets\npc\monster\green\green2.png",
                     r".\assets\npc\monster\green\green3.png",
                     r".\assets\npc\monster\green\green3.png",
                     r".\assets\npc\monster\green\green4.png",
                     r".\assets\npc\monster\green\green4.png"]
    blue_monster = [r".\assets\npc\monster\blue\blue1.png",
                     r".\assets\npc\monster\blue\blue1.png",
                     r".\assets\npc\monster\blue\blue2.png",
                     r".\assets\npc\monster\blue\blue2.png",
                     r".\assets\npc\monster\blue\blue3.png",
                     r".\assets\npc\monster\blue\blue3.png",
                     r".\assets\npc\monster\blue\blue4.png",
                     r".\assets\npc\monster\blue\blue4.png",
                     r".\assets\npc\monster\blue\blue5.png",
                     r".\assets\npc\monster\blue\blue5.png",
                     r".\assets\npc\monster\blue\blue6.png",
                     r".\assets\npc\monster\blue\blue6.png"]
    red_monster = [r".\assets\npc\monster\red\red1.png",
                     r".\assets\npc\monster\red\red1.png",
                     r".\assets\npc\monster\red\red2.png",
                     r".\assets\npc\monster\red\red2.png",
                     r".\assets\npc\monster\red\red3.png",
                     r".\assets\npc\monster\red\red3.png",
                     r".\assets\npc\monster\red\red4.png",
                     r".\assets\npc\monster\red\red4.png",
                     r".\assets\npc\monster\red\red5.png",
                     r".\assets\npc\monster\red\red5.png",
                     r".\assets\npc\monster\red\red6.png",
                     r".\assets\npc\monster\red\red6.png"]

    groundTiles = [
        r".\assets\tiles\ground1.png", 
        r".\assets\tiles\ground2.png", 
        r".\assets\tiles\ground3.png", 
        r".\assets\tiles\ground4.png", 
        r".\assets\tiles\ground5.png", 
        r".\assets\tiles\ground6.png", 
    ]
    city_bg = r".\assets\background\city_bg.png"
    cityWall = r".\assets\background\city_wall.png"

    grass_wild_bg= r".\assets\background\grass_wild.png"
    fire_wild_bg= r".\assets\background\fire_wild.png"
    water_wild_bg= r".\assets\background\water_wild.png"

    tree = r".\assets\tiles\tree.png"
    grass_bossdoor = r".\assets\tiles\bossdoor_grass.png" 

    fire = r".\assets\tiles\fire.jpg"
    fire_bossdoor = r".\assets\tiles\bossdoor_fire.png" 

    ice = r".\assets\tiles\ice.png"
    water_bossdoor = r".\assets\tiles\bossdoor_water.jpg" 

    grass_boss_bg= r".\assets\background\grass_wild.png"
    fire_boss_bg= r".\assets\background\fire_wild.png"
    water_boss_bg= r".\assets\background\water_wild.png"

    bossTiles = [
        r".\assets\tiles\boss1.png", 
        r".\assets\tiles\boss2.png", 
        r".\assets\tiles\boss3.png", 
        r".\assets\tiles\boss4.png", 
        r".\assets\tiles\boss5.png", 
        r".\assets\tiles\boss6.png", 
    ]

    bossWall = r".\assets\tiles\bossWall.png"

    portal = r".\assets\background\portal.png"
    portal_water = r".\assets\background\portal_water.png"
    portal_grass = r".\assets\background\portal_grass.png"
    portal_fire = r".\assets\background\portal_fire.png"
    attack = [r"assets\attack\up.png",
              r"assets\attack\down.png",
              r"assets\attack\left.png",
              r"assets\attack\right.png"
              ]
    gun = [ r"assets\gun\up.png",
           r"assets\gun\down.png",
           r"assets\gun\left.png",
           r"assets\gun\right.png"
           ]
    #boss 是按照“下左右上”的顺序
    boss=[  [[r"assets\npc\boss\grass\1.png",r"assets\npc\boss\grass\1.png",r"assets\npc\boss\grass\2.png",r"assets\npc\boss\grass\2.png",
              r"assets\npc\boss\grass\3.png",r"assets\npc\boss\grass\3.png",r"assets\npc\boss\grass\4.png",r"assets\npc\boss\grass\4.png"],
                [r"assets\npc\boss\grass\5.png",r"assets\npc\boss\grass\5.png",r"assets\npc\boss\grass\6.png",r"assets\npc\boss\grass\6.png",
                 r"assets\npc\boss\grass\7.png",r"assets\npc\boss\grass\7.png",r"assets\npc\boss\grass\8.png",r"assets\npc\boss\grass\8.png"],
                [r"assets\npc\boss\grass\9.png",r"assets\npc\boss\grass\9.png",r"assets\npc\boss\grass\10.png",r"assets\npc\boss\grass\10.png",
                 r"assets\npc\boss\grass\11.png",r"assets\npc\boss\grass\11.png",r"assets\npc\boss\grass\12.png",r"assets\npc\boss\grass\12.png"],
                [r"assets\npc\boss\grass\13.png",r"assets\npc\boss\grass\13.png",r"assets\npc\boss\grass\14.png",r"assets\npc\boss\grass\14.png",
                 r"assets\npc\boss\grass\15.png",r"assets\npc\boss\grass\15.png",r"assets\npc\boss\grass\16.png",r"assets\npc\boss\grass\16.png"],
            ],
            [[r"assets\npc\boss\water\1.png",r"assets\npc\boss\water\1.png",r"assets\npc\boss\water\2.png",r"assets\npc\boss\water\2.png",
              r"assets\npc\boss\water\3.png",r"assets\npc\boss\water\3.png",r"assets\npc\boss\water\4.png",r"assets\npc\boss\water\4.png"],
                [r"assets\npc\boss\water\5.png",r"assets\npc\boss\water\5.png",r"assets\npc\boss\water\6.png",r"assets\npc\boss\water\6.png",
                 r"assets\npc\boss\water\7.png",r"assets\npc\boss\water\7.png",r"assets\npc\boss\water\8.png",r"assets\npc\boss\water\8.png"],
                [r"assets\npc\boss\water\9.png",r"assets\npc\boss\water\9.png",r"assets\npc\boss\water\10.png",r"assets\npc\boss\water\10.png",
                 r"assets\npc\boss\water\11.png",r"assets\npc\boss\water\11.png",r"assets\npc\boss\water\12.png",r"assets\npc\boss\water\12.png"],
                [r"assets\npc\boss\water\13.png",r"assets\npc\boss\water\13.png",r"assets\npc\boss\water\14.png",r"assets\npc\boss\water\14.png",
                 r"assets\npc\boss\water\15.png",r"assets\npc\boss\water\15.png",r"assets\npc\boss\water\16.png",r"assets\npc\boss\water\16.png"],
            ],
            [[r"assets\npc\boss\fire\1.png",r"assets\npc\boss\fire\1.png",r"assets\npc\boss\fire\2.png",r"assets\npc\boss\fire\2.png",
              r"assets\npc\boss\fire\3.png",r"assets\npc\boss\fire\3.png",r"assets\npc\boss\fire\4.png",r"assets\npc\boss\fire\4.png"],
                [r"assets\npc\boss\fire\5.png",r"assets\npc\boss\fire\5.png",r"assets\npc\boss\fire\6.png",r"assets\npc\boss\fire\6.png",
                 r"assets\npc\boss\fire\7.png",r"assets\npc\boss\fire\7.png",r"assets\npc\boss\fire\8.png",r"assets\npc\boss\fire\8.png"],
                [r"assets\npc\boss\fire\9.png",r"assets\npc\boss\fire\9.png",r"assets\npc\boss\fire\10.png",r"assets\npc\boss\fire\10.png",
                 r"assets\npc\boss\fire\11.png",r"assets\npc\boss\fire\11.png",r"assets\npc\boss\fire\12.png",r"assets\npc\boss\fire\12.png"],
                [r"assets\npc\boss\fire\13.png",r"assets\npc\boss\fire\13.png",r"assets\npc\boss\fire\14.png",r"assets\npc\boss\fire\14.png",
                 r"assets\npc\boss\fire\15.png",r"assets\npc\boss\fire\15.png",r"assets\npc\boss\fire\16.png",r"assets\npc\boss\fire\16.png"],
            ]
        ]
class PortalSettings:
    width = 300
    height = 360
    coordX1 = (SceneSettings.tileXnum - 10) * SceneSettings.tileWidth - width / 2
    coordY1 = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight - height / 2
    coordX2 = width / 2
    coordY2 = height / 2

class GameState(Enum):
    START_CG = 1
    MAIN_MENU = 2
    GAME_PLAY_WILD_GRASS= 3
    GAME_PLAY_WILD_WATER = 4
    GAME_PLAY_WILD_FIRE = 5  
    GAME_PLAY_CITY = 6
    GAME_PLAY_BOSS_GRASS = 7
    GAME_PLAY_BOSS_WATER = 8
    GAME_PLAY_BOSS_FIRE = 9

class GameEvent:
    EVENT_SWITCH_START_MENU = pygame.USEREVENT + 1
    EVENT_SWITCH_CITY= pygame.USEREVENT + 2
    EVENT_SWITCH_WILD_GRASS= pygame.USEREVENT + 3
    EVENT_SWITCH_WILD_WATER= pygame.USEREVENT + 4
    EVENT_SWITCH_WILD_FIRE= pygame.USEREVENT + 5   
    EVENT_SWITCH_BOSS_GRASS= pygame.USEREVENT + 6
    EVENT_SWITCH_BOSS_WATER= pygame.USEREVENT + 7
    EVENT_SWITCH_BOSS_FIRE= pygame.USEREVENT + 8
    EVENT_DIALOG = pygame.USEREVENT + 9
    EVENT_END_DIALOG = pygame.USEREVENT + 10
    EVENT_SHOP = pygame.USEREVENT + 11
    EVENT_END_SHOP = pygame.USEREVENT + 12
