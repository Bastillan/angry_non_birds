from credits import Credits
import pygame


class CreditsVictory(Credits):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.text = 'Victory'
