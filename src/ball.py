import pymunk


class BallRadiusError(Exception):
    def __init__(self) -> None:
        super().__init__("Ball's radius has to be positive")


class BallMassError(Exception):
    def __init__(self) -> None:
        super().__init__("Ball's mass has to be positive")


class Ball:
    def __init__(self, pos, radius, color, mass) -> None:
        if radius <= 0:
            raise BallRadiusError
        if mass <= 0:
            raise BallMassError

        self._body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self._body.position = pos
        self._shape = pymunk.Circle(self._body, radius)
        self._shape.color = color
        self._shape.mass = mass
        self._shape.elasticity = 0.9
        self._shape.friction = 0.4
        self._shape.collision_type = 1

    def add_to_space(self, space: pymunk.Space):
        space.add(self.body, self.shape)

    def remove_from_space(self, space: pymunk.Space):
        space.remove(self.body, self.shape)

    @property
    def body(self) -> pymunk.Body:
        return self._body

    @property
    def shape(self) -> pymunk.Circle:
        return self._shape
