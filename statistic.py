import time
import statistics
import sys
import os
from contextlib import contextmanager
from commands.prefiltered import PrefilteredCommand

@contextmanager
def suppress_stdout():
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        yield
    finally:
        sys.stdout.close()
        sys.stdout = original_stdout

tests_num = 100
times = []
for _ in range(tests_num):
    with suppress_stdout():  # Подавляем вывод внутри run()
        start = time.time()
        PrefilteredCommand().run()
        end = time.time()
    times.append(end - start)

print("Число выполнений:", tests_num)
print("Медиана:", statistics.median(times))

