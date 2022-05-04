import pygame
pygame.init()

# Window
screen = pygame.display.set_mode([850, 700])
pygame.display.set_caption("Raycasting Test")




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

    pygame.display.flip()

# Quit
pygame.quit()