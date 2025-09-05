"""Run pytracer."""

import math
from pathlib import Path

from pytracer.color import Color
from pytracer.ray import Ray
from pytracer.vector3 import Point, Vector3


def hit_sphere(center: Point, radius: float, ray: Ray):
    """Check if a ray hits a sphere."""
    oc = center - ray.origin
    a = ray.direction.length_squared()
    h = Vector3.dot(ray.direction, oc)
    c = oc.length_squared() - (radius * radius)
    discriminant = (h * h) - (a * c)

    if discriminant < 0:
        return -1.0
    else:
        return (h - math.sqrt(discriminant)) / a


def lerp(a, b, alpha):
    """Linear interpolation between two values."""
    return ((1 - alpha) * a) + (alpha * b)


def ray_color(ray: Ray) -> Color:
    """Get the color for a given ray."""
    t = hit_sphere(Point(0, 0, -1), 0.5, ray)
    if t > 0.0:
        normal = ray.at(t) - Vector3(0, 0, -1)
        normal_unit = normal.unit()
        color_vector = Vector3(normal_unit.x + 1, normal_unit.y + 1, normal_unit.z + 1) * 0.5
        color = Color(color_vector.x, color_vector.y, color_vector.z)
        return color

    a = 0.5 * (ray.direction.unit().y + 1.0)
    return Color(*lerp(Color(1.0, 1.0, 1.0), Color(0.5, 0.7, 1.0), a))


def main():
    """Run pytracer."""
    ASPECT_RATIO = 16.0 / 9.0
    IMAGE_WIDTH = 400
    _image_height = int(IMAGE_WIDTH / ASPECT_RATIO)
    IMAGE_HEIGHT = _image_height if _image_height > 1 else 1

    VIEWPORT_HEIGHT = 2.0
    VIEWPORT_WIDTH = VIEWPORT_HEIGHT * (IMAGE_WIDTH / IMAGE_HEIGHT)

    MAX_COLOR = 255

    # Camera
    focal_length = 1.0
    camera_center = Point(0, 0, 0)

    viewport_u = Vector3(VIEWPORT_WIDTH, 0, 0)
    viewport_v = Vector3(0, -VIEWPORT_HEIGHT, 0)

    pixel_delta_u = viewport_u / IMAGE_WIDTH
    pixel_delta_v = viewport_v / IMAGE_HEIGHT

    # Calculate location of upper left pixel
    viewport_upper_left = camera_center - Vector3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2
    upper_pixel_location = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

    lines = ["P3", f"{IMAGE_WIDTH} {IMAGE_HEIGHT}", str(MAX_COLOR)]
    for j in range(IMAGE_HEIGHT):
        for i in range(IMAGE_WIDTH):
            pixel_center = upper_pixel_location + (i * pixel_delta_u) + (j * pixel_delta_v)
            ray_direction = pixel_center - camera_center
            ray = Ray(camera_center, ray_direction)
            color = ray_color(ray)
            lines.append(str(color))

            # r = i / IMAGE_WIDTH
            # g = j / IMAGE_HEIGHT
            # b = 0.0
            # color = Color(r, g, b)

            # lines.append(str(color))

    image_file = Path.cwd() / "image.ppm"
    image_file.write_text("\n".join(lines))
    print(f"Image written to {image_file}")


if __name__ == "__main__":
    main()
