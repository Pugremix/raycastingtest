# Import and initialize pygame library
import math
import pygame
import processing

pygame.init()

# Player
class Player:
    def __init__(self, pX, pY):
        self.pX = pX
        self.pY = pY
# Player Movement
class Movement:
    def __init__(self, angle=-90):
        self.angle = angle
        self.rotation_speed = 5
    def Rotate_Left(self):
        self.angle -= self.rotation_speed
    def Rotate_Right(self):
        self.angle += self.rotation_speed
    # def Move_Forwards(self):
        # self.
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
