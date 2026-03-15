
import random
import time
from selection_algorithms.deterministic_select import median_of_medians
from selection_algorithms.randomized_quickselect import quickselect

def generate_data(n, type="random"):
    if type == "random":
        return [random.randint(1, 100000) for _ in range(n)]
    elif type == "sorted":
        return list(range(n))
    elif type == "reverse":
        return list(range(n, 0, -1))

def run_test():
    sizes = [1000, 5000, 10000]

    for size in sizes:
        data = generate_data(size, "random")
        k = size // 2

        start = time.time()
        median_of_medians(data.copy(), k)
        det_time = time.time() - start

        start = time.time()
        quickselect(data.copy(), k)
        rand_time = time.time() - start

        print(f"Size: {size}")
        print(f"Deterministic Select Time: {det_time:.6f}")
        print(f"Randomized Quickselect Time: {rand_time:.6f}")
        print("-"*40)

if __name__ == "__main__":
    run_test()
