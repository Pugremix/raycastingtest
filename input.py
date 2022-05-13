# Import and initialize pygame library
import math
import pygame
pygame.init()

# Player
class Player:
    def __init__(self, pX, pY, p_angle, sight):
        self.pX = pX
        self.pY = pY
        self.p_angle = p_angle
        self.sight = sight
    def sight(self, screen):
        line_x = self.pX + 7 + math.cos(math.radians(self.p_angle)) * self.sight
        line_y = self.pY + 7 + math.sin(math.radians(self.p_angle)) * self.sight
        pygame.draw.line(screen, (0, 0, 0), (self.pX + 7, self.pY + 7), (line_x, line_y))
# Player Movement
class Movement:
    def __init__(self, angle=-90):
        self.angle = angle
        self.rotation_speed = 4
    def Rotate_Left(self):
        self.angle -= self.rotation_speed
    def Rotate_Right(self):
        self.angle += self.rotation_speed
# Maps
MAP_Templates = (
    '#########'
    '#_______#'
    '#_______#'
    '#_______#'
    '#_______#'
    '#_______#'
    '#__#_#__#'
    '#_______#'
    '#########'
)
