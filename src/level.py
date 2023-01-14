import pygame
import pymunk
import pymunk.pygame_util


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

    def draw(self):
        self.window.fill(self.wall_color)
        pygame.display.update()

    def action(self, event: pygame.event.Event, line):  # : list[tuple(int, int)]
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.tries < 1:
                return 'next_level'
            self.tries -= 1
        return 'level'
