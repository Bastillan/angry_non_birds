import pygame
from src.credits import Credits


class CreditsDefeat(Credits):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.text = 'Defeat'
