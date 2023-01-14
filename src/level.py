import pygame
import pymunk
import pymunk.pygame_util


class Level:
    def __init__(self, window: pygame.Surface) -> None:
        self.wall_color = 'white'
        self.window = window
        self.draw_options = pymunk.pygame_util.DrawOptions(self.window)
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)

    def draw(self):
        self.window.fill(self.wall_color)
        pygame.display.update()

    def action(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return 'next_level'
        return 'level'
