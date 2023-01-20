import pytest
import pymunk

from src.target import Target
from src.target import (
    TargetRadiusError,
    TargetMassError
)


def test_target_create():
    pos = (100, 50)
    radius = 20
    color = (255, 0, 0, 100)
    mass = 10
    target = Target(pos, radius, color, mass)
    assert target.body.position == pos
    assert target.shape.color == color
    assert target.shape.mass == mass
    assert target.shape.elasticity == 0.4
    assert target.shape.friction == 0.4
    assert target.shape.collision_type == 2


def test_target_create_invalid_radius():
    pos = (0, 0)
    radius = 0
    color = (255, 0, 0, 100)
    mass = 10
    with pytest.raises(TargetRadiusError):
        Target(pos, radius, color, mass)


def test_target_create_invalid_mass():
    pos = (0, 0)
    radius = 100
    color = (255, 0, 0, 100)
    mass = -30
    with pytest.raises(TargetMassError):
        Target(pos, radius, color, mass)


def test_target_add_to_space():
    pos = (0, 0)
    radius = 20
    color = (255, 0, 0, 100)
    mass = 10
    target = Target(pos, radius, color, mass)
    space = pymunk.Space()
    target.add_to_space(space)
    assert target.body in space.bodies
    assert target.shape in space.shapes
