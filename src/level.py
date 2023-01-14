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

        pygame.display.update()

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
