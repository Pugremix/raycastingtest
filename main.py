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
Hitbox = processing.Player(0, 0, Hitbox_Movement.angle)

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
    screen.fill((20, 20, 20))

    # Map
    Active_MAP = input.MAP_Templates
    Board = output.Map()
    Board.Draw_Map(screen, Active_MAP)

    # View

    # Player
    Hitbox = processing.Player(195, 195, Hitbox_Movement.angle)
    Hitbox.internal_player(screen)
    Hitbox.internal_vision(screen, Active_MAP)

    pygame.display.flip()

# Quit
pygame.quit()

# Assistant line rotation code credit: https://stackoverflow.com/questions/18179877/pygame-rotating-a-line
# Tile mapping code credit: https://www.youtube.com/watch?v=gxyKOGrqPq4&list=PLLfIBXQeu3abhbqWp4yUTYi7hWNOsEpXa&index=1
# (Don't worry, the lack of libraries in this example inhibit
# me from using most of the actual raycasting code as he has programmed)