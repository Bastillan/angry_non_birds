import pygame
import pymunk
import pymunk.pygame_util
import math
from level import Level


class Level1(Level):
    def __init__(self, window: pygame.Surface) -> None:
        super().__init__(window)
        self.create_boundries()
        self.create_structure()
        self.tries = 3

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
            self.space.add(body, shape)

    def create_structure(self):
        pass

    def create_ball(self, radius=20, mass=10):
        pos = (300, self.height-200)
        body = pymunk.Body(body_type=pymunk.Body.STATIC)
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.mass = mass
        shape.elasticity = 0.9
        shape.friction = 0.4
        shape.color = (255, 0, 0, 100)
        self.space.add(body, shape)
        return shape

    def draw(self, line):
        self.window.fill(self.wall_color)

        if line:
            pygame.draw.line(self.window, 'black', line[0], line[1], 3)

        self.space.debug_draw(self.draw_options)

        pygame.display.update()

    def calculate_distance(self, p1, p2):
        return math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)

    def calculate_angle(self, p1, p2):
        return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

    def action(self, event: pygame.event.Event, line):
        if self.tries < 1:
            return 'credits'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.ball:
                self.ball = self.create_ball()
                self.start_ball_pos = self.ball.body.position
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

                if self.tries < 1:
                    return 'credits'
        return 'level1'
