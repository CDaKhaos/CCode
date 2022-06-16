import pygame
import random
import pygame

class c_node():
    node_count = 1

    def __init__(self, settings, screen):
        # initialize spaceship and its location
        self.id = c_node.node_count
        c_node.node_count += 1
        # print("id:%d" % (self.id))
        
        self.screen = screen
        self.settings = settings

        # load bmp image and get rectangle
        self.image = pygame.image.load('A.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put spaceship on the bottom of window
        x_offset = random.randint(-settings.pos_offset, settings.pos_offset)
        y_offset = random.randint(-settings.pos_offset, settings.pos_offset)
        self.rect.x = self.screen_rect.centerx + x_offset
        self.rect.y = self.screen_rect.centery + y_offset

    def blitme(self):
        color = 0,0,0
        #pygame.draw.circle(self.screen, color, self.get_pos(), self.settings.net_distance, 2)
        # buld the spaceship at the specific location
        self.screen.blit(self.image, self.rect)

    def update(self):
        direction = random.randint(1, 2)
        speed = random.randint(-self.settings.node_speed,
                               self.settings.node_speed)
        if direction == 1:
            self.rect.x += speed
            if self.rect.x > self.screen_rect.right-30:
                self.rect.x = self.screen_rect.right-30
            if self.rect.x < self.screen_rect.left+30:
                self.rect.x = self.screen_rect.left+30
        elif direction == 2:
            self.rect.y += speed
            if self.rect.y > self.screen_rect.bottom-30:
                self.rect.y = self.screen_rect.bottom-30
            if self.rect.y < self.screen_rect.top+30:
                self.rect.y = self.screen_rect.top+30

    def get_pos(self):
        pos = self.rect.centerx, self.rect.centery
        return pos
