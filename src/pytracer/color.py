"""Class representing a color."""

from pytracer.vector3 import Vector3


class Color(Vector3):
    """Class representing a color."""

    @property
    def r(self) -> float:
        """Get the red component of the color."""
        return self.x

    @property
    def g(self) -> float:
        """Get the green component of the color."""
        return self.y

    @property
    def b(self) -> float:
        """Get the blue component of the color."""
        return self.z

    def __str__(self):
        rbyte = int(255.999 * self.r)
        gbyte = int(255.999 * self.g)
        bbyte = int(255.999 * self.b)
        return f"{rbyte} {gbyte} {bbyte}"
