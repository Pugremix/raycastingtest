# Import and initialize pygame library
import math
import pygame
pygame.init()

# Internal view

class Map:
    def __init__(self):
        self.size

class Player:
    def __init__(self, pX, pY, p_angle, sight):
        self.pX = pX
        self.pY = pY
        self.p_angle = p_angle
        self.sight = sight
    def Draw_internal_player(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pX, self.pY, 15, 15))
        line_x = self.pX + 7 + math.cos(math.radians(self.p_angle)) * self.sight
        line_y = self.pY + 7 + math.sin(math.radians(self.p_angle)) * self.sight
        pygame.draw.line(screen, (0, 0, 0), (self.pX + 7, self.pY + 7), (line_x, line_y), 3)