# import colorsys
# import signal
# import time
# from sys import exit

import random
import unicornhathd

total = 5

for i in range(0, total):
  x[i] = random.randint(0,150)
  y[i] = random.randint(0,15)
  s[i] = random.randint(1,10)

try:
  while True:
    for i in range(0, total):
      unicornhathd.set_pixel(x[i], y[i], 0, 0, 0)
      x[i] = (x[i] + s[i]) % 150
      unicornhathd.set_pixel(x[i], y[i], 255, 255, 255)
except KeyboardInterrupt:
  unicornhathd.off
