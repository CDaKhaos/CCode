import math
from enum import Enum
from settings import Settings


class em_yinyang(Enum):
    YIN = 0
    YANG = 1


class c_node():
    node_id = 0
    settings = Settings()

    def __init__(self, x, y, em_yinyang=em_yinyang.YIN, b_id=True):
        self.id = -1
        if b_id:
            self.id = c_node.node_id
            c_node.node_id += 1
        self.centerx = c_node.settings.screen_width / 2
        self.centery = c_node.settings.screen_height / 2
        self.x = x
        self.y = y
        self.em_yinyang = em_yinyang
        self.level_gap = c_node.settings.level_gap

        self.lst_pos = []
        self.lst_pos.append((x + self.centerx, y + self.centery))
        for i in range(1, 360):  # 1~359
            self.lst_pos.append(self.__rotate(i))
        self.__rotate_angle = 0
        # print(len(self.lst_pos))  # 360

    def left(self, em_yinyang, level, b_id=True):
        return c_node(self.level_gap*level, self.y, em_yinyang, b_id)

    def right(self, em_yinyang, level, b_id=True):
        return c_node(-self.level_gap*level, self.y, em_yinyang, b_id)

    def up(self, em_yinyang, level, b_id=True):
        return c_node(self.x, -self.level_gap*level, em_yinyang, b_id)

    def down(self, em_yinyang, level, b_id=True):
        return c_node(self.x, self.level_gap*level, em_yinyang, b_id)

    def get_pos(self, rotate = 0):
        self.__rotate_angle += rotate
        if self.__rotate_angle > 359:
            self.__rotate_angle -= 359
        return self.lst_pos[self.__rotate_angle]

    def __rotate(self, rotate):
        cos_a = math.cos(rotate)
        sin_a = math.sin(rotate)
        tmp_x = self.x 
        tmp_y = self.y 

        x = tmp_x * cos_a + tmp_y * sin_a + self.centerx
        y = tmp_y * cos_a - tmp_x * sin_a + self.centery
        return x, y

    def get_yinyang(self):
        return self.em_yinyang.value

    def is_yang(self):
        return self.em_yinyang == em_yinyang.YANG


if __name__ == '__main__':
    n = c_node(10, 10, em_yinyang.YIN)
    print(type(n.get_yinyang()))
