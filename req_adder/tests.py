import pathlib, os
import subprocess as sub
import time as t
from multiprocessing import Pool, cpu_count

path = "C:\\Dell"
pp = pathlib.PurePath(path).joinpath() / 'drivers'

print(pp)
list_= ["licznik",".nielicznik"]

for l_ in list_:
  if l_.startswith('.'):
    print(l_)

path = pathlib.Path.cwd()
path_ = path.joinpath() / 'zupa'
print(path)
print(path_)

# dir_list = ["../Day_60","../Day_60_","../Day_61"]
# for dl in dir_list:
#   sub.run(["pipreqs",f"{dl}","--savepath",f"{dl + '/req_test.txt'}"],shell=False, capture_output=True)

base_path = "C:\\Users\\BadUser\\PycharmProjects\\100 Days of Code - Bootcamp"
print(base_path)
ignore_tuple = ('.idea','.','.venv','build','dist','data','images','chrome_profile','Extensions')
first_level_dirs = []
for root,dirs,files in os.walk(base_path):
  first_level_dirs = [d for d in dirs if not d.startswith(ignore_tuple)]
  break
print(first_level_dirs)

print('files list: ',os.listdir(),type(os.listdir()))
file = [f for f in os.listdir() if os.path.isfile(f)]
print(file)
is_file_exist = os.path.exists(pathlib.Path.cwd() / 'test.txt')
path_to_file = pathlib.Path.cwd() / 'test.txt'
path= pathlib.Path.cwd()
print(is_file_exist)

if is_file_exist:
  os.remove(path_to_file)

start_time = t.time()
t.sleep(1)
time_spent = t.time() - start_time
print("start_time: ",start_time)
print(f"total_time: {time_spent:.2f}")

print(72%72)
print(72%80)
print(72//60)
time = 128
if time <= 60:
  print('time',time,'seconds')
else:
  min = time//60
  sec = time%60
  print(f'min: {min}, sec: {sec}')

print(128//60)

print('ilosc rdzeni',cpu_count())