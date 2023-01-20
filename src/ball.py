import pymunk


class BallRadiusError(Exception):
    def __init__(self) -> None:
        super().__init__("Ball's radius has to be positive")


class BallMassError(Exception):
    def __init__(self) -> None:
        super().__init__("Ball's mass has to be positive")


class Ball:
    """
    Class Ball.
    Contains attributes:

    :param body: ball's simulation body
    :type body: pymunk.Body

    :param shape: ball's simulation shape
    :type shape: pymunk.Circle
    """
    def __init__(self, pos, radius, color, mass) -> None:
        """
        Creates instance of the Ball.
        Raises BallRadiusError if radius is not positive.
        Raises BallMassError if mass is not positive.
        """
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

    def add_to_space(self, space: pymunk.Space) -> None:
        """Adds ball's body and shape to simulation's space."""
        space.add(self.body, self.shape)

    def remove_from_space(self, space: pymunk.Space) -> None:
        """Removes ball's body and shape from simulation's space."""
        space.remove(self.body, self.shape)

    @property
    def body(self) -> pymunk.Body:
        """Returns ball's body."""
        return self._body

    @property
    def shape(self) -> pymunk.Circle:
        """Returns ball's shape."""
        return self._shape
