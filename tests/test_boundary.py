import pytest
import pymunk

from src.boundary import Boundary
from src.boundary import BoundarySizeError


def test_boundary_create():
    pos = (0, 0)
    size = (100, 20)
    color = (255, 0, 0, 100)
    boundary = Boundary(pos, size, color)
    assert boundary.body.position == pos
    assert boundary.shape.color == color
    assert boundary.shape.elasticity == 0.4
    assert boundary.shape.friction == 0.5
    assert boundary.shape.collision_type == 4


def test_boundary_create_invalid_size():
    pos = (0, 0)
    size = (-100, 20)
    color = (255, 0, 0, 100)
    with pytest.raises(BoundarySizeError):
        Boundary(pos, size, color)


def test_boundary_add_to_space():
    pos = (0, 0)
    size = (100, 20)
    color = (255, 0, 0, 100)
    boundary = Boundary(pos, size, color)
    space = pymunk.Space()
    boundary.add_to_space(space)
    assert boundary.body in space.bodies
    assert boundary.shape in space.shapes
