from functools import wraps

# def dodawanie(x: int,y: int)->int:
#   """dodawamy xD"""
#   return x + y

def decorator(f):
  @wraps(f)
  def wrapper(*args):
    print('wynik dodawania: ')
    result = f(*args)
    print(result)
    return result
  return wrapper

# dodawanie = decorator(dodawanie)
# dodawanie(5,5)
# print(id(dodawanie(5,5)))
#
# id(decorator(dodawanie(5,5)))
# print(id(decorator(dodawanie(5,5))))

@decorator
def dodawanie(x: int,y: int)->int:
  """dodawamy xD"""
  return x + y
dodawanie(5,5)
# print(id(dodawanie(5,5)))

