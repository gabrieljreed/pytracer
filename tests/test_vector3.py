from pytracer.vector3 import Vector3
import pytest
import math


def test_addition():
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(4, 5, 6)
    assert v1 + v2 == Vector3(5, 7, 9)


def test_subtraction():
    v1 = Vector3(5, 7, 9)
    v2 = Vector3(1, 2, 3)
    assert v1 - v2 == Vector3(4, 5, 6)


def test_scalar_multiplication_left_and_right():
    v = Vector3(1, -2, 3)
    assert v * 2 == Vector3(2, -4, 6)
    assert 2 * v == Vector3(2, -4, 6)


def test_scalar_division():
    v = Vector3(2, 4, 6)
    assert v / 2 == Vector3(1, 2, 3)


def test_elementwise_multiplication_and_division():
    v1 = Vector3(2, 4, 6)
    v2 = Vector3(1, 2, 3)
    assert v1 * v2 == Vector3(2, 8, 18)
    assert v1 / v2 == Vector3(2, 2, 2)


def test_negation():
    v = Vector3(1, -2, 3)
    assert -v == Vector3(-1, 2, -3)


def test_length_and_unit():
    v = Vector3(3, 4, 0)
    assert math.isclose(v.length(), 5.0)
    u = v.unit()
    assert math.isclose(u.length(), 1.0)


def test_dot_product():
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(4, -5, 6)
    assert v1.dot(v2) == (1 * 4 + 2 * (-5) + 3 * 6)  # 12


def test_cross_product():
    v1 = Vector3(1, 0, 0)
    v2 = Vector3(0, 1, 0)
    assert v1.cross(v2) == Vector3(0, 0, 1)  # right-hand rule


def test_inplace_add_and_sub():
    v = Vector3(1, 2, 3)
    v2 = Vector3(4, 5, 6)
    v += v2
    assert v == Vector3(5, 7, 9)
    v -= v2
    assert v == Vector3(1, 2, 3)


def test_repr_and_unpacking_and_indexing():
    v = Vector3(1, 2, 3)
    assert repr(v) == "Vector3(1.000, 2.000, 3.000)"

    x, y, z = v
    assert (x, y, z) == (1, 2, 3)

    assert v[0] == 1
    assert v[1] == 2
    assert v[2] == 3

    with pytest.raises(IndexError):
        _ = v[3]


def test_equality_with_tolerance():
    v1 = Vector3(1.00000000001, 2, 3)
    v2 = Vector3(1.0, 2, 3)
    assert v1 == v2  # should pass with isclose
