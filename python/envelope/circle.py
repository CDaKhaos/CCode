import math
import random
from shape import c_shape, c_point


class c_circle(c_shape):
    def __init__(self, center: list, radius: int):
        self.r = radius
        super().__init__(center[0], center[1])

    def _polygon(self):
        n = 24
        cos_n = math.cos(2.0 * math.pi / n)
        sin_n = math.sin(2.0 * math.pi / n)
        x_base = 0
        y_base = self.r
        lst_point: list = []
        lst_point.append(c_point(x_base, y_base))
        for i in range(1, n):
            tmp_x = x_base
            x_base = tmp_x * cos_n - y_base * sin_n
            y_base = tmp_x * sin_n + y_base * cos_n
            lst_point.append(c_point(x_base, y_base))
        return lst_point

    def _auto_move(self):
        self._move(c_point().rand())


if __name__ == '__main__':
    c = c_circle([400, 400], 35)
    print(c.auto_move())
