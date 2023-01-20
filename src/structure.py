import pymunk


class StructureSizeError(Exception):
    def __init__(self) -> None:
        super().__init__("Structure's size has to have positive dimensions")


class StructureMassError(Exception):
    def __init__(self) -> None:
        super().__init__("Structure's mass has to be positive")


class Structure:
    """
    Class Structure.
    Contains attributes:

    :param body: structure's simulation body
    :type body: pymunk.Body

    :param shape: structure's simulation shape
    :type shape: pymunk.Poly
    """
    def __init__(self, pos, size, color, mass) -> None:
        """
        Creates instance of the Structure.
        Raises StructureSizeError if one of size's dimensions is not positive.
        Raises StructureMassError if mass is not positive.
        """
        sx, sy = size
        if sx <= 0 or sy <= 0:
            raise StructureSizeError
        if mass <= 0:
            raise StructureMassError

        self._body = pymunk.Body()
        self._body.position = pos
        self._shape = pymunk.Poly.create_box(self._body, size, radius=1)
        self._shape.color = color
        self._shape.mass = mass
        self._shape.elasticity = 0.4
        self._shape.friction = 0.4
        self._shape.collision_type = 3

    def add_to_space(self, space: pymunk.Space) -> None:
        """Adds structure's body and shape to simulation's space."""
        space.add(self.body, self.shape)

    @property
    def body(self) -> pymunk.Body:
        """Returns structure's body."""
        return self._body

    @property
    def shape(self) -> pymunk.Poly:
        """Returns structure's shape."""
        return self._shape
