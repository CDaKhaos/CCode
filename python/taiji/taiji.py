import pygame
import math
from settings import Settings


class taiji():
    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.centerx = screen.get_rect().centerx
        self.centery = screen.get_rect().centery

        self.big_radius: int = int(self.centery * 0.7)
        self.mid_radius: int = int(self.big_radius / 2)
        self.sml_radius: int = int(self.mid_radius / 4)

        self.pos_yin = [self.centerx, self.centery - self.mid_radius]
        self.pos_yang = [self.centerx, self.centery + self.mid_radius]

        pos1 = self.centerx - self.big_radius, self.centery - self.big_radius
        pos2 = self.centerx, pos1[1]
        pos3 = self.centerx, self.centery + self.big_radius
        pos4 = pos1[0], pos3[1]
        self.pos_polygon = [pos1, pos2, pos3, pos4]

        pass

    def update(self, rotate):
        self.pos_yin = self.rotate(self.pos_yin, rotate)
        self.pos_yang = self.rotate(self.pos_yang, rotate)
        self.pos_polygon = [self.rotate(self.pos_polygon[0], rotate),
                            self.rotate(self.pos_polygon[1], rotate),
                            self.rotate(self.pos_polygon[2], rotate),
                            self.rotate(self.pos_polygon[3], rotate)]
        pass

    def rotate(self, pos, rotate):
        cos_a = math.cos(rotate)
        sin_a = math.sin(rotate)

        tmp_x = pos[0] - self.centerx
        tmp_y = pos[1] - self.centery
        x = tmp_x * cos_a + tmp_y * sin_a
        y = tmp_y * cos_a - tmp_x * sin_a
        return x + self.centerx, y + self.centery

    def draw(self):
        # big circle
        pygame.draw.circle(self.screen, self.settings.black_color,
                           [self.centerx, self.centery], self.big_radius, 0)

        # polygon
        pygame.draw.polygon(
            self.screen, self.settings.bg_color, self.pos_polygon, 0)

        # mid circel
        # mid circle yang
        pygame.draw.circle(self.screen, self.settings.bg_color,
                           self.pos_yang, self.mid_radius, 0)
        # mid circle yin
        pygame.draw.circle(self.screen, self.settings.black_color,
                           self.pos_yin, self.mid_radius, 0)

        # small circle
        # mid circle yin
        pygame.draw.circle(self.screen, self.settings.bg_color,
                           self.pos_yin, self.sml_radius, 0)
        # mid circle yang
        pygame.draw.circle(self.screen, self.settings.black_color,
                           self.pos_yang, self.sml_radius, 0)

        # big circle yang
        pygame.draw.circle(self.screen, self.settings.black_color,
                           [self.centerx, self.centery], self.big_radius, 2)
        pass
