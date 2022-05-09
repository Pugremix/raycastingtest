# Import and initialize pygame library
import math
import pygame
pygame.init()

class Movement:
    def __init__(self, angle=-90):
        self.angle = angle
        self.rotation_speed = 4
    def Rotate_Left(self):
        self.angle -= self.rotation_speed
    def Rotate_Right(self):
        self.angle += self.rotation_speed
