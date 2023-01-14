import pygame
from gameStage import GameStage


class Intro(GameStage):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.wall_color = 'blue'

    def action(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return 'level1'
        return 'intro'
