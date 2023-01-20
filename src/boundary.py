import pymunk


class Boundary:
    def __init__(self, pos, size, color) -> None:
        self.body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self.body.position = pos
        self.shape = pymunk.Poly.create_box(self.body, size)
        self.shape.color = color
        self.shape.elasticity = 0.4
        self.shape.friction = 0.5
        self.shape.collision_type = 4

    def add_to_space(self, space: pymunk.Space):
        space.add(self.body, self.shape)
