import pymunk


class TargetRadiusError(Exception):
    def __init__(self) -> None:
        super().__init__("Target's radius has to be positive")


class TargetMassError(Exception):
    def __init__(self) -> None:
        super().__init__("Target's mass has to be positive")


class Target:
    def __init__(self, pos, radius, color, mass) -> None:
        if radius <= 0:
            raise TargetRadiusError
        if mass <= 0:
            raise TargetMassError

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
