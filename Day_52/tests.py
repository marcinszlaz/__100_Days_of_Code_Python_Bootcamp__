import time as t
import random as r
x,y = 0.0,0.0

def rand_time():
  global x,y
  x = r.uniform(1.2, 3)
  y = r.uniform(5.5, 8.5)

  return t.sleep(r.uniform(a=x, b=y))


# for _ in range(r.randint(2, 5)):
#   print(f'loop: {_}')

for _ in range(1,4):
  print(_)

try:
  print(f'2 / 0 = ',2/0)
except Exception as e:
  print(f'[ERROR] {e}')

"""
print('print 1')
t1 = t.time()
print(t1)
rand_time()
print(f'delay between {x} and {y}')
t2= t.time()
print(t2)
if (t2-t1) <= (y-x):
  print(f't2-t1={t2-t1} ; y-x={y-x}')
  print(f'(t2-t1) <= (y-x)')
  print('True')
else:
  print('something went terribly wrong xD')

input("End of experiment, check time delta manually")
"""

