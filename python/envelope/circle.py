import math
import random


class c_circle():
    def __init__(self, center: list, radius: int):
        x = center[0] / 2
        y = center[1] / 2
        self.start_x = random.randint(center[0]-x, center[0]+x)
        self.start_y = random.randint(center[1]-y, center[1]+y)
        self.r = radius

        self._lst_polygon = self._polygon()
        self._move(self.start_x, self.start_y)

        pass

    def _polygon(self):
        n = 24
        cos_n = math.cos(2.0 * math.pi / n)
        sin_n = math.sin(2.0 * math.pi / n)
        x_base = 0
        y_base = self.r
        lst_point: list = []
        lst_point.append([x_base, y_base])
        for i in range(1, n):
            tmp_x = x_base
            x_base = tmp_x * cos_n - y_base * sin_n
            y_base = tmp_x * sin_n + y_base * cos_n
            lst_point.append([int(x_base), int(y_base)])
        return lst_point

    def _move(self, x, y):
        self._lst_polygon = [(pt[0]+x, pt[1]+y) for pt in self._lst_polygon]

    def _rotate(self, angle):
        pass

    def get_polygon(self):
        return self._lst_polygon

    def auto_move(self):
        setp = 5
        x = random.randint(-setp, setp)
        y = random.randint(-setp, setp)
        self._move(x, y)
        return self.get_polygon()


if __name__ == '__main__':
    c = c_circle([400, 400], 35)
    print(c.auto_move())
