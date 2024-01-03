from enum import Enum

class WindowSettings:
    name = "Marked Odyssey"
    width = 1600
    height = 800
    outdoorScale = None

class PlayerSettings:
    playerSpeed = None
    playerWidth = None
    playerHeight = None
    playerHP = None
    playerAttack = None

class NPCSettings:
    npcSpeed = 1
    npcWidth = 60
    npcHeight = 60
    talkCD = 30           # 1s

class MonsterSettings:
    BOSSWidth = 60
    BOSSHeight = 60
    BOSSHP = 10
    BOSSAttack = 3
    SmallMonsterWidth = None
    SmallMonsterHeight = None
    SmallMonsterHP = None

class SceneSettings:
    tileXnum = None
    tileYnum = None
    tileWidth = tileHeight = None
    obstacleDensity = None          #<1
    statue_x = []                  # position
    statue_y = []
    
class DialogSettings:
    boxWidth = 800
    boxHeight = 180
    boxAlpha = 150
    boxStartX = WindowSettings.width // 4           # Coordinate X of the box
    boxStartY = WindowSettings.height // 3 * 2 + 20 # Coordinate Y of the box

    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 + 10         # Coordinate X of the first line of dialog
    textStartY = WindowSettings.height // 3 * 2 + 30    # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3                # Vertical distance of two lines

    npcWidth = WindowSettings.width // 5
    npcHeight = WindowSettings.height // 3
    npcCoordX = 0
    npcCoordY = WindowSettings.height * 2 // 3 - 20

class BattleSettings:
    boxWidth = WindowSettings.width * 3 // 4 
    boxHeight = WindowSettings.height * 3 // 4 
    boxAlpha = 200
    boxStartX = WindowSettings.width // 8           # Coordinate X of the box
    boxStartY = WindowSettings.height // 8
    textSize = 48 # Default font size
    textStartX = WindowSettings.width // 4 
    textPlayerStartX = WindowSettings.width // 4          # Coordinate X of the first line of dialog
    textMonsterStartX = WindowSettings.width // 2 +100   
    textStartY = WindowSettings.height // 3         # Coordinate Y of the first line of dialog
    textVerticalDist = textSize // 4 * 3            # Vertical distance of two lines

    playerWidth = WindowSettings.width // 6
    playerHeight = WindowSettings.height // 3
    playerCoordX = WindowSettings.width // 8
    playerCoordY = WindowSettings.height // 2

    monsterWidth = WindowSettings.width // 6
    monsterHeight = WindowSettings.height // 3
    monsterCoordX = WindowSettings.width * 5 // 8
    monsterCoordY = WindowSettings.height // 2 

    
    animationCount = 15

    stepSpeed = 20

class GamePath:
    # palyer has four state,  the first number of the file_name, 1,2,3,4, represents respectly up, down, left, right. 
    player = [
        r".\assets\player\11.png", r".\assets\player\12.png", r".\assets\player\13.png", r".\assets\player\14.png", 
        r".\assets\player\21.png", r".\assets\player\22.png", r".\assets\player\23.png", r".\assets\player\24.png", 
        r".\assets\player\31.png", r".\assets\player\32.png", r".\assets\player\33.png", r".\assets\player\34.png", 
        r".\assets\player\41.png", r".\assets\player\42.png", r".\assets\player\43.png", r".\assets\player\44.png",         
    ]
    
    npc = r".\assets\npc\1.png"
    
    MonsterList = [
        r".\assets\npc\monster\1.png"
        r".\assets\npc\monster\2.png"
        r".\assets\npc\monster\3.png"
    ]
    
    StatueList = [ 
        r".\assets\statue\1.png",
        r".\assets\statue\2.png",
        r".\assets\statue\3.png",
    ]
    
    groundTiles = [
        [r".\assets\tiles\map_1\ground1.png", r".\assets\tiles\map_1\ground2.png", r".\assets\tiles\map_1\ground3.png", r".\assets\tiles\map_1\ground4.png", r".\assets\tiles\map_1\ground5.png", r".\assets\tiles\map_1\ground6.png"],
        [r".\assets\tiles\map_2\ground1.png", r".\assets\tiles\map_2\ground2.png", r".\assets\tiles\map_2\ground3.png", r".\assets\tiles\map_2\ground4.png", r".\assets\tiles\map_2\ground5.png", r".\assets\tiles\map_2\ground6.png"],
        [r".\assets\tiles\map_3\ground1.png", r".\assets\tiles\map_3\ground2.png", r".\assets\tiles\map_3\ground3.png", r".\assets\tiles\map_3\ground4.png", r".\assets\tiles\map_3\ground5.png", r".\assets\tiles\map_3\ground6.png"]
    ]

    tree = r".\assets\tiles\tree.png"

class GameState(Enum):
    MAIN_MENU = 1
    GAME_LOADING = 2
    GAME_OVER = 3
    GAME_WIN = 4
    GAME_PAUSE = 5
    GAME_PLAY_WILD = 6