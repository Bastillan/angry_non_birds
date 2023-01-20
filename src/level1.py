import pygame

from src.level import Level
from src.boundary import Boundary
from src.structure import Structure
from src.target import Target


class Level1(Level):
    """
    Class Level1.
    Inherits after Level.
    """
    def __init__(self, window: pygame.Surface) -> None:
        """Creates instance of the Level1."""
        super().__init__(window)
        self.create_boundaries()
        self.create_structure()
        self.create_targets()
        self._tries = 3

    def create_boundaries(self) -> None:
        """Creates boundries for the simulation."""
        GREY = (70, 75, 92, 100)
        rects = [
            [(self.width/2, self.height-10), (self.width, 20), GREY]
        ]

        self._number_of_bodies += len(rects)

        for pos, size, color, in rects:
            boundary = Boundary(pos, size, color)
            boundary.add_to_space(self.space)

    def create_structure(self) -> None:
        """Creates structures for the simulation."""
        BROWN = (139, 69, 19, 100)
        floor = 20
        rects = [
            [(self.width-300, self.height-50-floor), (20, 100), BROWN, 50],
            [(self.width-400, self.height-50-floor), (20, 100), BROWN, 50],
            [(self.width-500, self.height-50-floor), (20, 100), BROWN, 50],
            [(self.width-450, self.height-110-floor), (100, 20), BROWN, 50],
            [(self.width-350, self.height-110-floor), (100, 20), BROWN, 50]
        ]

        self._number_of_bodies += len(rects)

        for pos, size, color, mass in rects:
            structure = Structure(pos, size, color, mass)
            structure.add_to_space(self.space)

    def create_targets(self) -> None:
        """Creates targets for the simulation."""
        GREEN = (35, 118, 0, 100)
        floor = 20
        targs = [
            [(self.width-450, self.height-floor-20), 20, GREEN, 10],
            [(self.width-450, self.height-floor-140), 20, GREEN, 10]
        ]

        self._number_of_bodies += len(targs)
        self._number_of_targets = len(targs)

        for pos, radius, color, mass in targs:
            target = Target(pos, radius, color, mass)
            target.add_to_space(self.space)

    def action(self, event: pygame.event.Event, line) -> str:
        """
        Handles events.
        If parent's function returns 'next_level', returns 'level2'.
        Else if parent's function returns 'creditsDefeat' passes it down.
        Else returns 'level1'.
        """
        level = super().action(event, line)
        if level == 'next_level':
            return 'level2'
        if level == 'creditsDefeat':
            return level
        return 'level1'
