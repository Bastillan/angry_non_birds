from .credits import Credits
import pygame


class CreditsDefeat(Credits):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.text = 'Defeat'
