import sys
import pygame
from settings import Settings

from abc import ABCMeta, abstractmethod


class game_frame():
    __metaclass__ = ABCMeta

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.screen_caption)

        self.running = True

    def _listen(self):
        # respond to  keyboard and mouse item
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.running = 1-self.running
                self._listen_KeyDown(event.key)

    def _listen_KeyDown(self, event_key):
        pass

    @abstractmethod
    def _update(self):
        pass

    @abstractmethod
    def _draw(self):
        pass

    def run(self):
        while True:
            # fill color
            self.screen.fill(self.settings.bg_color)

            self._listen()

            if self.running:
                self._update()

            self._draw()

            # visualiaze the window
            pygame.display.flip()

            # pygame.time.delay(300)


if __name__ == '__main__':
    g = game()
    g.run()

###############################
# example
# class my_game(game_frame):
    # def __init__(self):
    # super().__init__()
    # self.gc = my_game_calss(self.screen)

    # def _listen_KeyDown(self, event_key):
    # pass

    # def _update(self):
        # self.gc.update()
        # pass
    
    # def _draw(self):
        # self.gc.draw()
        # pass


# if __name__ == '__main__':
    # g = my_game()
    # g.run()

    # def _draw(self):
    # self.gc.update(1)
    # pass


# if __name__ == '__main__':
    # g = my_game()
    # g.run()
