import pygame
import random
import numpy as np
import math


class c_node():
    node_count = 1

    def __init__(self, settings, screen):
        # initialize spaceship and its location
        self.id = c_node.node_count
        c_node.node_count += 1
        # print("id:%d" % (self.id))

        self.screen = screen
        self.settings = settings

        self.b_center = False

        # load bmp image and get rectangle
        self.image = pygame.image.load('A.png')
        self.image_center = pygame.image.load('B.png')
        self.rect = self.image.get_rect()
        self.rect_center = self.image_center.get_rect()
        self.screen_rect = screen.get_rect()

        # put spaceship on the bottom of window
        x_offset = random.randint(-settings.pos_offset, settings.pos_offset)
        y_offset = random.randint(-settings.pos_offset, settings.pos_offset)
        self.rect.x = self.screen_rect.centerx + x_offset
        self.rect.y = self.screen_rect.centery + y_offset

    def blitme(self):
        color = 0, 0, 0
        #pygame.draw.circle(self.screen, color, self.get_pos(), self.settings.net_distance, 2)
        # buld the spaceship at the specific location
        if self.b_center == False:
            self.screen.blit(self.image, self.rect)
        else:
            self.screen.blit(self.image_center, self.rect)

    def update(self):
        direction = random.randint(1, 2)
        speed = random.randint(-self.settings.node_speed,
                               self.settings.node_speed)
        if direction == 1:
            self.rect.x += speed
            if self.rect.x > self.screen_rect.right-30:
                self.rect.x = self.screen_rect.right-30
            if self.rect.x < self.screen_rect.left+30:
                self.rect.x = self.screen_rect.left+30
        elif direction == 2:
            self.rect.y += speed
            if self.rect.y > self.screen_rect.bottom-30:
                self.rect.y = self.screen_rect.bottom-30
            if self.rect.y < self.screen_rect.top+30:
                self.rect.y = self.screen_rect.top+30

    def get_pos(self):
        pos = self.rect.centerx, self.rect.centery
        return pos

    def distance(self, other_node):
        np_pos = np.array([self.get_pos()])
        np_other = np.array([other_node.get_pos()])
        pos_off = np_pos - np_other
        dis = math.hypot(pos_off[0][0], pos_off[0][1])
        return dis

    def center_node(self, set_node):
        center_node = ()
        n_len = len(set_node)
        if n_len < 3:
            list_node = list(set_node)
            center_node = list_node[0]
        else:
            np_node = np.zeros(2)
            # find center pos
            for node in set_node:
                np_node = np.array([node.get_pos()]) + np_node
                node.b_center = False
            np_center = np_node / n_len

            # find center node
            min_dis = 9999999999
            for node in set_node:
                np_node = np.array([node.get_pos()])
                pos_off = np_node - np_center
                dis = math.hypot(pos_off[0][0], pos_off[0][1])
                if dis < min_dis:
                    min_dis = dis
                    center_node = node

        return center_node
