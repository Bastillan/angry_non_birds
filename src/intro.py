import pygame
from src.gameStage import GameStage


class Intro(GameStage):
    """
    Class Intro.
    Inherits after GameStage.
    Contains additional attributes:

    :param background: background image
    :type background: pygame.Surface
    """
    def __init__(self, window: pygame.Surface) -> None:
        """
        Creates instance of the Intro.
        Sets background image.
        """
        super().__init__(window)
        self._background = pygame.image.load('img/intro_image.png')

    def draw(self):
        """Displays Intro on window."""
        self.window.blit(self.background, (0, 0))
        pygame.display.update()

    def action(self, event: pygame.event.Event):
        """
        Handles events.
        Returns 'level1' if mouse was clicked otherwise eturns 'intro.'
        """
        level = super().action(event)
        if level == 'next_level':
            return 'level1'
        return 'intro'

    @property
    def background(self) -> pygame.Surface:
        """Returns background image."""
        return self._background
