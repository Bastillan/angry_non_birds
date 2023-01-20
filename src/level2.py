import pygame
from src.level import Level
from src.boundary import Boundary
from src.target import Target


class Level2(Level):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.create_boundaries()
        self.create_targets()
        self.tries = 3

    def create_boundaries(self):
        GREY = (70, 75, 92, 100)
        rects = [
            [(self.width/2, self.height-10), (self.width, 20), GREY],
            [(self.width-500, self.height-70), (20, 100), GREY],
            [(self.width-10, self.height*3/4), (20, self.height/2), GREY],
            [(self.width-450, self.height-130), (100, 20), GREY]
        ]

        self.number_of_bodies += len(rects)

        for pos, size, color in rects:
            boundary = Boundary(pos, size, color)
            boundary.add_to_space(self.space)

    def create_targets(self):
        GREEN = (35, 118, 0, 100)
        floor = 20
        targs = [
            [(self.width-250, self.height-floor-20), 20, GREEN, 10],
            [(self.width-450, self.height-floor-20), 20, GREEN, 10],
            [(self.width-450, self.height-floor-140), 20, GREEN, 10]
        ]

        self.number_of_bodies += len(targs)
        self.number_of_targets = len(targs)

        for pos, radius, color, mass in targs:
            target = Target(pos, radius, color, mass)
            target.add_to_space(self.space)

    def action(self, event: pygame.event.Event, line):
        level = super().action(event, line)
        if level == 'next_level':
            return 'level3'
        if level == 'creditsDefeat':
            return level
        return 'level2'
