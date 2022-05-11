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
class Player:
    def __init__(self, pX, pY, p_angle):
        self.pX = pX
        self.pY = pY
        self.p_angle = p_angle
    def internal_player(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pX, self.pY, 15, 15))
        print("starting loop")
        for sight in range(1, 5):
            line_x = self.pX + 7 + math.cos(math.radians(self.p_angle)) * (sight * 45)
            line_y = self.pY + 7 + math.sin(math.radians(self.p_angle)) * (sight * 45)
            identify_tile(line_x, line_y)
            pygame.draw.line(screen, (0, 0, 0), (self.pX + 7, self.pY + 7), (line_x, line_y), 3)

# Identify tiles
def identify_tile(line_x, line_y):
    tile_x = line_x / 45
    tile_y = line_y / 45
    print(tile_x, tile_y)
