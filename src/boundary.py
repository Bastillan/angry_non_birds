import pymunk


class BoundarySizeError(Exception):
    def __init__(self) -> None:
        super().__init__("Boundary's size has to have positive dimensions")


class Boundary:
    def __init__(self, pos, size, color) -> None:
        sx, sy = size
        if sx <= 0 or sy <= 0:
            raise BoundarySizeError

        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        self.shape = pymunk.Poly.create_box(self.body, size)
        self.shape.color = color
        self.shape.elasticity = 0.4
        self.shape.friction = 0.5
        self.shape.collision_type = 4

    def add_to_space(self, space: pymunk.Space):
        space.add(self.body, self.shape)
