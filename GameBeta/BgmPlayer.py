import pygame
from Settings import *

class BgmPlayer():
    def __init__(self):

        self.start=pygame.mixer.Sound(GamePath.bgm[0])
        self.city=pygame.mixer.Sound(GamePath.bgm[1])
        self.wild=pygame.mixer.Sound(GamePath.bgm[2])
        self.boss=pygame.mixer.Sound(GamePath.bgm[3])


    
