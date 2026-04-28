# TODO how to make branch in git, not fork but branch for disposable tests
# TODO how to make it faster, maybe threading, nope better will be use multiprocessing

import os, pathlib
from prettytable import PrettyTable
import subprocess as sub
import time as t
from multiprocessing import Pool, cpu_count

current_drive_ = pathlib.Path.cwd().drive
current_path_ = pathlib.Path.cwd()
directory_list = os.listdir()
chosen_path = ''
ignore_list = ["build",".idea",".venv","dist","static","templates"]
ignore_list_ = ",".join(ignore_list)
ignore_tuple = ('.','idea','env','venv','build','dist','data','images','chrome_profile','Extensions')
old_file_to_rem = ""

basic_data = PrettyTable()
info_print = PrettyTable()
dir_list = PrettyTable()
basic_data.header = True
list_ = [current_drive_,current_path_]
basic_data.field_names = ["Current drive", "Current Path"]
basic_data.add_row(list_)
print(basic_data)

info_print.header = False
info_print.add_row(["Type your path to scan without quotes"])
print(info_print)

def iter_check_it(_list_):
  print("------ LOADING  ---------")
  start_time = t.time()
  list_ = _list_
  for dir in list_:
    full_path_to_dir = pathlib.PurePath(chosen_path) / f'{dir}'
    if os.path.isdir(full_path_to_dir) and not dir.startswith(ignore_tuple):
      files = [f for f in os.listdir(full_path_to_dir) if os.path.isfile(f)]
      for file in files:
        file_to_remove = pathlib.Path(full_path_to_dir) / f'{old_file_to_rem}'
        if os.path.exists(file_to_remove):
          print(f"[INFO] found {old_file_to_rem} in\npath: {full_path_to_dir}\n"
                f"[INFO] removing {old_file_to_rem}")
          os.remove(file_to_remove)
        full_path_to_file = pathlib.PurePath(full_path_to_dir) / f'{file}'
        if os.path.isfile(full_path_to_file) and file.endswith('.py'):
          print(f'[INFO] Found Python file(s) in\n'
                f'[INFO] {full_path_to_dir}'
                f'[INFO] generating requirements.txt file')
          sub.run(["pipreqs",f"{full_path_to_dir}", "--ignore", ignore_list_, "--force"], capture_output=True, shell=False)
  spent_time = t.time() - start_time
  if spent_time < 60:
    print(f"task lasted: {spent_time}")
  else:
    min = spent_time//60
    sec = spent_time%60
    print(f"min: {min}, sec: {sec}")
  input(f"------ COMPLETED  ---------"
        f"press any key to quit ")

def check_it():
  print("------ LOADING  ---------")
  start_time = t.time()
  for dir in directory_list:
    full_path_to_dir = pathlib.PurePath(chosen_path) / f'{dir}'
    if os.path.isdir(full_path_to_dir) and not dir.startswith(ignore_tuple):
      files = [f for f in os.listdir(full_path_to_dir) if os.path.isfile(f)]
      for file in files:
        file_to_remove = pathlib.Path(full_path_to_dir) / f'{old_file_to_rem}'
        if os.path.exists(file_to_remove):
          print(f"[INFO] found {old_file_to_rem} in\npath: {full_path_to_dir}\n"
                f"[INFO] removing {old_file_to_rem}")
          os.remove(file_to_remove)
        full_path_to_file = pathlib.PurePath(full_path_to_dir) / f'{file}'
        if os.path.isfile(full_path_to_file) and file.endswith('.py'):
          print(f'[INFO] Found Python file(s) in\n'
                f'[INFO] {full_path_to_dir}'
                f'[INFO] generating requirements.txt file')
          sub.run(["pipreqs",f"{full_path_to_dir}", "--ignore", ignore_list_, "--force"], capture_output=True, shell=False)
  spent_time = t.time() - start_time
  if spent_time < 60:
    print(f"task lasted: {spent_time}")
  else:
    min = spent_time//60
    sec = spent_time%60
    print(f"min: {min}, sec: {sec}")
  input(f"------ COMPLETED  ---------"
        f"press any key to quit ")

again = True
while again:
  chosen_path = input("Type path: ")
  old_file_to_rem = input("Name of old req file to remove: ")
  try:
    directory_list = os.listdir(chosen_path)
  except OSError as er:
    print(f'Wrong path\n did you mean {chosen_path.replace('"','').replace("'","")}')
    again_ = input("Continue? (y/n)")
    if again_.lower() == 'y':
      again = True
    else:
      print('Bye')
      again = False
  else:
    dir_list.field_names = ["List of files and folders"]
    dir_list.add_row([directory_list])
    print(dir_list)
    if __name__ == "__main__":
      with Pool(processes=cpu_count()) as pool:
        results = pool.map(iter_check_it, directory_list)
    break


