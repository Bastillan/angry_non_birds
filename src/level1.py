import pygame
import pymunk
from level import Level


# def collide(arbiter, space, data):
#     print('hello')


class Level1(Level):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.create_boundries()
        self.create_structure()
        self.create_targets()
        self.tries = 5
        handler_ball_target = self.space.add_collision_handler(1, 2)
        handler_ball_target.post_solve = self.collide_ball_target
        handler_target_structure = self.space.add_collision_handler(2, 3)
        handler_target_structure.post_solve = self.collide_target_structure
        handler_target_boundries = self.space.add_collision_handler(2, 4)
        handler_target_boundries.post_solve = self.collide_target_boundries

    def collide_ball_target(self, arbiter, space, data):
        ball_shape, target_shape = arbiter.shapes
        self.space.remove(target_shape, target_shape.body)
        self.number_of_targets -= 1

    def collide_target_structure(self, arbiter, space, data):
        target_shape, structure_shape = arbiter.shapes
        if arbiter.total_ke > 1000000:
            self.space.remove(target_shape, target_shape.body)
            self.number_of_targets -= 1

    def collide_target_boundries(self, arbiter, space, data):
        target_shape, boundries_shape = arbiter.shapes
        if arbiter.total_ke > 1000000:
            self.space.remove(target_shape, target_shape.body)
            self.number_of_targets -= 1

    def create_boundries(self):
        rects = [
            [(self.width/2, self.height-10), (self.width, 20)]
        ]

        for pos, size in rects:
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position = pos
            shape = pymunk.Poly.create_box(body, size)
            shape.elasticity = 0.4
            shape.friction = 0.5
            shape.collision_type = 4
            self.space.add(body, shape)

    def create_structure(self):
        BROWN = (139, 69, 19, 100)
        floor = 20
        rects = [
            [(self.width-300, self.height-50-floor), (20, 100), BROWN, 50],
            [(self.width-400, self.height-50-floor), (20, 100), BROWN, 50],
            [(self.width-500, self.height-50-floor), (20, 100), BROWN, 50],
            [(self.width-450, self.height-110-floor), (100, 20), BROWN, 50],
            [(self.width-350, self.height-110-floor), (100, 20), BROWN, 50]

        ]

        for pos, size, color, mass in rects:
            body = pymunk.Body()
            body.position = pos
            shape = pymunk.Poly.create_box(body, size, radius=1)
            shape.color = color
            shape.mass = mass
            shape.elasticity = 0.4
            shape.friction = 0.4
            shape.collision_type = 3
            self.space.add(body, shape)

    def create_targets(self):
        GREEN = (35, 118, 0, 100)
        floor = 20
        targs = [
            [(self.width-450, self.height-floor-20), 20, GREEN, 10],
            [(self.width-450, self.height-floor-140), 20, GREEN, 10],
            [(self.width-700, self.height-floor-80), 20, GREEN, 10]
        ]

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
        return 'level1'
