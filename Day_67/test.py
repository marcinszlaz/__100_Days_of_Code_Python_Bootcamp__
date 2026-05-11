from datetime import date

# print(date.today().strftime('%B %d,%Y'))
# print(type(date.today().strftime('%B %d,%Y')))
print(date.today())
print(type(date.today()))
date_string = (date.today().isoformat())
print(type(date_string))
print((date_string))
date_string_ = '2026-05-09'
print(date.fromisoformat(date_string).strftime('%B %d, %Y'))
print(date.today().fromisoformat(date_string_).strftime('%B %d, %Y'))
iso = "May 10, 2026"


noname_func = lambda: (date.today().strftime('%B %d, %Y'))
print(noname_func())
print(type(noname_func()))
# print((lambda: date.today().strftime('%B %d, %Y'))())

cafes = [{"name": "A", "sockets": 5}, {"name": "B", "sockets": 2}]
sorted_cafes = sorted(cafes, key=lambda cafe: cafe["sockets"])
print(cafes)
print(sorted_cafes)

year  = date.today().year
print(year)