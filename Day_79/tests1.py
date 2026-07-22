print(type(...))
if ...:
  print(f'class {...} here :-)')

def return_elipsis():
  return ...
print(return_elipsis())

def mutation(lst=[]):
  lst.append(10)
  return lst

mutation()
mutation()
mutation()
print(mutation())

def mutation(lst=None):
  if lst == None:
    lst = []
  lst.append(10)
  return lst

mutation()
mutation()
mutation()
print(mutation())