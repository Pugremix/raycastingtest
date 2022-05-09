# Import and initialize pygame library
import math
import pygame
pygame.init()

# Internal view
# Map
MAP = (
    '#########'
    '#_______#'
    '#_______#'
    '#_______#'
    '#_______#'
    '#_______#'
    '#_______#'
    '#_______#'
    '#########'
)
class Map:
    def __init__(self):
        self.grid = 9
        self.size = 45
        self.color = (200, 200, 200)
        self.empty = (100, 100, 100)
    def Draw_Map(self, screen):
        for row in range(self.grid):
            for col in range(self.grid):
                tile = row * self.grid + col
                pygame.draw.rect(
                    screen, self.color if MAP[tile] == '#' else
                    self.empty, (col * self.size, row * self.size, self.size, self.size))
# Player
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