import math
import random
from abc import ABCMeta, abstractmethod


class c_point():
    def __init__(self, _x=0, _y=0):
        self.x = _x
        self.y = _y

    def move(self, pt_move):
        self.x += pt_move.x
        self.y += pt_move.y

    def rand(self):
        setp = 5
        x = random.randint(-setp, setp)
        y = random.randint(-setp, setp)
        return c_point(x, y)

    def x(self):
        return self.x

    def y(self):
        return self.y


class c_shape():
    __metaclass__ = ABCMeta
    id_index = 0

    def __init__(self, centerx, centery):
        self._id = c_shape.id_index
        c_shape.id_index += 1

        self._pt_center = c_point()
        self._lst_polygon = self._polygon()
        self._move(self._get_start_pt(centerx, centery))
        pass

    def get_polygon(self):
        return self._lst_polygon
    
    def get_polygon_lst(self):
        ret_lst : list = [ [pt.x, pt.y] for pt in self._lst_polygon ]
        return ret_lst

    @abstractmethod
    def _polygon(self):
        pass

    @abstractmethod
    def _auto_move(self):
        pass


    def _get_start_pt(self, centerx, centery):
        x = centerx / 2
        y = centery / 2
        start_x = random.randint(centerx-x, centerx+x)
        start_y = random.randint(centery-y, centery+y)
        return c_point(start_x, start_y)

    def _move(self, pt_move: c_point):
        for pt in self._lst_polygon:
            pt.move(pt_move)
        self._pt_center.move(pt_move)

    def _rotate(self, angle):
        direction = random.choice([-1, 0, 1])
        if direction == 0:
            return

        angle = random.randint(0, 5)
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        for pt in self._lst_polygon:
            x_tmp = pt.x - self._pt_center.x
            y_tmp = pt.y - self._pt_center.y
            pt.x = x_tmp * cos_a + \
                (y_tmp * sin_a * direction) + self._pt_center.x
            pt.y = y_tmp * cos_a - \
                (x_tmp * sin_a * direction) + self._pt_center.y
        pass

    def auto_move(self):
        self._auto_move()
        return self.get_polygon_lst()
