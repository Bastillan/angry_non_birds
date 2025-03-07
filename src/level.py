import pygame
import pymunk
import pymunk.pygame_util
import math

from src.gameStage import GameStage
from src.ball import Ball


class Level(GameStage):
    """
    Class Level.
    Inherits after GameStage.
    Contains additional attributes:

    :param draw_options: draw options for displaying pymunk simulation
    :type draw_options: pymunk.pygame_util.DrawOptions

    :param space: simulation's space
    :type space: pymunk.Space

    :param start_ball_pos: ball's starting position
    :type start_ball_pos: tuple(int, int)

    :param ball: ball
    :type ball: Ball

    :param tries: number of tries
    :type tries: int

    :param number_of_targets: number of targets to hit
    :type number_of_targets: int

    :param number_of_bodies: number of all objects in a simulation
    :type number_of_bodies: int
    """
    def __init__(self, window: pygame.Surface) -> None:
        """Creates instance of the Level."""
        super().__init__(window)
        self._draw_options = pymunk.pygame_util.DrawOptions(self.window)
        self._space = pymunk.Space()
        self._space.gravity = (0, 981)
        self._start_ball_pos = None
        self._ball = None
        self._tries = 1
        self._number_of_targets = 0
        self._number_of_bodies = 0
        self._setup_collision_handlers()

    def _setup_collision_handlers(self) -> None:
        """Setups collision handlers."""
        handler_ball_target = self.space.add_collision_handler(1, 2)
        handler_ball_target.post_solve = self.collide_ball_target
        handler_target_structure = self.space.add_collision_handler(2, 3)
        handler_target_structure.post_solve = self.collide_target_structure
        handler_target_boundries = self.space.add_collision_handler(2, 4)
        handler_target_boundries.post_solve = self.collide_target_boundries

    def draw(self, line) -> None:
        """Displays current Level simulation stage on window."""
        self.window.fill(self.wall_color)

        if line:
            pygame.draw.line(self.window, 'black', line[0], line[1], 3)

        self.space.debug_draw(self.draw_options)
        self._show_number_of_tries()

        pygame.display.update()

    def _show_number_of_tries(self) -> None:
        """Displays number of tries left."""
        font = pygame.font.Font(None, 60)
        text_pos = (10, 10)
        tries = font.render(f'Tries left: {self.tries}', True, (120, 120, 120))
        self.window.blit(tries, text_pos)

    def action(self, event: pygame.event.Event, line) -> str:
        """
        Handles events.
        When mouse is clicked, creates ball.
        When mouse is clicked again throws the ball.
        When mouse is clicked once again deletes the ball
        and all objects outside of window borders.
        During level returns 'level'.
        If level is completed returns 'next_level'
        else if player lost, returns 'creditsDefeat.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not self.ball:
                pos = (300, self.height-200)
                self._ball = self.create_ball(pos)
                self._start_ball_pos = pos
            elif self.start_ball_pos:
                self.ball.body.body_type = pymunk.Body.DYNAMIC
                angle = self._calculate_angle(*line)
                force = self._calculate_distance(*line) * 50
                fx = -math.cos(angle) * force
                fy = -math.sin(angle) * force
                self.ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
                self._start_ball_pos = None
                self._tries -= 1
            else:
                self.ball.remove_from_space(self.space)
                self._ball = None

                self._deleting_objects_outside()

                without_targets = self.number_of_bodies-self.number_of_targets
                if len(self.space.bodies) <= without_targets:
                    return 'next_level'
                elif self.tries < 1:
                    return 'creditsDefeat'
        return 'level'

    def _deleting_objects_outside(self) -> None:
        """
        Deletes from the simulation all objects outside of window borders.
        """
        for shape in self.space.shapes:
            x, y = shape.body.position
            if x < 0 or y < 0 or x > self.width or y > self.height:
                self.space.remove(shape, shape.body)

    def create_ball(self, pos, radius=20, mass=10) -> Ball:
        """Creates ball."""
        RED = (250, 0, 0, 100)
        ball = Ball(pos, radius, RED, mass)
        ball.add_to_space(self.space)
        return ball

    def _calculate_distance(self, p1, p2) -> float:
        """Calculates distance between user's mouse and the ball."""
        return math.sqrt((p2[1]-p1[1])**2 + (p2[0]-p1[0])**2)

    def _calculate_angle(self, p1, p2) -> float:
        """Calculates angle of the throw."""
        return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

    def collide_ball_target(self, arbiter, space, data) -> None:
        """Handles collision between ball and target."""
        ball_shape, target_shape = arbiter.shapes
        self.space.remove(target_shape, target_shape.body)

    def collide_target_structure(self, arbiter, space, data) -> None:
        """Handles collision between target and structure."""
        target_shape, structure_shape = arbiter.shapes
        if arbiter.total_ke > 1000000:
            self.space.remove(target_shape, target_shape.body)

    def collide_target_boundries(self, arbiter, space, data) -> None:
        """Handles collision between target and boundries."""
        target_shape, boundries_shape = arbiter.shapes
        if arbiter.total_ke > 1000000:
            self.space.remove(target_shape, target_shape.body)

    @property
    def draw_options(self) -> pymunk.pygame_util.DrawOptions:
        """Returns draw options."""
        return self._draw_options

    @property
    def space(self) -> pymunk.Space:
        """Returns space."""
        return self._space

    @property
    def start_ball_pos(self):
        """Returns ball's starting position."""
        return self._start_ball_pos

    @property
    def ball(self) -> Ball:
        """Returns ball."""
        return self._ball

    @property
    def tries(self) -> int:
        """Returns number of tries."""
        return self._tries

    @property
    def number_of_targets(self) -> int:
        """Returns number of targets."""
        return self._number_of_targets

    @property
    def number_of_bodies(self) -> int:
        """Returns number of bodies."""
        return self._number_of_bodies
