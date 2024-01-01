import pygame
import sys,os
bg_path=file_abs_path = os.path.abspath('grass.png')
bg=pygame.image.load('.\grass.png')
player=pygame.image.load(".\player.png")
player=pygame.transform.scale(player,(50,50))
width,height=1280,720

# pygame setup
pygame.init()
#screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
running = True
window = pygame.display.set_mode((width, height))

class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
speed=25
# 在游戏中创建人物对象
player_rect = Character(800, 600)  # 以 (100, 100) 为初始坐标
def run_game_rect():
    if keys[pygame.K_LEFT]:
            # player_rect.update_position(player_rect.x-speed,player_rect.y)
            player_rect.x-=speed
    if keys[pygame.K_RIGHT]:
        # player_rect.update_position(player_rect.x-speed,player_rect.y)
        player_rect.x+=speed
    if keys[pygame.K_UP]:
        # player_rect.update_position(player_rect.x-speed,player_rect.y)
        player_rect.y-=speed
    if keys[pygame.K_DOWN]:
        # player_rect.update_position(player_rect.x-speed,player_rect.y)
        player_rect.y+=speed
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys=pygame.key.get_pressed()

    run_game_rect()
    # fill the screen with a color to wipe away anything from last frame
    # window.fill((0, 0, 0)) 
    window.blit(bg,(0,0))
    window.blit(player,(player_rect.x,player_rect.y))
    # 填充窗口为黑色

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
pygame.quit()
