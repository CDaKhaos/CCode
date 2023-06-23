import pygame
from shapely import ops
from shapely import geometry
from settings import Settings
from math import pi
from circle import c_circle


class envelope():
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.centerx = screen.get_rect().centerx
        self.centery = screen.get_rect().centery

        self.sml_radius: int = 30

        self.circles: list = []
        for i in range(10):
            self.circles.append(
                c_circle([self.centerx, self.centery], self.sml_radius))
        pass

    def update(self):
        pass

    def draw(self):
        # convert to geometry
        geoPolygons = []
        for circle in self.circles:
            geoPolygons.append(geometry.Polygon(circle.auto_move()))

        # calc union
        geoPoints = ops.unary_union(geoPolygons)
        if geoPoints.geom_type == 'MultiPolygon':
            # print(list(geoPoints.geoms))
            for geos in list(geoPoints.geoms):
                self.draw_geoPloygon(geos)

        elif geoPoints.geom_type == 'Polygon':
            self.draw_geoPloygon(geoPoints)

        pass

    def draw_geoPloygon(self, geoPolygon):
        if geoPolygon.geom_type != 'Polygon':
            return

        # convert
        lst_draw = []
        lst_draw.append(geoPolygon.exterior.coords[:-1])

        # draw
        for draw in lst_draw:
            pygame.draw.polygon(
                self.screen, self.settings.black_color, draw, 1)
