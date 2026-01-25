def add(*n):
  """add n int digits, no matters how many"""
  add_result = sum([digit for digit in n])
  return add_result

def add_mine(*n):
  add_list = []
  add_list.append([digit for digit in n])
  add_args = [add_list[0][num] for num in range(0,len(add_list[0]))]
  add_result = 0
  for digit in add_args:
    add_result += digit
  return add_result

print(add(1,2,3,10,300))
print(add_mine(1,2,3,10,300))


def bar(spam, eggs, toast='yes please!', ham=0):
  print(spam, eggs, toast, ham)


bar(1, 2)


def test1(*args):
  print(args)
  print(type(args))


test1(1, 2, 3, 5)


def all_aboard(a, *args, **kw):
  print(a, args, kw)


print(type(all_aboard(4, 7, 3, 0, x=10, y=64)))