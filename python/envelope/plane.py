import math
import random
from shape import c_shape, c_point
from track import c_track


class c_plane(c_shape):
    def __init__(self, center: list, normal_angle: int):
        self.normal = normal_angle

        super().__init__(center[0], center[1])
        self._rotate(normal_angle, False)

        self.track = c_track(self._pt_center)
        self.track.create(5)

    def _polygon(self):
        lst_point: list = []

        lst_point.append(c_point(0, -11))  # head
        lst_point.append(c_point(6, 11))  # right
        lst_point.append(c_point(0, 5))  # tail
        lst_point.append(c_point(-6, 11))  # left

        return lst_point

    def _auto_move(self):
        # self._move(c_point().rand())
        # self._rotate(random.randint(1, 10) )
        pass


if __name__ == '__main__':
    c = c_plane([400, 400], 10)
    c.track_create(5)
    c.track_print()
    c.track_pro()
