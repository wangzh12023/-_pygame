
keys = pygame.key.get_pressed()

if keys[pygame.K_w]:
    player_pos[1] -= player_speed
if keys[pygame.K_s]:
    player_pos[1] += player_speed
if keys[pygame.K_a]:
    player_pos[0] -= player_speed
if keys[pygame.K_d]:
    player_pos[0] += player_speed

# 玩家攻击
if keys[pygame.K_j]:
    current_time = pygame.time.get_ticks() / 1000
    if current_time - player_last_attack_time > attack_cooldown:
        player_attack_wave.append([player_pos[0] - player_size, player_pos[1],1])
        player_last_attack_time = current_time

if keys[pygame.K_k]:
    current_time = pygame.time.get_ticks() / 1000
    if current_time - player_last_attack_time > attack_cooldown:
        player_attack_wave.append([player_pos[0] + player_size, player_pos[1],2])
        player_last_attack_time = current_time

if keys[pygame.K_i]:
    current_time = pygame.time.get_ticks() / 1000.0
    if current_time - player_last_attack_time > attack_cooldown:
        player_attack_wave.append([player_pos[0], player_pos[1] - player_size,3])
        player_last_attack_time = current_time

if keys[pygame.K_m]:
    current_time = pygame.time.get_ticks() / 1000.0
    if current_time - player_last_attack_time > attack_cooldown:
        player_attack_wave.append([player_pos[0], player_pos[1] + player_size,4])
        player_last_attack_time = current_time

# 更新玩家和BOSS位置
boss_pos[0] += random.choice([-1, 0, 1]) * boss_speed
boss_pos[1] += random.choice([-1, 0, 1]) * boss_speed

# 更新屏幕
screen.fill(BLACK)

# 绘制玩家
pygame.draw.rect(screen, player_color, (player_pos[0], player_pos[1], player_size, player_size))

# 绘制BOSS
pygame.draw.rect(screen, boss_color, (boss_pos[0], boss_pos[1], boss_size, boss_size))

# 处理玩家的攻击波
for attack in player_attack_wave:
    if attack[2]==1:
        attack[0] -= attack_speed
    if attack[2]==2:
        attack[0] += attack_speed
    if attack[2]==3:
        attack[1] -= attack_speed
    if attack[2]==4: 
        attack[1] += attack_speed
    screen.blit(attack_image, (attack[0], attack[1]))

    # 检查是否击中BOSS
    if (
        boss_pos[0] < attack[0] < boss_pos[0] + boss_size
        and boss_pos[1] < attack[1] < boss_pos[1] + boss_size
    ):
        boss_health -= player_attack
        player_attack_wave.remove(attack)