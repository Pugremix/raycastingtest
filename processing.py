# Import and initialize pygame library
import math
import pygame
pygame.init()

# Ray Distance
class Ray_Calculation():
    Ray_Target = 0
    target_x = pX - math.sin(p_angle)
    target_y = pY + math.cos(p_angle)
# Map
class Map:
    def __init__(self):
        self.grid = 9
        self.size = 45
        self.color = (160, 160, 160)
        self.empty = (100, 100, 100)
    def Calulate(self):
        tile = row * self.grid + col
