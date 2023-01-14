import pygame
import sys
from level import Level
from intro import Intro
from level1 import Level1
from credits import Credits


class Game:
    def __init__(self, width=1000, height=800, fps=60) -> None:
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        self.fps = fps
        self.dt = 1 / self.fps
        self.level = 'intro'
        self.run = True
        intro = Intro(self.window)
        level1 = Level1(self.window)
        credits = Credits(self.window)
        self.levels = {
            'intro': intro,
            'level1': level1,
            'credits': credits
            }

    def play(self):
        clock = pygame.time.Clock()

        while self.run:
            for event in pygame.event.get():
                current_level = self.levels[self.level]
                if event.type == pygame.QUIT:
                    self.run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.level = current_level.action(event)
                current_level.draw()
                if isinstance(current_level, Level):
                    current_level.space.step(self.dt)
                clock.tick(self.fps)

        pygame.quit()
        sys.exit()


game = Game()
game.play()
