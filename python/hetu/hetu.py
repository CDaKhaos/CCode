import pygame
from note import c_node
from settings import Settings


class hetu():
    settings = Settings()
    def __init__(self, screen):
        self.screen = screen
        self.centerx = screen.get_rect().centerx
        self.centery = screen.get_rect().centery
        self.lst_node = []
        self.lst_line = []

        # center
        self.center_node = c_node(screen, 0, 0, 0, False)
        # first
        self.lst_node.append(node_b := self.center_node.left(1, 1))
        self.lst_node.append(node_e := self.center_node.right(1, 1))
        self.lst_line.append([node_b.id, node_e.id])

        self.lst_node.append(node_b := self.center_node.up(1, 1))
        self.lst_node.append(node_e := self.center_node.down(1, 1))
        self.lst_line.append([node_b.id, node_e.id])
        # second-up
        node = self.center_node.up(0, 2)
        self.lst_node.append(node)
        self.lst_node.append(node.left(0, 1))
        self.lst_node.append(node_b := node.left(0, 2))
        self.lst_node.append(node.right(0, 1))
        self.lst_node.append(node_e := node.right(0, 2))
        self.lst_line.append([node_b.id, node_e.id])
        node_id1 = node_b.id
        node_id3 = node_e.id
        # second-down
        node = self.center_node.down(0, 2)
        self.lst_node.append(node)
        self.lst_node.append(node.left(0, 1))
        self.lst_node.append(node_b := node.left(0, 2))
        self.lst_node.append(node.right(0, 1))
        self.lst_node.append(node_e := node.right(0, 2))
        self.lst_line.append([node_b.id, node_e.id])
        node_id2 = node_b.id
        node_id4 = node_e.id
        self.lst_line.append([node_id1, node_id2])
        self.lst_line.append([node_id3, node_id4])

        # third-up
        node = self.center_node.up(0, 3, False)
        self.lst_node.append(node_b := node.left(0, 1.5))
        self.lst_node.append(node_e := node.right(0, 1.5))
        self.lst_line.append([node_b.id, node_e.id])

        # third-down
        self.lst_node.append(self.center_node.down(1, 3))

        # third-left
        node = self.center_node.left(1, 3)
        self.lst_node.append(node)
        self.lst_node.append(node_b := node.up(1, 1.5))
        self.lst_node.append(node_e := node.down(1, 1.5))
        self.lst_line.append([node_b.id, node_e.id])

        # third-right
        node = self.center_node.right(0, 3, False)
        self.lst_node.append(node.up(0, 0.5))
        self.lst_node.append(node_b := node.up(0, 1.5))
        self.lst_node.append(node.down(0, 0.5))
        self.lst_node.append(node_e := node.down(0, 1.5))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-up
        node = self.center_node.up(1, 4)
        self.lst_node.append(node)
        self.lst_node.append(node.left(1, 1))
        self.lst_node.append(node.left(1, 2))
        self.lst_node.append(node_b := node.left(1, 3))
        self.lst_node.append(node.right(1, 1))
        self.lst_node.append(node.right(1, 2))
        self.lst_node.append(node_e := node.right(1, 3))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-down
        node = self.center_node.down(0, 4, False)
        self.lst_node.append(node.left(0, 0.5))
        self.lst_node.append(node.left(0, 1.5))
        self.lst_node.append(node_b := node.left(0, 2.5))
        self.lst_node.append(node.right(0, 0.5))
        self.lst_node.append(node.right(0, 1.5))
        self.lst_node.append(node_e := node.right(0, 2.5))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-left
        node = self.center_node.left(0, 4, False)
        self.lst_node.append(node.up(0, 0.5))
        self.lst_node.append(node.up(0, 1.5))
        self.lst_node.append(node.up(0, 2.5))
        self.lst_node.append(node_b := node.up(0, 3.5))
        self.lst_node.append(node.down(0, 0.5))
        self.lst_node.append(node.down(0, 1.5))
        self.lst_node.append(node.down(0, 2.5))
        self.lst_node.append(node_e := node.down(0, 3.5))
        self.lst_line.append([node_b.id, node_e.id])

        # fourth-right
        node = self.center_node.right(1, 4)
        self.lst_node.append(node)
        self.lst_node.append(node.up(1, 0.85))
        self.lst_node.append(node.up(1, 1.7))
        self.lst_node.append(node.up(1, 2.55))
        self.lst_node.append(node_b := node.up(1, 3.4))
        self.lst_node.append(node.down(1, 0.85))
        self.lst_node.append(node.down(1, 1.7))
        self.lst_node.append(node.down(1, 2.55))
        self.lst_node.append(node_e := node.down(1, 3.4))
        self.lst_line.append([node_b.id, node_e.id])

        # print(len(self.lst_node))
        # print(self.lst_line)
        pass

    def update(self, rotate):
        # center
        pygame.draw.circle(self.screen, [0, 0, 0],
                           [self.centerx, self.centery], 10, 0)

        # node
        for node in self.lst_node:
            node.update(rotate)

        # line
        for line in self.lst_line:
            pygame.draw.line(self.screen, [0, 0, 0],
                             self.lst_node[line[0]].get_pos(),
                             self.lst_node[line[1]].get_pos())

        # shixing Circle
        # center
        pygame.draw.circle(self.screen, hetu.settings.bg_color,
                           [self.centerx, self.centery], 9, 9)

        for node in self.lst_node:
            node.updateYin()

        pass
