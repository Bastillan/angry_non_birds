import pymunk


class Structure:
    def __init__(self, pos, size, color, mass) -> None:
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
