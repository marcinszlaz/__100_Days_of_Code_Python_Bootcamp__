# with open('a_file1.txt') as file:
#   file.read()
# a_dictionary = {}
'''
try: try this
except: if error occurs handle it
except <error_type> as er: if other error occurs handle it too
else: do it if any errors occurs
finally: do this instead of everything
  raise <errorType eg. KeyError> 'Error optional comment (your comment)' - you can raise your own error :)
'''

try:
  file = open('a_file1.txt')
  a_dictionary = {'key': 'value'}
  print(a_dictionary['key'])
except FileNotFoundError as er:
  print('There was an error, file doesn\'t exist')
  print(er)
  file = open('a_file1.txt','w')
  file.write('Something')
  print('We created file a_file1.txt')
except KeyError as er:
  print(f'Chosen key {er} doesn\'t exist')
  a_dictionary.update({'sfsd':'value2'})
  print(a_dictionary['key'])
  print(a_dictionary['sfsd'])
else:
  fr = file.read()
  print(fr)
finally:
  # raise KeyError 'Dziewczyny lubią w brąz'
  file.close()
  print("file was closed.")

height = 3.1
weight = 67
if height > 3:
  raise ValueError("Human can\'t gow that height")

print('bmi is equal', weight/pow(height,2))