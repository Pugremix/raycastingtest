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
Hitbox = processing.Player(Hitbox_Movement.pX, Hitbox_Movement.pY)

# Run until user asks to quit loop
running = True
while running:
    pygame.time.delay(15)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        Hitbox_Movement.Rotate_Left()
    if keys[pygame.K_RIGHT]:
        Hitbox_Movement.Rotate_Right()
    if keys[pygame.K_UP]:
        Hitbox_Movement.Move_Forwards()
    if keys[pygame.K_DOWN]:
        Hitbox_Movement.Move_Backwards()

    # Draw
    # Background
    screen.fill((20, 20, 20))

    # Map
    Active_MAP = input.MAP_Templates
    Board = output.Map()
    Board.Draw_Map(screen, Active_MAP)

    # View

    # Player
    Hitbox = processing.Player(Hitbox_Movement.pX, Hitbox_Movement.pY)
    Hitbox.internal_player(screen)
    Hitbox.internal_vision(screen, Active_MAP, Hitbox_Movement.angle)

    pygame.display.flip()

# Quit
pygame.quit()