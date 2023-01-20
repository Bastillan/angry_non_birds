import pygame
from src.gameStage import GameStage


class Intro(GameStage):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.background = pygame.image.load('img/intro_image.png')

    def draw(self):
        self.window.blit(self.background, (0, 0))
        pygame.display.update()

    def action(self, event: pygame.event.Event):
        level = super().action(event)
        if level == 'next_level':
            return 'level1'
        return 'intro'
