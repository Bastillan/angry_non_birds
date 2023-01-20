import pygame
import sys

from src.level import Level
from src.intro import Intro
from src.level1 import Level1
from src.level2 import Level2
from src.level3 import Level3
from src.credits import Credits


class WindowSizeError(Exception):
    def __init__(self) -> None:
        super().__init__("Window's size has to have positive dimensions")


class FpsError(Exception):
    def __init__(self) -> None:
        super().__init__("Fps has to be positive")


class Game:
    """
    Class Game.
    Contains attributes:

    :param window: pygame's window
    :type window: pygame.Surface

    :param fps: number of fps
    :type fps: int

    :param dt: delta time
    :type dt: float

    :param level: curent level of the game
    :type level: str

    :param run: False if game should stop
    :type run: bool

    :param levels: all levels of the game
    :type levels: dict[str, GameStage]
    """
    def __init__(self, width=1500, height=800, fps=60) -> None:
        """
        Creates instance of the Game.
        Raises WindowsSizeError if width or height is not positive.
        Raises FpsError if fps is not positive
        """
        if width <= 0 or height <= 0:
            raise WindowSizeError
        if fps <= 0:
            raise FpsError

        pygame.init()
        self._window = pygame.display.set_mode((width, height))
        self._fps = fps
        self._dt = 1 / self.fps
        self._level = 'intro'
        self._run = True
        self._prepare_levels()

    def _prepare_levels(self) -> None:
        """Creates dict of all levels of the game."""
        intro = Intro(self.window)
        level1 = Level1(self.window)
        level2 = Level2(self.window)
        level3 = Level3(self.window)
        creditsDefeat = Credits(self.window, 'Defeat')
        creditsVictory = Credits(self.window, 'Victory')
        self._levels = {
            'intro': intro,
            'level1': level1,
            'level2': level2,
            'level3': level3,
            'creditsDefeat': creditsDefeat,
            'creditsVictory': creditsVictory
            }

    def play(self) -> None:
        """Runs game loop."""
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
                    self._run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if isinstance(current_level, Level):
                        self._level = current_level.action(event, line)
                    else:
                        self._level = current_level.action(event)

            if isinstance(current_level, Level):
                current_level.draw(line)
                current_level.space.step(self.dt)
            else:
                current_level.draw()
            clock.tick(self.fps)

        pygame.quit()
        sys.exit()

    @property
    def window(self) -> pygame.Surface:
        """Returns game's window."""
        return self._window

    @property
    def fps(self) -> int:
        """Returns fps."""
        return self._fps

    @property
    def dt(self) -> float:
        """Returns delta time."""
        return self._dt

    @property
    def level(self) -> str:
        """Returns current level."""
        return self._level

    @property
    def run(self) -> bool:
        """Returns run."""
        return self._run

    @property
    def levels(self) -> dict:
        """Returns dict of levels."""
        return self._levels
