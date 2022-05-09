# Import and initialize libraries
import math
import pygame
import input
import processing
import output

pygame.init()

# Window
screen = pygame.display.set_mode([900, 750])
pygame.display.set_caption("Raycasting Test")

# Map

# Objects
# Hitbox
Hitbox_Movement = input.Movement()
Hitbox = output.Player(120, 125, Hitbox_Movement.angle, 100)

# Run until user asks to quit loop
running = True
while running:
    pygame.time.delay(20)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        Hitbox_Movement.Rotate_Left()
    if keys[pygame.K_RIGHT]:
        Hitbox_Movement.Rotate_Right()

    # Draw
    # Background
    screen.fill((150, 150, 150))

    # View
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400, 400, 100, 100))

    # Player
    Hitbox = output.Player(120, 125, Hitbox_Movement.angle, 100)
    Hitbox.Draw_internal_player(screen)

    pygame.display.flip()

# Quit
pygame.quit()

# Assistant line rotation code credit: https://stackoverflow.com/questions/18179877/pygame-rotating-a-line
# Map drawing code credit: https://youtu.be/Rt5rEW0jQjw (Don't worry, the requirements for this project inhibit
# me from using most of his actual raycasting code as he has programmed)