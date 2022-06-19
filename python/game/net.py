import pygame
from node import c_node


class c_net():
    net_id = 1

    def __init__(self, settings, screen):
        self.id = self.net_id
        self.net_id += 1

        self.screen = screen
        self.settings = settings

        self.list_nets = []
        self.list_nodes = []
        for i in range(settings.max_node):
            node = c_node(settings, screen)
            self.list_nodes.append(node)

    def __calc_net__(self):
        self.list_nets.clear()
        index = 0
        set_temp_node = set()
        list_done_id = list()
        
        for node in self.list_nodes:
            if index == self.settings.max_node:
                break
            if (node.id in list_done_id):
                continue
            index += 1
            pos = node.get_pos()
            set_temp_node = set([node])
            list_done_id.append(node.id)
            self.__calc_connect__(node, self.list_nodes, set_temp_node, list_done_id)
            
            #find center node
            center_node = node.center_node(set_temp_node)
            center_node.b_center = True
            self.list_nets.append(set_temp_node)

            #print(index, node.id, list_done_id)
        #print("----------------")

    def __calc_connect__(self, node, list_nodes, set_result, list_id):
        pos = node.get_pos()
        for node_next in list_nodes:
            if node.id == node_next.id:
                continue
            pos_next = node_next.get_pos()
            if node.distance(node_next) < self.settings.net_distance:
                b_calc = node_next.id not in list_id
                set_result.add(node_next)
                list_id.append(node_next.id)
                posx = node_next.get_pos()
                pygame.draw.line(self.screen, [0, 0, 0], pos, posx)
                #print("---%d, %d" %(node.id, node_next.id))
                #print(list_id)
                if b_calc:
                    self.__calc_connect__(node_next, list_nodes, set_result, list_id)
                
    def update(self):
        for node in self.list_nodes:
            node.update()
            node.blitme()
        self.__calc_net__()



