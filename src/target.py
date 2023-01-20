import pymunk


class Target:
    def __init__(self, pos, radius, color, mass) -> None:
        self.body = pymunk.Body()
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.color = color
        self.shape.mass = mass
        self.shape.elasticity = 0.4
        self.shape.friction = 0.4
        self.shape.collision_type = 2

    def add_to_space(self, space: pymunk.Space):
        space.add(self.body, self.shape)
