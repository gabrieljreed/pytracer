"""Class representing a ray."""

from pytracer.vector3 import Point, Vector3
from dataclasses import dataclass


@dataclass
class Ray:
    """Class representing a ray."""

    origin: Point
    direction: Vector3

    def at(self, t: float) -> float:
        """Get the value along the ray at a given point."""
        return self.origin + (t * self.direction)
