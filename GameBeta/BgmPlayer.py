import pygame
from Settings import *

class BgmPlayer():
    def __init__(self):
        pygame.mixer.init()
    def play(self, index):
        pygame.mixer_music.load(GamePath.bgm[index])
        pygame.mixer_music.play()

    def stop(self):
        pygame.mixer_music.stop()

    def update(self, GOTO):
        pass


    
