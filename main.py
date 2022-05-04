import pygame

# This is a sample Python script.

pygame.init()

# Window
screen = pygame.display.set_mode([800, 750])
pygame.display.set_caption("Test")


# Run until user asks to quit loop
running = True
while running:
    pygame.time.delay(25)

    # Did user click the close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
