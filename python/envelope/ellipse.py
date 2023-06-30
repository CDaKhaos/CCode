import math
import random


class c_ellipse():
    def __init__(self, center: list, x_radius: int, y_radius: int):
        x = center[0] / 2
        y = center[1] / 2
        self.center_x = random.randint(center[0]-x, center[0]+x)
        self.center_y = random.randint(center[1]-y, center[1]+y)
        self.x_r = x_radius
        self.y_r = y_radius

        self._lst_polygon = self._polygon()

        pass

    def _polygon(self):
        angle = 0.0
        sides = 24
        increment = 2 * math.pi / sides

        lst_point: list = []
        for i in range(sides):
            x = self.x_r * math.cos(angle)
            y = self.y_r * math.sin(angle)
            angle += increment
            lst_point.append([int(x)+self.center_x, int(y)+self.center_y])

        return lst_point

    def _move(self, x, y):
        self._lst_polygon = [[pt[0]+x, pt[1]+y] for pt in self._lst_polygon]
        self.center_x += x
        self.center_y += y

    def _rotate(self, angle):
        direction = random.choice([-1, 0, 1])
        if direction == 0:
            return

        angle = random.randint(0, 5)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        for pt in self._lst_polygon:
            x_tmp = pt[0] - self.center_x
            y_tmp = pt[1] - self.center_y
            pt[0] = x_tmp * cos_a + (y_tmp * sin_a * direction) + self.center_x
            pt[1] = y_tmp * cos_a - (x_tmp * sin_a * direction) + self.center_y
        pass

    def get_polygon(self):
        return self._lst_polygon

    def auto_move(self):
        setp = 5
        x = random.randint(-setp, setp)
        y = random.randint(-setp, setp)
        self._move(x, y)
        self._rotate(10)
        return self.get_polygon()


if __name__ == '__main__':
    c = c_ellipse([400, 400], 35)
    print(c.auto_move())
