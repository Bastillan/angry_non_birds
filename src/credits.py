import pygame
import sys

from src.gameStage import GameStage


class Credits(GameStage):
    """
    Class Credits.
    Inherits after GameStage.
    Contains additional attributes:

    :param text: credits' text
    :type text: str
    """
    def __init__(self, window: pygame.Surface, text='Credits') -> None:
        """
        Creates instance of the Credits.
        """
        super().__init__(window)
        self._wall_color = 'red'
        self._text = text

    def draw(self):
        """Displays Credidts on window."""
        self.window.fill(self.wall_color)
        self.display_text()
        pygame.display.update()

    def display_text(self):
        """Displays credits' text."""
        font = pygame.font.Font(None, 60)
        text = font.render(f'{self.text}', True, (38, 46, 162))
        text_rect = text.get_rect(center=self.window.get_rect().center)
        self.window.blit(text, text_rect)

    def action(self, event: pygame.event.Event):
        """
        Handles events.
        If mouse was clicked ends the program.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()

    @property
    def text(self):
        """Returns credits' text."""
        return self._text
