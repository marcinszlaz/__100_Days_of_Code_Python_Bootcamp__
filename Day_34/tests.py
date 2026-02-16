age: int

age = 'twelve'

def police_check(age: int) -> bool: # TYPE HINT in Python, good thing age: int type of parameter -> bool type of return
  if age > 18:
    can_drive = True
  else:
    can_drive = False
  return can_drive

print(police_check(21))

