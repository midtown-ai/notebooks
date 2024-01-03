import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
PLAYER_SPEED = 5

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chase Game")

# Create player and enemy characters
player = pygame.Rect(50, 50, 40, 40)
enemy = pygame.Rect(700, 500, 40, 40)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the player with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP]:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player.y += PLAYER_SPEED

    # Simple chase logic: Move enemy towards the player
    if player.x < enemy.x:
        enemy.x -= PLAYER_SPEED
    if player.x > enemy.x:
        enemy.x += PLAYER_SPEED
    if player.y < enemy.y:
        enemy.y -= PLAYER_SPEED
    if player.y > enemy.y:
        enemy.y += PLAYER_SPEED

    # Clear the screen
    screen.fill(WHITE)

    # Draw player and enemy
    pygame.draw.rect(screen, (0, 0, 255), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.update()
