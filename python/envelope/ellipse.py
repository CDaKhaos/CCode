import math
import random
from shape import c_shape, c_point


class c_ellipse(c_shape):
    def __init__(self, center: list, x_radius: int, y_radius: int):
        self.x_r = x_radius
        self.y_r = y_radius
        super().__init__(center[0], center[1])

    def _polygon(self):
        angle = 0.0
        sides = 24
        increment = 2 * math.pi / sides

        lst_point: list = []
        for i in range(sides):
            x = self.x_r * math.cos(angle)
            y = self.y_r * math.sin(angle)
            angle += increment
            lst_point.append(c_point(int(x), int(y)))

        return lst_point

    def _auto_move(self):
        self._move(c_point().rand())
        self._rotate(random.randint(1, 10))


if __name__ == '__main__':
    c = c_ellipse([400, 400], 35, 10)
    print(c.auto_move())
    print(c.auto_move())
    print(c.auto_move())
