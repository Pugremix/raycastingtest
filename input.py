# Import and initialize pygame library
import math
import pygame
pygame.init()

class Movement:
    def __init__(self, angle=90):
        self.angle = angle
        self.keys = pygame.key.get_pressed()
    def Rotation(self, keys):
        if keys[pygame.K_LEFT]:
            self.angle -= 2
        if keys[pygame.K_RIGHT]:
            self.angle += 2
