import pygame
import sys
from src.gameStage import GameStage


class Credits(GameStage):
    def __init__(self, window: pygame.Surface, text='Credits') -> None:
        super().__init__(window)
        self.wall_color = 'red'
        self.text = text

    def draw(self):
        self.window.fill(self.wall_color)
        self.display_text()
        pygame.display.update()

    def display_text(self):
        font = pygame.font.Font(None, 60)
        text = font.render(f'{self.text}', True, (38, 46, 162))
        text_rect = text.get_rect(center=self.window.get_rect().center)
        self.window.blit(text, text_rect)

    def action(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
            sys.exit()
