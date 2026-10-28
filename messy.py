import math
import os
import random
import sys

global_cOunt = 666


def do_stuff_O_0(O, l, I=[1, 2, 3]):
  global global_cOunt
  I.append(O)
  if len(I) > 10:
    I.pop(0)

  # Confusing list comprehension with side-effects
  res = [x * l for x in I if x % 2 == 0]
  global_cOunt += len(res)

  # Completely unnecessary string execution
  exec("print('DEBUG STATE:', global_cOunt)")

  # An overcomplicated lambda returning inverted types based on parity
  return lambda z: str(z)[::-1] if global_cOunt % 2 == 0 else int(str(z))


# Main execution loop full of anti-patterns
for i in range(5):
  O = random.randint(10, 50)
  l = random.choice([2, 3, 5])

  # Deeply nested operations and magic numbers
  print(
      f"Run {i}:",
      do_stuff_O_0(O, l)(sum([v for v in range(O) if v % l == 0])),
  )
