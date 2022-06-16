import pygame
import numpy as np
import math
from node import c_node

class c_net():
    net_id = 1

    def __init__(self, settings, screen):
        self.id = self.net_id
        self.net_id += 1

        self.screen = screen
        self.settings = settings
        
        self.list_nodes = []
        for i in range(settings.max_node):
            node = c_node(settings, screen)
            self.list_nodes.append(node)
        

    def __calc_net__(self):
        index = 0
        for node in self.list_nodes:
            if index == self.settings.max_node:
                break
            pos = node.get_pos()
            pos_np = np.array([pos])    
            index += 1
            for node_n in self.list_nodes[index:]:
                posx = node_n.get_pos()
                posx_np = np.array([posx])    
                pos_off = posx_np - pos_np
                dis = math.hypot(pos_off[0][0], pos_off[0][1])
                if dis < self.settings.net_distance:
                    pygame.draw.line(self.screen, [0, 0, 0], pos, posx)
                    

    def update(self):
        for node in self.list_nodes:
            node.update()
            node.blitme()

        self.__calc_net__()
