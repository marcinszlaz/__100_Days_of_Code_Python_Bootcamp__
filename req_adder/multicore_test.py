import subprocess
from multiprocessing import Pool, cpu_count
import time


def process_folder(folder_info):
  """Ta funkcja wykona się równolegle dla każdego folderu"""
  full_path, output_path = folder_info

  start = time.time()
  # Twoja dopieszczona komenda subprocess
  subprocess.run(
    ["pipreqs", full_path, "--savepath", output_path, "--force", "--use-local"],
    capture_output=True,
    shell=False
  )
  end = time.time()
  return f"Gotowe: {full_path} ({round(end - start, 2)}s)"


if __name__ == "__main__":
  # 1. Przygotuj listę zadań (tuple ze ścieżkami)
  # Wykorzystaj swoją listę first_level_dirs, którą wczoraj zrobiłeś
  tasks = [(os.path.join(base_path, d), os.path.join(base_path, d, "req_new.txt"))
           for d in first_level_dirs]

  print(f"Odpałam robotę na {cpu_count()} rdzeniach... 🚀")

  # 2. Odpalenie basenu procesów
  with Pool(processes=cpu_count()) as pool:
    # map() rozsyła zadania do wolnych rdzeni
    results = pool.map(process_folder, tasks)

  for r in results:
    print(r)

  print("------ COMPLETED ---------")