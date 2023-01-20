import pygame
import sys
from src.level import Level
from src.intro import Intro
from src.level1 import Level1
from src.level2 import Level2
from src.level3 import Level3
from src.creditsDefeat import CreditsDefeat
from src.creditsVictory import CreditsVictory


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
        level2 = Level2(self.window)
        level3 = Level3(self.window)
        creditsDefeat = CreditsDefeat(self.window)
        creditsVictory = CreditsVictory(self.window)
        self.levels = {
            'intro': intro,
            'level1': level1,
            'level2': level2,
            'level3': level3,
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
                    mouse_pos = pygame.mouse.get_pos()
                    line = [current_level.start_ball_pos, mouse_pos]

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
