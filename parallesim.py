# Parallelism
# Now imagine three chefs, each preparing a different dish at the same time:

# Chef 1 → Task A: █████████
# Chef 2 → Task B: █████████
# Chef 3 → Task C: █████████

# In computing, parallelism usually requires multiple CPU cores or processors:
# Parallelism is useful for computation-heavy work such as:
# - Image and video processing
# - Mathematical calculations
# - Data analysis
# - Machine-learning computations
# - Compression
# - Encryption

from concurrent.futures import ProcessPoolExecutor


def calculate_sum(limit):
    total = 0

    for number in range(limit):
        total += number * number

    return total

if __name__ == "__main__":
    limits = [20_000_000, 20_000_000]

    with ProcessPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(calculate_sum, limits))

    print(results)