import pymunk


class StructureSizeError(Exception):
    def __init__(self) -> None:
        super().__init__("Structure's size has to have positive dimensions")


class StructureMassError(Exception):
    def __init__(self) -> None:
        super().__init__("Structure's mass has to be positive")


class Structure:
    def __init__(self, pos, size, color, mass) -> None:
        sx, sy = size
        if sx <= 0 or sy <= 0:
            raise StructureSizeError
        if mass <= 0:
            raise StructureMassError

        self.body = pymunk.Body()
        self.body.position = pos
        self.shape = pymunk.Poly.create_box(self.body, size, radius=1)
        self.shape.color = color
        self.shape.mass = mass
        self.shape.elasticity = 0.4
        self.shape.friction = 0.4
        self.shape.collision_type = 3

    def add_to_space(self, space: pymunk.Space):
        space.add(self.body, self.shape)
