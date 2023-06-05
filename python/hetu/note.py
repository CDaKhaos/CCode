import pygame
import math
from settings import Settings


class c_node():
    level_gap = 70
    node_id = 0
    settings = Settings()

    def __init__(self, screen, x, y, b_yin, b_id=True):
        self.id = -1
        if b_id:
            self.id = c_node.node_id
            c_node.node_id += 1
        self.screen = screen
        self.centerx = screen.get_rect().centerx
        self.centery = screen.get_rect().centery
        self.x = x
        self.y = y
        self.b_yin = b_yin

    def left(self, yinyang, level, b_id=True):
        return c_node(self. screen, self.level_gap*level, self.y, yinyang, b_id)

    def right(self, yinyang, level, b_id=True):
        return c_node(self. screen, -self.level_gap*level, self.y, yinyang, b_id)

    def up(self, yinyang, level, b_id=True):
        return c_node(self. screen, self.x, -self.level_gap*level, yinyang, b_id)

    def down(self, yinyang, level, b_id=True):
        return c_node(self. screen, self.x, self.level_gap*level, yinyang, b_id)

    def get_pos(self):
        return self.x+self.centerx, self.y+self.centery

    def update(self, rotate):
        v1 = pygame.math.Vector2(self.x, self.y)
        v2 = v1.rotate(rotate)
        self.x = v2[0]
        self.y = v2[1]
        # print(v2)
        pygame.draw.circle(self.screen, [0, 0, 0],
                           [self.x+self.centerx, self.y+self.centery], 10, self.b_yin)

    def updateYin(self):
        if self.b_yin != 0:
            pygame.draw.circle(self.screen, c_node.settings.bg_color,
                               [self.x+self.centerx, self.y+self.centery], 9, 9)
