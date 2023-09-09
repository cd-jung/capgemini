# You have a car, with initial location (0.0, 0.0) in cartesian (x, y) coordinates.
# Given a list of moves in the form [(a1, m1), (a2, m2), ...] where
# a is an angle in degrees (from north) and m is a magnitude or distance, write a function that accepts
# this list and returns the final position. For simplicity the final position's x and y should be
# rounded to 1dp.

import math


def determine_location(
    directions: list[tuple[float, float]]) -> tuple[float, float]:
  # code here! add any support functions/classes as you like
  x = 0.0
  y = 0.0
  for direction in directions:
    degrees = direction[0] * -1 + 90
    length = direction[1]
    x += _get_cos(degrees) * length
    y += _get_sin(degrees) * length

  return (round(x, 1), round(y, 1))


def _degree_2_radians(degrees):
  return degrees * (math.pi / 180)


# to caculate y
def _get_sin(degrees):
  return math.sin(_degree_2_radians(degrees))


# to caculate x
def _get_cos(degrees):
  return math.cos(_degree_2_radians(degrees))
