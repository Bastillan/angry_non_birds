import pygame
import pymunk
from src.level import Level


class Level2(Level):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.create_boundries()
        self.create_targets()
        self.tries = 3

    def create_boundries(self):
        GREY = (70, 75, 92, 100)
        rects = [
            [(self.width/2, self.height-10), (self.width, 20)],
            [(self.width-500, self.height-70), (20, 100)],
            [(self.width-10, self.height*3/4), (20, self.height/2)],
            [(self.width-450, self.height-130), (100, 20)]
        ]

        self.number_of_bodies += len(rects)

        for pos, size in rects:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position = pos
            shape = pymunk.Poly.create_box(body, size)
            shape.color = GREY
            shape.elasticity = 0.4
            shape.friction = 0.5
            shape.collision_type = 4
            self.space.add(body, shape)

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
            body = pymunk.Body()
            body.position = pos
            shape = pymunk.Circle(body, radius)
            shape.color = color
            shape.mass = mass
            shape.elasticity = 0.4
            shape.friction = 0.4
            shape.collision_type = 2
            self.space.add(body, shape)

    def action(self, event: pygame.event.Event, line):
        level = super().action(event, line)
        if level == 'next_level':
            return 'creditsVictory'
        if level == 'creditsDefeat':
            return level
        return 'level2'
