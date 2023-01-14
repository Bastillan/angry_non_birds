import pygame
import pymunk
import pymunk.pygame_util
import math


class Level:
    def __init__(self, window: pygame.Surface) -> None:
        self.wall_color = 'white'
        self.window = window
        width, height = pygame.display.get_window_size()
        self.width = width
        self.height = height
        self.draw_options = pymunk.pygame_util.DrawOptions(self.window)
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.start_ball_pos = None
        self.ball = None
        self.tries = 1

    def draw(self, line):
        self.window.fill(self.wall_color)

        if line:
            pygame.draw.line(self.window, 'black', line[0], line[1], 3)

        self.space.debug_draw(self.draw_options)
        self.show_tries()

        pygame.display.update()

    def show_tries(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text_pos = (10, 10)
        tries = font.render(f'Tries left: {self.tries}', True, (120, 120, 120))
        self.window.blit(tries, text_pos)

    def action(self, event: pygame.event.Event, line):  # : list[tuple(int, int)]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.tries < 1:
                return 'next_level'
            self.tries -= 1
        return 'level'

    def calculate_distance(self, p1, p2):
        return math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)

    def calculate_angle(self, p1, p2):
        return math.atan2(p2[1] - p1[1], p2[0] - p1[0])
