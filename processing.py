# Import and initialize pygame library
import math
import pygame
import output

pygame.init()

# Player
class Player:
    def __init__(self, pX, pY):
        self.pX = pX
        self.pY = pY
    def internal_player(self, screen):
        output.draw_hitbox(screen, self.pX, self.pY)
    def internal_vision(self, screen, map, angle):
        for rays in range(-32, 33):
            sight_range = 45
            current_tile = None
            distance = 0
            distance_mod = 0
            for sight in range(1, sight_range):
                line_x = self.pX + 7 + math.cos(math.radians(angle + (rays * 1))) * (sight * 5)
                line_y = self.pY + 7 + math.sin(math.radians(angle + (rays * 1))) * (sight * 5)
                dist, tile = identify_tile(line_x, line_y, map)
                if dist == '_':
                    distance += 1
                    if not current_tile == tile:
                        distance_mod += 1
                elif dist == '#':
                    break
                if distance == (sight_range - 1):
                    distance_mod = 0
                output.draw_sight(screen, self.pX, self.pY, line_x, line_y)
                output.draw_vision(screen, ((distance * 4.5) - distance_mod), rays)

# Identify tiles
def identify_tile(line_x, line_y, map):
    tile_x = math.trunc(line_x / 45)
    tile_y = math.trunc(line_y / 45)
    tile_num = tile_x + (tile_y * 9)
    tile_contents = map[tile_num]
    # print(tile_x, tile_y, tile_num, tile_contents)
    return tile_contents, tile_num
