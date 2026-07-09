import random as r
import time
win_five = []
win_two = []
def rand_a():
  return r.sample(population=range(1, 51, 1), k=5)
def rand_b():
  return r.sample(population = range(1,13,1), k = 2)
def random_digits()->None:
  global win_five, win_two
  win_five = rand_a()
  win_two = rand_b()
  return None
random_digits()
print('We will try to hit at: ',win_five, win_two)
attempts = 0
start = time.perf_counter()
win_five_ = set(win_five)
win_two_ = set(win_two)
while True:
  attempts += 1
  if win_five_ == set(rand_a()) and win_two_ == set(rand_b()):
    print(f'You have WON! at {attempts} attempt')
    break
  else:
    continue
stop = time.perf_counter()
duration = stop - start
print(f'Time elapsed: {duration:.3f}')