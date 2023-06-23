import math
import random


class c_circle():
    def __init__(self, center: list, radius: int):
        x = center[0] / 2
        y = center[1] / 2
        self.x = random.randint(center[0]-x, center[0]+x)
        self.y = random.randint(center[1]-y, center[1]+y)
        self.r = radius

        pass

    def polygon(self):
        n = 24
        cos_n = math.cos(2.0 * math.pi / n)
        sin_n = math.sin(2.0 * math.pi / n)
        x_base = 0
        y_base = self.r
        lst_point: list = []
        lst_point.append([self.x+x_base, self.y+y_base])
        for i in range(1, n):
            tmp_x = x_base
            x_base = tmp_x * cos_n - y_base * sin_n
            y_base = tmp_x * sin_n + y_base * cos_n
            lst_point.append([int(self.x+x_base), int(self.y+y_base)])
        return lst_point

    def auto_move(self):
        setp = 5
        self.x += random.randint(-setp, setp)
        self.y += random.randint(-setp, setp)
        return self.polygon()


if __name__ == '__main__':
    c = c_circle([400, 400], 35)
    print(c.auto_move())
