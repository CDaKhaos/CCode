import math
import random
from shape import c_shape, c_point


class c_fan(c_shape):
    def __init__(self, center: list, radius: int, flare_angle: int, normal_angle: int):
        self.r = radius
        self.flare = int(flare_angle / 2)
        self.normal = normal_angle
        self.for_step = int(self.flare / 10)
        if self.for_step < 2:
            self.for_step = int(self.flare / 2)

        super().__init__(center[0], center[1])
        self._rotate(normal_angle)

    def _polygon(self):
        lst_point: list = []
        lst_point.append(c_point()) # center point

        for i in range(-self.flare, self.flare, self.for_step):
            tmp = i - 90
            x = math.cos(tmp * math.pi / 180) * self.r
            y = math.sin(tmp * math.pi / 180) * self.r
            lst_point.append(c_point(x, y))

        return lst_point

    def _auto_move(self):
        self._move(c_point().rand())
        self._rotate(random.randint(1, 10))
        pass


if __name__ == '__main__':
    c = c_fan([400, 400], 35, 1, 20)
    print(c.auto_move())
