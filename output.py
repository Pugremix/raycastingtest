# Import and initialize pygame library
import math
import pygame

pygame.init()

# Internal view
# Map
class Map:
    def __init__(self):
        self.grid = 9
        self.size = 45
        self.color = (160, 160, 160)
        self.empty = (100, 100, 100)
    def Draw_Map(self, screen, map):
        for row in range(self.grid):
            for col in range(self.grid):
                tile = row * self.grid + col
                pygame.draw.rect(
                    screen, self.color if map[tile] == '#' else
                    self.empty, (col * self.size, row * self.size, self.size - 1, self.size - 1))
# Player
