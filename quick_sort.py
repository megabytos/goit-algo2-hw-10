import random
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quick_sort(less) + equal + deterministic_quick_sort(greater)


if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    execution_times = {"Randomized": [], "Deterministic": []}

    for size in sizes:
        test_array = [random.randint(0, 1_000_000) for _ in range(size)]

        start_time = time.time()
        for _ in range(5):
            randomized_quick_sort(test_array[:])
        avg_randomized_time = (time.time() - start_time) / 5
        execution_times["Randomized"].append(avg_randomized_time)

        start_time = time.time()
        for _ in range(5):
            deterministic_quick_sort(test_array[:])
        avg_deterministic_time = (time.time() - start_time) / 5
        execution_times["Deterministic"].append(avg_deterministic_time)

    for i, size in enumerate(sizes):
        print(f"\nSize of the array: {size}")
        print(f"\tRandomized QuickSort: {execution_times['Randomized'][i]:.4f} seconds")
        print(f"\tDeterministic QuickSort: {execution_times['Deterministic'][i]:.4f} seconds")


    plt.figure(figsize=(10, 6))
    plt.plot(sizes, execution_times["Randomized"], label="Randomized QuickSort", marker='o')
    plt.plot(sizes, execution_times["Deterministic"], label="Deterministic QuickSort", marker='o')
    plt.title("Comparison of Randomized and Deterministic QuickSort")
    plt.xlabel("Array size")
    plt.ylabel("Average execution time (seconds)")
    plt.legend()
    plt.grid()
    plt.savefig('diagram.png')
    plt.show()
