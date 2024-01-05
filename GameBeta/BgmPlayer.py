import pygame
from Settings import *

class BgmPlayer():
    def __init__(self):
        ##### Your Code Here ↓ #####
        pygame.mixer_music.load(GamePath.bgm[0])
        ##### Your Code Here ↑ #####


    def play(self, name, loop=-1):
        ##### Your Code Here ↓ #####
        pygame.mixer_music.play()
        ##### Your Code Here ↑ #####

    def stop(self):
        ##### Your Code Here ↓ #####
        pygame.mixer_music.stop()
        ##### Your Code Here ↑ #####

    def update(self, GOTO):
        ##### Your Code Here ↓ #####
        pass
        ##### Your Code Here ↑ #####


    
