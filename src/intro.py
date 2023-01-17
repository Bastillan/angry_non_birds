import pygame
from src.gameStage import GameStage


class Intro(GameStage):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.wall_color = 'blue'

    def action(self, event: pygame.event.Event):
        level = super().action(event)
        if level == 'next_level':
            return 'level1'
        return 'intro'
