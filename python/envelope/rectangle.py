import math
import random
from shape import c_shape, c_point


class c_rectangle(c_shape):
    def __init__(self, center: list, width: int, heigh: int):
        self.w = width
        self.h = heigh
        super().__init__(center[0], center[1])

    def _polygon(self):
        lst_point: list = []
        x = int(self.w / 2)
        y = int(self.h / 2)
        lst_point.append(c_point(-x, -y))
        lst_point.append(c_point(x, -y))
        lst_point.append(c_point(x, y))
        lst_point.append(c_point(-x, y))
        return lst_point

    def _auto_move(self):
        self._move(c_point().rand())
        self._rotate(random.randint(1, 10))


if __name__ == '__main__':
    c = c_rectangle([400, 400], 40, 50)
    print(c.auto_move())
