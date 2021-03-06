# Import and initialize pygame library
import math
import pygame
import processing

pygame.init()

# Player Movement
class Movement:
    def __init__(self, angle=-90, pX = 195, pY = 195):
        self.pX = pX
        self.pY = pY
        self.angle = angle
        self.rotation_speed = 5
    def Rotate_Left(self):
        self.angle -= self.rotation_speed
    def Rotate_Right(self):
        self.angle += self.rotation_speed
    def Move_Forwards(self):
        self.pX += math.cos(math.radians(self.angle)) * 1
        self.pY += math.sin(math.radians(self.angle)) * 1
    def Move_Backwards(self):
        self.pX -= math.cos(math.radians(self.angle)) * 1
        self.pY -= math.sin(math.radians(self.angle)) * 1

# Maps
MAP_Templates = (
    '#########'
    '#_______#'
    '#_______#'
    '##______#'
    '#______##'
    '#_______#'
    '#_#__#__#'
    '#_______#'
    '#########'
)
