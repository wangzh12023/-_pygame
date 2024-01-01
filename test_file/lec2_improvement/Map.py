# -*- coding:utf-8 -*-
from Settings import *
import pygame
from random import random, randint

class Block(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        pass

    def fix_with_BG(self, cameraX, cameraY):
        pass

def gen_map():
    images = [pygame.image.load(tile) for tile in GamePath.groundTiles]
    images = [pygame.transform.scale(image, (SceneSettings.tileWidth, SceneSettings.tileHeight)) for image in images]

    mapObj = []
    for i in range(SceneSettings.tileXnum):
        tmp = []
        for j in range(SceneSettings.tileYnum):
            tmp.append(images[randint(0, len(images) - 1)])
        mapObj.append(tmp)
    
    return mapObj
def gen_map_2():
    image=pygame.image.load(GamePath.skd)
    map_skd_part=[]
    for i in range(0,image.get_width()-40,40):
        temp=[]
        for j in range(0,image.get_height()-40,40):
            sub_rect=pygame.Rect(i,j,40,40)
            sub_image = image.subsurface(sub_rect)
            temp.append(sub_image)
        map_skd_part.append(temp)
    return map_skd_part
def build_obstacle():
    pass

print(gen_map_2())