# Import and initialize pygame library
import math
import pygame
pygame.init()

# Internal view
class Player:
    def __init__(self, pX, pY, p_angle):
        self.pX = pX
        self.pY = pY
        self.p_angle = p_angle
    def Draw_internal_player(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pX, self.pY, 15, 15))
        line_x = self.pX + math.cos(math.radians(0))
        line_y = self.pY + math.sin(math.radians(0))
        pygame.draw.line(screen, (0, 0, 0), (self.pX + 7, self.pY + 7), (self.pX + 7, self.pY + 100), 3)