"""Class representing a Vec3."""

from dataclasses import dataclass
import math


@dataclass
class Vector3:
    """Class representing a Vec3."""

    x: float
    y: float
    z: float

    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self.x * other, self.y * other, self.z * other)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, (float, int)):
            return self * (1 / other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z
        return self

    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        if not isinstance(other, Vector3):
            raise ValueError(f"{other} is not of type Vector3")
        return all([math.isclose(self.x, other.x), math.isclose(self.y, other.y), math.isclose(self.z, other.z)])

    def length(self) -> float:
        """Get the length of the vector."""
        return math.sqrt(self.length_squared())

    def length_squared(self) -> float:
        """Get the length squared of the vector."""
        return self.x * self.x + self.y * self.y + self.z * self.z

    def dot(self, other: "Vector3") -> float:
        """Compute the dot product with another vector."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector3") -> "Vector3":
        """Compute the cross product with another vector."""
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector3(x, y, z)

    def unit(self) -> "Vector3":
        """Get a normalized vector."""
        return self / self.length()

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        raise IndexError(f"{index} is too high for Vector3")

    def __repr__(self):
        return f"Vector3({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"


class Point(Vector3):
    """Class representing a point.

    An alias to Vector3.
    """

    pass
