# Import and initialize pygame library
import pygame
pygame.init()

# Internal view
class Player:
    def __init__(self, pX, pY, p_angle):
        self.pX = pX
        self.pY = pY
        self.p_angle = p_angle
    def Draw_internal_player(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pX, self.pY, 20, 20))