# What to do!
# Each function below has an instruction on what it should do, and in 
# some cases some doctests to illustrate what it should do (run the doctests 
# with the Run button) but no implementation. Add the implementation,
# you can use any libraries you like (assuming replit supports it). If you'd 
# like to structure your solution with more than just one function (multiple functions, 
# classes etc) feel free to do so. These snippets are small, but please treat them like 
# "real" code :) (comments if appropriate, attention to edge cases etc)

import doctest
from pathlib import Path
from dataclasses import dataclass
import datetime
import math

# ---- 1.
# Write a function that accepts two Paths and returns the portion of the first Path that is not
# common with the second, which is to say portion of the first path starting from where the two
# paths diverged.
# p.s. bonus points for thinking of a better name for this function and its parameters
def relative_to_common_base(path1: Path, path2: Path) -> Path:
  """
  >>> relative_to_common_base(Path('/home/daniel/git/ws/py311/test.yaml'), Path('/home/daniel/git/slippers'))
  PosixPath('ws/py311/test.yaml')
  """
  # edge cases
  if path1 == None:
    return None
  root = Path('/')
  if path2 == None or path1 == root or path2 == root:
    return path1
    
  # loop to find relative part of given paths until it reach to root
  while path2 != root:
    # if it found common part of both, return the rest of the first path
    if path1.is_relative_to(path2):
      return path1.relative_to(path2)
    path2 = path2.parent

  # if the loop reach to root, return the first path itself
  return path1

# ---- 2.
# Write a function that accepts a string as the first parameter, and a 
# list of strings as the second parameter, and returns a string from the 
# list that is "most like" the first string. There are some examples of 
# what "most like" is below, but the choice of algorithm is yours.
def closest_word(word: str, possibilities: list[str]):
  """
  >>> closest_word('potato', ['potato', 'pumpkin'])
  'potato'
  >>> closest_word('arakeat', ['zzzzzzzz', 'parakeet'])
  'parakeet'
  """
  # edge case
  if word == None or len(word) == 0:
    return None
  if possibilities == None or len(possibilities) == 0:
    return None

  diff = -1
  closest = None
  word_dict = _convert_word_2_dict(word)
  for candidate in possibilities:
    # ranking system
    # 1. same word is the closest one.
    if candidate == word:
      return candidate
    candidate_dict = _convert_word_2_dict(candidate)  
    # 2. if none, a word consist of same numbers of alphabets is the closest one.
    # 3. if none, a word has closest numbers of alphabets is the closest one.
    difference = _compare_dicts(word_dict, candidate_dict)
    if diff == -1 or difference < diff:
      diff = difference
      closest = candidate

  return closest

def _convert_word_2_dict(word):
  res = {}
  for letter in word:
    res[letter] = res[letter] + 1 if letter in res else 1
  return res

def _compare_dicts(dict1, dict2):
  diff = 0
  
  for key in dict1:
    if key in dict2:
      diff += abs(dict1[key] - dict2[key])
    else:
      diff += dict1[key]

  for key in dict2:
    if not key in dict1:
      diff += dict2[key]
      
  return diff
    
# ---- 3.
# Pretend there is a vehicle traveling along a path. The path is represented
# by a list of x, y points and a timestamp at that point. The vehicle travels
# in straight lines between those points and passes through each point at
# the corresponding timestamp. Given this list of points and timestamps,
# and a time seconds (relative to the first timestamp), write a function
# that returns the instantaneous speed at that timestamp. For simplicity
# return the speed as a string rounded and zero-padded to 2dp.
@dataclass
class PointInTime:
  x: float
  y: float
  ts: datetime.datetime


def speed_at_time(at_time: float | int, path: list[PointInTime]) -> str:
  """
  >>> now = datetime.datetime.now()
  >>> speed_at_time(10, [PointInTime(x=0, y=0, ts=now), PointInTime(x=0, y=10, ts=now + datetime.timedelta(seconds=20))])
  '0.50'
  """
  # 0. edge cases
  if at_time == None or path == None or len(path) == 0:
    return None
    
  # 1. find two paths at the time
  point1, point2 = _find_two_points_at_time(at_time, path)
  if point1 == None and point2 == None:
    return None
  
  # 2. calculate the distance between two points
  distance = _caculate_distance(point1, point2)
  # 3. calculate the speed : v = s/t
  speed = distance/(point2.ts.timestamp() - point1.ts.timestamp())
  
  return f"{speed:.2f}"

def _find_two_points_at_time(at_time, path):
  beginning_time = path[0].ts.timestamp()
  at_time = beginning_time + at_time
  prev = path[0]
  for i in range(1,len(path)):
    if prev.ts.timestamp() <= at_time and at_time < path[i].ts.timestamp():
      return prev, path[i]
  return None, None

def _caculate_distance(p1, p2):
  return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
  
if __name__ == '__main__':
  doctest.testmod(verbose=True, exclude_empty=True)
