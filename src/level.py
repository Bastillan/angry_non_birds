import pygame
import pymunk
import pymunk.pygame_util
import math
from .gameStage import GameStage


class Level(GameStage):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.draw_options = pymunk.pygame_util.DrawOptions(self.window)
        self.space = pymunk.Space()
        self.space.gravity = (0, 981)
        self.start_ball_pos = None
        self.ball = None
        self.tries = 1
        self.number_of_targets = 0
        self.number_of_bodies = 0
        handler_ball_target = self.space.add_collision_handler(1, 2)
        handler_ball_target.post_solve = self.collide_ball_target
        handler_target_structure = self.space.add_collision_handler(2, 3)
        handler_target_structure.post_solve = self.collide_target_structure
        handler_target_boundries = self.space.add_collision_handler(2, 4)
        handler_target_boundries.post_solve = self.collide_target_boundries

    def draw(self, line):
        self.window.fill(self.wall_color)

        if line:
            pygame.draw.line(self.window, 'black', line[0], line[1], 3)

        self.space.debug_draw(self.draw_options)
        self.show_tries()

        pygame.display.update()

    def show_tries(self):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text_pos = (10, 10)
        tries = font.render(f'Tries left: {self.tries}', True, (120, 120, 120))
        self.window.blit(tries, text_pos)

    def action(self, event: pygame.event.Event, line):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.ball:
                pos = (300, self.height-200)
                self.ball = self.create_ball(pos)
                self.start_ball_pos = pos
            elif self.start_ball_pos:
                self.ball.body.body_type = pymunk.Body.DYNAMIC
                angle = self.calculate_angle(*line)
                force = self.calculate_distance(*line) * 50
                fx = -math.cos(angle) * force
                fy = -math.sin(angle) * force
                self.ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
                self.start_ball_pos = None
                self.tries -= 1
            else:
                self.space.remove(self.ball, self.ball.body)
                self.ball = None

                self.deleting_outside()
                if len(self.space.bodies) <= self.number_of_bodies-self.number_of_targets:
                    return 'next_level'
                elif self.tries < 1:
                    return 'creditsDefeat'
        return 'level'

    def deleting_outside(self):
        for shape in self.space.shapes:
            x, y = shape.body.position
            if x < 0 or y < 0 or x > self.width or y > self.height:
                self.space.remove(shape, shape.body)

    def create_ball(self, pos, radius=20, mass=10):
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.mass = mass
        shape.elasticity = 0.9
        shape.friction = 0.4
        shape.collision_type = 1
        shape.color = (255, 0, 0, 100)
        self.space.add(body, shape)
        return shape

    def calculate_distance(self, p1, p2):
        return math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)

    def calculate_angle(self, p1, p2):
        return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

    def collide_ball_target(self, arbiter, space, data):
        ball_shape, target_shape = arbiter.shapes
        self.space.remove(target_shape, target_shape.body)

    def collide_target_structure(self, arbiter, space, data):
        target_shape, structure_shape = arbiter.shapes
        if arbiter.total_ke > 1000000:
            self.space.remove(target_shape, target_shape.body)

    def collide_target_boundries(self, arbiter, space, data):
        target_shape, boundries_shape = arbiter.shapes
        if arbiter.total_ke > 1000000:
            self.space.remove(target_shape, target_shape.body)
