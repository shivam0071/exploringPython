import multiprocessing
import time
import concurrent.futures

def cpu_bound(number):
    return sum(i * i for i in range(number))


def find_sums(numbers):
    # with multiprocessing.Pool() as pool:
    #     pool.map(cpu_bound, numbers)
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as pool:
        pool.map(cpu_bound, numbers)

if __name__ == "__main__":
    numbers = [5_000_000 + x for x in range(20)]

    start_time = time.time()
    find_sums(numbers)
    duration = time.time() - start_time
    print(f"Duration {duration} seconds")
    # Duration 1.6299042701721191 seconds
