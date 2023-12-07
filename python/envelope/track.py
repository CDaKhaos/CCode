import math
import random
from shape import c_shape, c_point


class c_track():
    def __init__(self, pt_start: c_point):
        self.pt_start = pt_start
        pass

    def create(self, track_num):
        self.lst_track: list = []
        pt = self.pt_start
        self.lst_track.append(pt)
        for i in range(1, track_num):
            self.lst_track.append(pt.move(pt.rand(50)))

    def pro(self):
        if len(self.lst_track) < 2:
            return

        pt_prev=self.lst_track[0]
        for pt in self.lst_track[1:]:
            dis=int(pt.distance(pt_prev))

            pt_prev=pt
            print(dis)

    def print(self):
        for pt in self.lst_track:
            pt.print()

if __name__ == '__main__':
    c = c_track(c_point(400, 400))
    c.create(5)
    c.print()
    c.pro()
