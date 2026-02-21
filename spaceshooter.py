pip install pygame
import pygame
import random

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player
player = pygame.Rect(275, 500, 50, 50)
player_speed = 5

# Bullet
bullets = []
bullet_speed = 7

# Enemies
enemies = []
enemy_speed = 3

clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(pygame.Rect(player.x + 20, player.y, 10, 20))

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.x += player_speed

    # Spawn enemies
    if random.randint(1, 30) == 1:
        enemies.append(pygame.Rect(random.randint(0, 550), 0, 50, 50))

    # Update bullets
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Update enemies
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Collision
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
                break

    # Draw player
    pygame.draw.rect(screen, WHITE, player)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, RED, bullet)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (0, 255, 0), enemy)

    # Score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()