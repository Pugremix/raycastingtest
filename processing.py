# Import and initialize pygame library
import math
import pygame
pygame.init()

# Ray Distance
class Ray_Calculation:
    def __init__(self, pX, pY, p_angle):
        self.grid = 9
        self.size = 45
        self.Ray_Target = 0
        self.target_x = pX - math.sin(p_angle)
        self.target_y = pY + math.cos(p_angle)
