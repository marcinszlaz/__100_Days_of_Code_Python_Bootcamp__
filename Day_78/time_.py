import time


start = time.perf_counter()
time.sleep(2.34)
stop = time.perf_counter()
duration = stop - start
print(f'{duration:.3f}')
list_a = [1,2,3]
set_a = set(list_a)
print(set_a)