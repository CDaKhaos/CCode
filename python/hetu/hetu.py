import pygame
from node import c_node, em_yinyang
from settings import Settings


class hetu():
    settings = Settings()
    node_size = 10

    def __init__(self, screen):
        self.screen = screen
        self.centerx = screen.get_rect().centerx
        self.centery = screen.get_rect().centery
        self.lst_node = []
        self.lst_line = []

        self.__init_graph__()
        pass

    def update(self, rotate):
        # center
        pygame.draw.circle(self.screen, hetu.settings.black_color,
                           [self.centerx, self.centery], hetu.node_size, 0)

        # node
        for node in self.lst_node:
            width = node.get_yinyang()
            pygame.draw.circle(self.screen, hetu.settings.black_color,
                               node.get_pos(rotate), hetu.node_size, width)

        # line
        for line in self.lst_line:
            pygame.draw.line(self.screen, hetu.settings.black_color,
                             self.lst_node[line[0]].get_pos(),
                             self.lst_node[line[1]].get_pos())

        # shixing Circle
        # center
        pygame.draw.circle(self.screen, hetu.settings.bg_color,
                           [self.centerx, self.centery], hetu.node_size-1, hetu.node_size-1)

        for node in self.lst_node:
            if node.is_yang():
                pygame.draw.circle(self.screen, c_node.settings.bg_color,
                                   node.get_pos(), hetu.node_size-1, hetu.node_size-1)

        pass

    def __init_graph__(self):
        # center
        self.center_node = c_node(0, 0, em_yinyang.YANG, False)
        # first
        self.lst_node.append(
            node_b := self.center_node.left(em_yinyang.YANG, 1))
        self.lst_node.append(
            node_e := self.center_node.right(em_yinyang.YANG, 1))
        self.lst_line.append([node_b.id, node_e.id])

        self.lst_node.append(node_b := self.center_node.up(em_yinyang.YANG, 1))
        self.lst_node.append(
            node_e := self.center_node.down(em_yinyang.YANG, 1))
        self.lst_line.append([node_b.id, node_e.id])
        # second-up
        node = self.center_node.up(em_yinyang.YIN, 2)
        self.lst_node.append(node)
        self.lst_node.append(node.left(em_yinyang.YIN, 1))
        self.lst_node.append(node_b := node.left(em_yinyang.YIN, 2))
        self.lst_node.append(node.right(em_yinyang.YIN, 1))
        self.lst_node.append(node_e := node.right(em_yinyang.YIN, 2))
        self.lst_line.append([node_b.id, node_e.id])
        node_id1 = node_b.id
        node_id3 = node_e.id
        # second-down
        node = self.center_node.down(em_yinyang.YIN, 2)
        self.lst_node.append(node)
        self.lst_node.append(node.left(em_yinyang.YIN, 1))
        self.lst_node.append(node_b := node.left(em_yinyang.YIN, 2))
        self.lst_node.append(node.right(em_yinyang.YIN, 1))
        self.lst_node.append(node_e := node.right(em_yinyang.YIN, 2))
        self.lst_line.append([node_b.id, node_e.id])
        node_id2 = node_b.id
        node_id4 = node_e.id
        self.lst_line.append([node_id1, node_id2])
        self.lst_line.append([node_id3, node_id4])

        # third-up
        node = self.center_node.up(em_yinyang.YIN, 3, False)
        self.lst_node.append(node_b := node.left(em_yinyang.YIN, 1.5))
        self.lst_node.append(node_e := node.right(em_yinyang.YIN, 1.5))
        self.lst_line.append([node_b.id, node_e.id])

        # third-down
        self.lst_node.append(self.center_node.down(em_yinyang.YANG, 3))

        # third-left
        node = self.center_node.left(em_yinyang.YANG, 3)
        self.lst_node.append(node)
        self.lst_node.append(node_b := node.up(em_yinyang.YANG, 1.5))
        self.lst_node.append(node_e := node.down(em_yinyang.YANG, 1.5))
        self.lst_line.append([node_b.id, node_e.id])

        # third-right
        node = self.center_node.right(em_yinyang.YIN, 3, False)
        self.lst_node.append(node.up(em_yinyang.YIN, 0.5))
        self.lst_node.append(node_b := node.up(em_yinyang.YIN, 1.5))
        self.lst_node.append(node.down(em_yinyang.YIN, 0.5))
        self.lst_node.append(node_e := node.down(em_yinyang.YIN, 1.5))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-up
        node = self.center_node.up(em_yinyang.YANG, 4)
        self.lst_node.append(node)
        self.lst_node.append(node.left(em_yinyang.YANG, 1))
        self.lst_node.append(node.left(em_yinyang.YANG, 2))
        self.lst_node.append(node_b := node.left(em_yinyang.YANG, 3))
        self.lst_node.append(node.right(em_yinyang.YANG, 1))
        self.lst_node.append(node.right(em_yinyang.YANG, 2))
        self.lst_node.append(node_e := node.right(em_yinyang.YANG, 3))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-down
        node = self.center_node.down(em_yinyang.YIN, 4, False)
        self.lst_node.append(node.left(em_yinyang.YIN, 0.5))
        self.lst_node.append(node.left(em_yinyang.YIN, 1.5))
        self.lst_node.append(node_b := node.left(em_yinyang.YIN, 2.5))
        self.lst_node.append(node.right(em_yinyang.YIN, 0.5))
        self.lst_node.append(node.right(em_yinyang.YIN, 1.5))
        self.lst_node.append(node_e := node.right(em_yinyang.YIN, 2.5))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-left
        node = self.center_node.left(em_yinyang.YIN, 4, False)
        self.lst_node.append(node.up(em_yinyang.YIN, 0.5))
        self.lst_node.append(node.up(em_yinyang.YIN, 1.5))
        self.lst_node.append(node.up(em_yinyang.YIN, 2.5))
        self.lst_node.append(node_b := node.up(em_yinyang.YIN, 3.5))
        self.lst_node.append(node.down(em_yinyang.YIN, 0.5))
        self.lst_node.append(node.down(em_yinyang.YIN, 1.5))
        self.lst_node.append(node.down(em_yinyang.YIN, 2.5))
        self.lst_node.append(node_e := node.down(em_yinyang.YIN, 3.5))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-right
        node = self.center_node.right(em_yinyang.YANG, 4)
        self.lst_node.append(node)
        self.lst_node.append(node.up(em_yinyang.YANG, 0.85))
        self.lst_node.append(node.up(em_yinyang.YANG, 1.7))
        self.lst_node.append(node.up(em_yinyang.YANG, 2.55))
        self.lst_node.append(node_b := node.up(em_yinyang.YANG, 3.4))
        self.lst_node.append(node.down(em_yinyang.YANG, 0.85))
        self.lst_node.append(node.down(em_yinyang.YANG, 1.7))
        self.lst_node.append(node.down(em_yinyang.YANG, 2.55))
        self.lst_node.append(node_e := node.down(em_yinyang.YANG, 3.4))
        self.lst_line.append([node_b.id, node_e.id])

        # print(len(self.lst_node))
        # print(self.lst_line)
