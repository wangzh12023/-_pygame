from enum import Enum
import pygame

class WindowSettings:
    name = "冤申"
    width = 1280
    height = 720
    outdoorScale = 1.5 

class BgmSettings:
    startBgmLength=22
    test=15
class BossType:
    GRASS=1
    WATER=2
    FIRE=3
class SceneSettings:
    tileXnum = 48 
    tileYnum = 27 
    tileWidth = tileHeight = 40
    obstacleDensity=0.07
    wildWidth=1920
    wildHeight=1080
    bossWidth=1920
    bossHeight=1080
    cityWallCoodX=480
    cityWallCoodY=0
    cityObstacleDoorCoodX=-200
    cityObstacleDoorCoodY=600
    cityObstacleBoardCoodX=800
    cityObstacleBoardCoodY=100
    cityHouseCoodX=-80
    cityHouseCoodY=0
    cityBostCoodX = 150
    cityBostCoodY = 400
    cityBost2CoodX = 380
    cityBost2CoodY = 400
    
    cityObstacleTreeCoodX = -300
    cityObstacleTreeCoodY = 620
    cityObstacleTree2CoodX = -50
    cityObstacleTree2CoodY = 620
    cityskelonCoodX = -190
    cityskelonCoodY = 750
    cityskelon2CoodX = -90
    cityskelon2CoodY = 800
    cityHouse2CoodX = 800
    cityHouse2CoodY = 550
    
    wildCameraX=640
    wildCameraY=360
    chestNum = 3

class PlayerSettings:
    playerSpeed = 7
    playerWidth = 33
    playerHeight = 33
    playerHp = 20
    playerAttack = 5
    playerDefence = 1
    playerMoney = 100
    playerAttackCooldown = 0.25
    playerAttackSpeed = 15
    playerAttackRange = 20
    playerGunWidth = 25
    playerGunHeight = 25
    mazeStartX= 44
    mazeStartY= 23
    wildCoodX= 1120
    wildCoodY= 560
    cityCoodX= 620
    cityCoodY= 80
    bossCoodX= 640
    bossCoodY= 360
    collideCd= 30

class NpcSettings:
    npcSpeed = 1
    npcWidth = 40
    npcHeight = 40
    talkCD = 30
    selectCD = 4
    shopCD = 15
    monsterNum = 5
    carolineCoodX=680
    carolineCoodY=280
    carolineDialog=[["喂，犯人，","休息得够久了吧？","快去干活!"]]
    justineCoodX=560
    justineCoodY=280
    justineDialog=[["你需要解决的怪物一共有三个,"],["火焰之地的凤凰,","极寒之地的急冻鸟,","以及扭曲森林中的鹰身女妖。"],["祝你“冤申”愉快。"]]
    igorCoodX=620
    igorCoodY=500
    igorDialog=[["呵呵，看起来你的“冤申”进行的很成功呢。"],["如果你从怪物身上的得到了金币,","可以来我这里换取力量。"]]
    igorShop={"Attack +1": "Coin -15", "Defence +1": "Coin -45",
            "HP +1": "Coin -15", "Coin +50": "HP -5", "Exit": ""}
    chairCoodX=520
    chairCoodY=40
    chairDialog=[["（这是一只板凳）"],["(你坐了上去)"],["(你站了起来)"]]
    elfCoodX=1000
    elfCoodY=240
    elfDialog=[["请看这块告示板，","那三只怪物都很危险"],["凤凰会喷吐火球，","而急冻鸟会在身边召唤冰旋，","而鹰身女妖会不定期发动俯冲。"],["请多加小心。"]]
    sisterCoodX=100
    sisterCoodY=120
    sisterDialog=[["如果受伤了的话，可以来我这里治疗哦。"]]
    soldierOneCoodX=1300
    soldierOneCoodY=600
    soldierOneDialog=[["好想摸鱼，不想上班~"],["嗯？你在找我?","可你为什么要找我这个连专属立绘","都没有的小卡拉米呢?"]]
    soldierTwoCoodX=1450
    soldierTwoCoodY=600
    soldierTwoDialog=[["说起来，你的画风和我们不太一样呢。"]]
    chestCoodX=1560
    chestCoodY=0
    chestDialog=[[["你从宝箱中获得了三点生命值！"]],
                 [["你从宝箱中获得了三点攻击力！"]],
                 [["你从宝箱中获得了一点护甲值！"]],
                 [["你从宝箱中获得了四十枚杜卡特！"]]]
    diaryCoodX=720
    diaryCoodY=40
    diaryDialog=[["(这是一本日记，记录了你所扮演的角色","“周可儿”————一名铁科学生的故事)"],
                 ["2024年1月24日","今天早上，我终于结束了我的最后一门期末考试。"],
                 ["终于可以享受我的假期了！"],
                 ["————我本来是这么认为的","可当我刚踏出考场的一瞬间,","我听到身边有同学好像在喊“冤申，乞动！”"],
                 ["然后我感受到了一阵强烈的眩晕，","等我醒来的时候，我身处一座监狱之中。"],
                 ["虽然不知道我为什么会来到这里，","但我想如果是因为同学的那句话，","那么我再喊一遍就有可能回去。"],
                 ["在我喊出了:“冤申，乞动！”之后,","这座监狱典狱长伊格尔注意到了我，","认为我想通过行动来洗刷冤情，","于是把一把长得像水枪的东西交给了我，"],
                 ["在他的授意下，我扣动了扳机，","水枪中射出了真正的子弹。"],
                 ["伊格尔与我做了一个交易，","只要我使用这把在我到来之前没人可以使用的","神器杀死三只凶恶的怪物，"],
                 ["他就愿意为我主持一场仪式，","将我送回原本的世界。"],
                 ["为了守护我本就不多的假期，我决定豁出去了。"]]
class CdType(Enum):
    LONG=1
    SHORT=2
    MEDIUM=3

class NPCType(Enum):
    DIALOG = 1
    MONSTER = 2
    SHOP = 3

class ShopType(Enum):
    TALK=1
    SHOP=2
    CLOSE=3

class DirectionType(Enum):
    UP = 0 
    DOWN = 1
    LEFT = 2
    RIGHT = 3

class BossSettings:
    bossWidth = 250
    bossHeight = 250
    bossSpeed = 4 
    bossHp = 100
    bossAttack = 3
    bossDefence = 1
    bossAttackSpeed = 10
    bossAttackRange = 16
    width = 300
    height = 300
    coordX = (SceneSettings.tileXnum / 2) * SceneSettings.tileWidth - width / 2
    coordY = (SceneSettings.tileYnum / 2) * SceneSettings.tileHeight - height / 2
    bossAttackRange = 80
    bossAttackTime = 5
    bossAttack2Time = 1
    bossAttackSpeed = 10

class MapType(Enum):
    TOPLEFT = 1
    TOPRIGHT = 2
    BOTTOMLEFT = 3
    BOTTOMRIGHT = 4
class SceneType(Enum):
    CITY = 1
    WILD_GRASS = 2
    WILD_WATER = 3
    WILD_FIRE = 4
    BOSS_GRASS = 5
    BOSS_WATER = 6
    BOSS_FIRE = 7
    MENU = 8
    GAME_OVER = 9
    GAME_CLEAR =10
    

class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxStartX = WindowSettings.width // 4 +50         # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 - 30 # Coordinate Y of the box

    textSize = 36 # Default font size
    nameStartX= WindowSettings.width // 4 + 75
    nameStartY= WindowSettings.height // 3 * 2 -25 
    textStartX = WindowSettings.width // 4 + 70         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 +40    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize               # Vertical distance of two lines

    npcWidth = 400
    npcHeight = 400
    npcCoordX = 0
    npcCoordY = WindowSettings.height-400

class ShopSettings:
    boxWidth = 500
    boxHeight = 400
    boxStartX = WindowSettings.width // 4+100  # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 -100 # Coordinate Y of the box

    textSize = 56 # Default font size
    textStartX = boxStartX + 10         # Coordinate X of the first line of dialog
    textStartY = boxStartY + 25    # Coordinate Y of the first line of dialog

    cursorStartX=WindowSettings.width // 4+50
    cursorStartY=WindowSettings.height // 3 -10
    cursorOffset=65
class GuideboardSettings:
    guideWidth=250
    guideHeight=125
    changeCd=0.1
    startCoorX=300
    startCoorY=0

class StatusBarSettings:
    barWidth=300
    barHeight=100
    scaleWidth=227
    scaleHeight=22
    bossScaleWidth=600
    bossScaleHeight=30
    bossScaleBgWidth=720
    bossScaleBgHeight=67
    resourceSize=20
    hpSize=20

    hpCoodX=15
    hpCoodY=15
    
    attackCoodX=60
    attackCoodY=60
    
    defenceCoodX=150
    defenceCoodY=60

    moneyCoodX=230
    moneyCoodY=60

    scaleCoodX=40
    scaleCoodY=13

    bossHpScaleBgCoodX=256
    bossHpScaleBgCoody=634

    bossHpScaleCoodX=350
    bossHpScaleCoody=650

class GamePath:
    bgm = [r".\assets\bgm\start_bgm.mp3",
           r".\assets\bgm\city.mp3",
           r".\assets\bgm\wild.mp3",
           r".\assets\bgm\boss.mp3",
           ]
    font = r".\assets\font\simhei.ttf"
    # Window related path
    whiteBg=r".\assets\background\white.png"
    cg=r".\assets\background\cg.png"

    menu = r".\assets\background\menu.png"
    menuText = r".\assets\background\menutext.png"

    guide =[ r".\assets\background\GuideClose.png",
            r".\assets\background\GuideOpen.png"]
    dialogBox=r".\assets\background\dialogbox.png"
    shopBox=r".\assets\background\shopbox.png"
    shopCursor=r".\assets\background\shopboxcursor.png"


    gameover = r".\assets\background\gameover.png"
    gameoverText = r".\assets\background\return_attention.png"

    gameClear = r".\assets\background\gameclear.png"
    gameClearText = r".\assets\background\gameclear_text.png"
    gameClearText2 = r".\assets\background\gameclear_text2.png"

    statusBar=r".\assets\background\StatusBar.png"
    hpScale=r".\assets\background\HealthScale.png"
    bossScaleBg=r".\assets\background\HealthScaleBG.png"

    wild = r".\assets\background\wild.png"
    mapBlock = r".\assets\background\map.png"

    # player/npc related path
    npc = r".\assets\npc\npc.png"
    caroline = r".\assets\npc\Caroline.png"
    carolineTalk = r".\assets\npc\Caroline_talk.png"
    justine = r".\assets\npc\Justine.png"
    justineTalk = r".\assets\npc\Justine_talk.png"
    chair = r".\assets\npc\chair.png"

    diary = r".\assets\npc\diary.png"
    elf=r".\assets\npc\elf.png"
    sister=r".\assets\npc\sister.png"
    soldier=r".\assets\npc\soldier.png"
    soldierTwo=r".\assets\npc\soldier2.png"

    chest=r".\assets\npc\chest.png"

    igor = r".\assets\npc\Igor.png"
    igorTalk = r".\assets\npc\Igor_talk.png"
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
    grassMonster = [r".\assets\npc\monster\green\green1.png",
                     r".\assets\npc\monster\green\green1.png",
                     r".\assets\npc\monster\green\green2.png",
                     r".\assets\npc\monster\green\green2.png",
                     r".\assets\npc\monster\green\green3.png",
                     r".\assets\npc\monster\green\green3.png",
                     r".\assets\npc\monster\green\green4.png",
                     r".\assets\npc\monster\green\green4.png"]
    blueMonster = [r".\assets\npc\monster\blue\blue1.png",
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
    redMonster = [r".\assets\npc\monster\red\red1.png",
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
    cityBg = r".\assets\background\city_bg.png"
    cityWall = r".\assets\background\city_wall.png"

    cityObstacleDoor=r".\assets\background\city_obstacle1.png"
    cityObstacleBoard=r".\assets\background\city_obstacle2.png"
    house = r".\assets\background\house.png"
    bost = r".\assets\background\bost.png"
    ObstacleTree = r".\assets\background\ObstacleTree.png"
    skelon= r".\assets\background\skelon.png"
    stone= r".\assets\background\stone.png"
    house2 = r".\assets\background\house2.png"
    grassWildBg= r".\assets\background\grass_wild.png"
    fireWildBg= r".\assets\background\fire_wild.png"
    waterWildBg= r".\assets\background\water_wild.png"

    tree = r".\assets\tiles\tree.png"
    grassBossDoor = r".\assets\tiles\bossdoor_grass.png" 

    fire = r".\assets\tiles\fire.jpg"
    fireBossDoor = r".\assets\tiles\bossdoor_fire.png" 

    ice = r".\assets\tiles\ice.png"
    waterBossDoor = r".\assets\tiles\bossdoor_water.jpg" 

    grassBossBg= r".\assets\background\grass_wild.png"
    fireBossBg= r".\assets\background\fire_wild.png"
    waterBossBg= r".\assets\background\water_wild.png"

    BossTiles = [
        r".\assets\tiles\boss1.png", 
        r".\assets\tiles\boss2.png", 
        r".\assets\tiles\boss3.png", 
        r".\assets\tiles\boss4.png", 
        r".\assets\tiles\boss5.png", 
        r".\assets\tiles\boss6.png", 
    ]

    BossWall = r".\assets\tiles\bossWall.png"

    portal = r".\assets\background\portal.png"
    portalWater = r".\assets\background\portal_water.png"
    portalGrass = r".\assets\background\portal_grass.png"
    portalFire = r".\assets\background\portal_fire.png"
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
    bossAttack = [r"assets\bossAttack\grass.png",
                  r"assets\bossAttack\fire.png",
                  r"assets\bossAttack\water1.png",
                  r"assets\bossAttack\grass2.png",
                  r"assets\bossAttack\fire2.png",
                  r"assets\bossAttack\water2.png"]
class PortalSettings:
    width = 300
    height = 360
    cityWidth = 80
    cityHeight =120
    bossDoorCoodX=SceneSettings.tileXnum//3//2*SceneSettings.tileWidth-SceneSettings.wildCameraX
    bossDoorCoodY=SceneSettings.tileYnum//3*SceneSettings.tileHeight-SceneSettings.wildCameraY
    wildCoodX=1200
    wildCoodY=600
    cityGrassCoodX=1140
    cityGrassCoodY=200
    cityWaterCoodX=-160
    cityWaterCoodY=200
    cityFireCoodX=480
    cityFireCoodY=600

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
    GAME_OVER = 10
    GAME_CLEAR = 11

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
    EVENT_GAME_OVER = pygame.USEREVENT + 13
    GAME_CLEAR = pygame.USEREVENT + 14
