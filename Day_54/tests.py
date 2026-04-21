import time
import this as isa
import random as r

current_time = time.time()
print(current_time)  # seconds since Jan 1st, 1970

# Write your code below 👇
def speed_calc_decorator(input_function):
  pass

def fast_function():
  for i in range(1000000):
    i * i

def slow_function():
  for i in range(10000000):
    i * i

import pathlib, os

def calc(calc_function,a,b):
  return calc_function(a,b)

def sub(a,b):
  return a-b

result = calc(sub,2,1)
print(result)
print(type(result))

def outer_function():
  print("I\'m outer")
  def nested_function():
    print("I\'m inner")
  return nested_function

# outer_function()
inner = outer_function()
inner()




# path = pathlib.Path.cwd() /__file__
# print(path)
# print(__file__)

# with open(__file__,'r') as file:
#   tests = file.read()
#   print(tests)


print(dir(isa))
print(isa.s)
print(chr(65))
print(chr(97))
for _ in range(65,98):
  print(chr(_))
print(25%26)
print(chr(13))
print(isa)

list_ = [1,2,3,4,5]
print(sum(list_))
def args_func(*args,**kwargs):
  print(args,kwargs)

args_func(1,2,3,raz=1,dwa=2,trzy=3)

print(10*'\n','Exercise 1:')
# TODO: Create the logging_decorator() function 👇
def logging_decorator(function):
  def wrapper(*args):
    print(f"You called {function.__name__}{args}") # args is tuple, *args is unpacked tuple
    result = f"It returned: {function(*args)}"
    return print(result)
  return wrapper

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
  return sum(args)

a_function(1, 2, 3)

def random_number_generator():
  rm = r.randint(0,9)
  return print(rm)

random_number_generator()
