import pygame
import pymunk
import sys


class GameState():
    def __init__(self) -> None:
        self._state = 'intro'

    @property
    def state(self):
        return self._state

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._state = 'first_level'

        screen.fill((255, 0, 0))
        pygame.display.flip()

    def first_level(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((255, 255, 255))
        draw_ball(ball)
        space.step(1/50)
        pygame.display.update()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'first_level':
            self.first_level()


def create_ball(space):
    body = pymunk.Body(1, 100, body_type=pymunk.Body.DYNAMIC)
    body.position = (400, 0)
    shape = pymunk.Circle(body, 80)
    space.add(body, shape)
    return shape


def draw_ball(ball):
    pos_x = int(ball.body.position.x)
    pos_y = int(ball.body.position.y)
    pygame.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), 80)


# General setup
pygame.init()
clock = pygame.time.Clock()
game_state = GameState()

# Create the display surface
screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

space = pymunk.Space()
space.gravity = (0, 500)
ball = create_ball(space)

while True:
    game_state.state_manager()
    clock.tick(60)
