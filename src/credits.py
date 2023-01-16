import pygame
import sys
from gameStage import GameStage


class Credits(GameStage):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.wall_color = 'red'
        self.text = 'Credits'

    def draw(self):
        self.window.fill(self.wall_color)
        self.display_text()
        pygame.display.update()

    def display_text(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text_pos = (self.width/2, self.height/2)
        tries = font.render(f'{self.text}', True, (120, 120, 120))
        self.window.blit(tries, text_pos)

    def action(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
