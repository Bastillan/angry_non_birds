import pygame
import sys
from level import Level
from intro import Intro
from level1 import Level1
from creditsDefeat import CreditsDefeat
from creditsVictory import CreditsVictory


class Game:
    def __init__(self, width=1500, height=800, fps=60) -> None:
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
        creditsDefeat = CreditsDefeat(self.window)
        creditsVictory = CreditsVictory(self.window)
        self.levels = {
            'intro': intro,
            'level1': level1,
            'creditsDefeat': creditsDefeat,
            'creditsVictory': creditsVictory
            }

    def play(self):
        clock = pygame.time.Clock()

        while self.run:
            current_level = self.levels[self.level]
            if isinstance(current_level, Level):
                line = None
                if current_level.ball and current_level.start_ball_pos:
                    line = [current_level.start_ball_pos, pygame.mouse.get_pos()]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if isinstance(current_level, Level):
                        self.level = current_level.action(event, line)
                    else:
                        self.level = current_level.action(event)
            if isinstance(current_level, Level):
                current_level.draw(line)
                current_level.space.step(self.dt)
            else:
                current_level.draw()
            clock.tick(self.fps)

        pygame.quit()
        sys.exit()
