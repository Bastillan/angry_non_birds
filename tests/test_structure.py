import pytest
import pymunk

from src.structure import Structure
from src.structure import (
    StructureSizeError,
    StructureMassError
)


def test_structure_create():
    pos = (10, 50)
    size = (100, 20)
    color = (255, 0, 0, 100)
    mass = 10
    structure = Structure(pos, size, color, mass)
    assert structure.body.position == pos
    assert structure.shape.color == color
    assert structure.shape.mass == mass
    assert structure.shape.elasticity == 0.4
    assert structure.shape.friction == 0.4
    assert structure.shape.collision_type == 3


def test_structure_create_invalid_size():
    pos = (0, 0)
    size = (30, 0)
    color = (255, 0, 0, 100)
    mass = 10
    with pytest.raises(StructureSizeError):
        Structure(pos, size, color, mass)


def test_structure_create_invalid_mass():
    pos = (0, 0)
    size = (100, 100)
    color = (255, 0, 0, 100)
    mass = -40
    with pytest.raises(StructureMassError):
        Structure(pos, size, color, mass)


def test_structure_add_to_space():
    pos = (0, 0)
    size = (100, 20)
    color = (255, 0, 0, 100)
    mass = 10
    structure = Structure(pos, size, color, mass)
    space = pymunk.Space()
    structure.add_to_space(space)
    assert structure.body in space.bodies
    assert structure.shape in space.shapes
