# Concurrency is particularly useful when tasks spend time waiting for:
# - Network responses
# - Database queries
# - Files
# - User input
# - External APIs
# - Timers
# While one task waits, another task can use the available execution time.

import time
from concurrent.futures import ThreadPoolExecutor


def download_file(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

start = time.perf_counter()

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(
        download_file,
        ["file1", "file2", "file3"],
    )

elapsed = time.perf_counter() - start
print(f"Total time: {elapsed:.2f} seconds")

# Concurrency does not require multiple CPU cores. One CPU core can switch between tasks:
# async is one type of achieving concurrency. It allows a single thread 
# to manage multiple tasks by pausing and resuming them as needed. This is particularly useful for I/O-bound tasks, where the program spends a lot of time waiting for external resources.