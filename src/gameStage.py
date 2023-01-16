import pygame


class GameStage:
    def __init__(self, window: pygame.Surface) -> None:
        self.wall_color = 'white'
        self.window = window
        width, height = pygame.display.get_window_size()
        self.width = width
        self.height = height

    def draw(self):
        self.window.fill(self.wall_color)
        pygame.display.update()

    def action(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            return 'next_level'
        return 'level'
