import time

# current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970

# Write your code below 👇
def speed_calc_decorator(sinner):
  def wrapper():
    before = time.time()
    sinner()
    after = time.time()
    print(f'function {sinner.__name__} lasted: ',after - before)
  return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

# basicly @speed_calc_decorator do this:
# launch_torpedos = speed_calc_decorator(fast_function)
# print(launch_torpedos)
# # output <function speed_calc_decorator.<locals>.wrapper at 0x0000026C633049A0>
# launch_torpedos()
