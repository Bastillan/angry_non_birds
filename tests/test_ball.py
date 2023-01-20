import pytest
import pymunk

from src.ball import Ball
from src.ball import (
    BallRadiusError,
    BallMassError
)


def test_ball_create():
    pos = (0, 0)
    radius = 20
    color = (255, 0, 0, 100)
    mass = 10
    ball = Ball(pos, radius, color, mass)
    assert ball.body.position == pos
    assert ball.shape.color == color
    assert ball.shape.mass == mass
    assert ball.shape.elasticity == 0.9
    assert ball.shape.friction == 0.4
    assert ball.shape.collision_type == 1


def test_ball_create_invalid_radius():
    pos = (0, 0)
    radius = -100
    color = (255, 0, 0, 100)
    mass = 10
    with pytest.raises(BallRadiusError):
        Ball(pos, radius, color, mass)


def test_ball_create_invalid_mass():
    pos = (0, 0)
    radius = 100
    color = (255, 0, 0, 100)
    mass = 0
    with pytest.raises(BallMassError):
        Ball(pos, radius, color, mass)


def test_ball_add_to_space():
    pos = (0, 0)
    radius = 20
    color = (255, 0, 0, 100)
    mass = 10
    ball = Ball(pos, radius, color, mass)
    space = pymunk.Space()
    ball.add_to_space(space)
    assert ball.body in space.bodies
    assert ball.shape in space.shapes


def test_ball_remove_from_space():
    pos = (0, 0)
    radius = 20
    color = (255, 0, 0, 100)
    mass = 10
    ball = Ball(pos, radius, color, mass)
    space = pymunk.Space()
    ball.add_to_space(space)
    assert ball.body in space.bodies
    assert ball.shape in space.shapes
    ball.remove_from_space(space)
    assert ball.body not in space.bodies
    assert ball.shape not in space.shapes
