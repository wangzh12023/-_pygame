import pygame
import random

pygame.init()

win_width, win_height = 800, 600
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Player and Boss Game")

player_image = pygame.Surface((50, 50))
player_image.fill((0, 255, 0))  # 绿色玩家

boss_image = pygame.Surface((50, 50))
boss_image.fill((255, 0, 0))  # 红色Boss

player_rect = player_image.get_rect()
player_rect.x=100
player_rect.y=100
boss_rect = boss_image.get_rect()

player_speed = 10
boss_speed = 2

boss_attack_timer = 0
boss_attack_interval = 1000  # 每隔1秒发动一次攻击

running = True
while running:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed

    # Boss 距离玩家的曼哈顿距离
    distance_x = abs(player_rect.x - boss_rect.x)
    distance_y = abs(player_rect.y - boss_rect.y)
    manhattan_distance = distance_x + distance_y

    # 只有当曼哈顿距离大于两倍的大小总和时，Boss 才会跟随玩家移动
    if manhattan_distance > 2 * (player_rect.width + boss_rect.width):
        # Boss 跟随玩家移动
        if player_rect.x < boss_rect.x:
            boss_rect.x -= boss_speed
        elif player_rect.x > boss_rect.x:
            boss_rect.x += boss_speed
        if player_rect.y < boss_rect.y:
            boss_rect.y -= boss_speed
        elif player_rect.y > boss_rect.y:
            boss_rect.y += boss_speed

    # Boss 定期发动攻击
    boss_attack_timer += pygame.time.get_ticks()
    if boss_attack_timer > boss_attack_interval:
        # 在这里实现 Boss 攻击逻辑，这里简单地打印信息


        boss_attack_timer = 0

    window.fill((255, 255, 255))
    window.blit(player_image, player_rect)
    window.blit(boss_image, boss_rect)

    pygame.display.update()

pygame.quit()
