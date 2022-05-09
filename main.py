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

# Objects
# Hitbox
Hitbox_Movement = input.Movement()
Hitbox = output.Player(100, 100, 90, 100)

# Run until user asks to quit loop
running = True
while running:
    pygame.time.delay(25)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw
    # Background
    screen.fill((150, 150, 150))

    # Draw Player
    Hitbox.p_angle == Hitbox_Movement.angle
    Hitbox.Draw_internal_player(screen)

    pygame.display.flip()

# Quit
pygame.quit()

# Assistant code credit: https://stackoverflow.com/questions/18179877/pygame-rotating-a-line