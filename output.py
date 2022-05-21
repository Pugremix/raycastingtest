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
def draw_hitbox(screen, pX, pY):
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(pX, pY, 15, 15))
def draw_sight(screen, pX, pY, line_x, line_y):
    pygame.draw.line(screen, (0, 0, 0), (pX + 7, pY + 7), (line_x, line_y), 3)
# Viewing Spectacle
def draw_vision(screen, darkness, pixel):
    if darkness > 165:
        darkness = 165
    pygame.draw.rect(
        screen, (165 - darkness, 165 - darkness, 165 - darkness), pygame.Rect(420 + (pixel * 10), 480, 10, 195)
    )
