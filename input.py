# Import and initialize pygame library
import math
import pygame
pygame.init()

class Movement:
    def __init__(self, angle=90):
        self.angle = angle
        self.rotation_speed = 5
    def Movement(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.angle -= self.rotation_speed
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.angle += self.rotation_speed
