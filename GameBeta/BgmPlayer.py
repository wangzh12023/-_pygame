import pygame
from Settings import *

class BgmPlayer():
    def __init__(self):
        pygame.mixer.init()
        self.player=pygame.mixer.Sound(GamePath.bgm[0])
        # self.city=pygame.mixer.Sound(GamePath.bgm[1])
        # self.wild=pygame.mixer.Sound(GamePath.bgm[2])
        # self.boss=pygame.mixer.Sound(GamePath.bgm[3])
    def play(self,loop=-1):
        self.player.play(loop)
    def stop(self):
        self.player.stop()
    def update(self,GOTO):
        if GOTO==SceneType.CITY:
            self.player=pygame.mixer.Sound(GamePath.bgm[1])
        if GOTO==SceneType.WILD_GRASS or GOTO==SceneType.WILD_FIRE or GOTO==SceneType.WILD_WATER:
            self.player=pygame.mixer.Sound(GamePath.bgm[2])
        if GOTO==SceneType.BOSS_GRASS or GOTO==SceneType.BOSS_FIRE or GOTO==SceneType.BOSS_WATER:
            self.player=pygame.mixer.Sound(GamePath.bgm[3])
    
