import pymunk


class TargetRadiusError(Exception):
    def __init__(self) -> None:
        super().__init__("Target's radius has to be positive")


class TargetMassError(Exception):
    def __init__(self) -> None:
        super().__init__("Target's mass has to be positive")


class Target:
    """
    Class Target.
    Contains attributes:

    :param body: target's simulation body
    :type body: pymunk.Body

    :param shape: target's simulation shape
    "type shape: pymunk.Circle
    """
    def __init__(self, pos, radius, color, mass) -> None:
        """
        Creates instance of the Target.
        Raises TargetRadiusError if radius is not positive.
        Raises TargetMassError if mass is not positive.
        """
        if radius <= 0:
            raise TargetRadiusError
        if mass <= 0:
            raise TargetMassError

        self._body = pymunk.Body()
        self._body.position = pos
        self._shape = pymunk.Circle(self._body, radius)
        self._shape.color = color
        self._shape.mass = mass
        self._shape.elasticity = 0.4
        self._shape.friction = 0.4
        self._shape.collision_type = 2

    def add_to_space(self, space: pymunk.Space):
        """Adds target's body and shape to simulation's space."""
        space.add(self.body, self.shape)

    @property
    def body(self) -> pymunk.Body:
        """Returns target's body."""
        return self._body

    @property
    def shape(self) -> pymunk.Circle:
        """Returns target's shape."""
        return self._shape
