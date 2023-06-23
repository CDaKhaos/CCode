from game_frame import game_frame
import pygame
from envelope import envelope


class envelope_game(game_frame):
    def __init__(self):
        super().__init__()
        self.main = envelope(self.screen)

        # fonts = pygame.font.get_fonts()
        self.my_font = pygame.font.SysFont('lato', 24, True)
        self.text_surface = self.my_font.render('speed:', True, "black")

        self.start_time = self.end_time = 0
        self.count_update = 0

    def _listen_KeyDown(self, event_key):
        if event_key == pygame.K_RIGHT:
            pass
        if event_key == pygame.K_LEFT:
            pass
        pass

    def _update(self):
        # start
        if self.start_time == 0:
            self.start_time = pygame.time.get_ticks()

        # update
        self.main.update()

        # end
        self.count_update += 1
        self.end_time = pygame.time.get_ticks()

        # calc time
        calc_count = 2
        if self.end_time - self.start_time > (1000*calc_count):
            self.text_surface = self.my_font.render('test', True, "black")
            self.start_time = 0
            self.count_update = 0
        pass

    def _draw(self):
        self.main.draw()
        # self.screen.blit(self.text_surface, (0, 0))
        pass


if __name__ == '__main__':
    g = envelope_game()
    g.run()
