import pygame
import sys
from gameStage import GameStage


class Credits(GameStage):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.wall_color = 'red'

    def action(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
