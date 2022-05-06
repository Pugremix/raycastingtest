# Import and initialize pygame library
import pygame
pygame.init()

# Internal view
class Player:
    def __init__(self, pX, pY):
        self.pX = pX
        self.pY = pY
    def Draw_internal_player(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pX, self.pY, 20, 20))