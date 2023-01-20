import pymunk


class BoundarySizeError(Exception):
    def __init__(self) -> None:
        super().__init__("Boundary's size has to have positive dimensions")


class Boundary:
    """
    Class Boundary.
    Contains attributes:

    :param body: boundary's simulation body
    :type body: pymunk.Body

    :param shape: boundary's simulation shape
    :type shape: pymunk.Poly
    """
    def __init__(self, pos, size, color) -> None:
        """
        Creates instance of the Boundary.
        Raises BoundarySizeError if one of size's dimensions is not positive.
        """
        sx, sy = size
        if sx <= 0 or sy <= 0:
            raise BoundarySizeError

        self._body = pymunk.Body(body_type=pymunk.Body.STATIC)
        self._body.position = pos
        self._shape = pymunk.Poly.create_box(self._body, size)
        self._shape.color = color
        self._shape.elasticity = 0.4
        self._shape.friction = 0.5
        self._shape.collision_type = 4

    def add_to_space(self, space: pymunk.Space) -> None:
        """Adds boundary's body and shape to simulation's space."""
        space.add(self.body, self.shape)

    @property
    def body(self) -> pymunk.Body:
        """Returns boundary's body."""
        return self._body

    @property
    def shape(self) -> pymunk.Poly:
        """Returns boundary's shape."""
        return self._shape
