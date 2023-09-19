import time
import matplotlib.pyplot as plt
import numpy as np
from sorting_algorithms import HybridSort, MergeSort
from generate_data import generate_data


def test_sorter(sorter, datasets, threshold=None):
    sizes = []
    comparisons = []
    times_taken = []

    for data in datasets:
        size = len(data)
        sizes.append(size)

        start_time = time.time()
        if threshold:
            sorter.sort(data, threshold)
        else:
            sorter.sort(data)
        end_time = time.time()

        comparisons.append(sorter.comparison_count)
        times_taken.append(end_time - start_time)

        sorter.comparison_count = 0

    return sizes, comparisons, times_taken


first_magnitude = 3
second_magnitude = 7
datasets = generate_data(10**first_magnitude, 10**second_magnitude, seed=42)

S = 20
hybrid_sorter = HybridSort()
hybrid_sizes, hybrid_comparisons, hybrid_times = test_sorter(hybrid_sorter, datasets, S)

merge_sorter = MergeSort()
merge_sizes, merge_comparisons, merge_times = test_sorter(merge_sorter, datasets)

theoretical = [n * np.log2(n) for n in hybrid_sizes]

plt.figure(figsize=(7, 5))
plt.plot(hybrid_sizes, hybrid_comparisons, 'o-', label=f'HybridSort (S={S})')
plt.plot(hybrid_sizes, merge_comparisons, 's-', label=f'MergeSort')
plt.xlabel('Input size (n)')
plt.ylabel('Key Comparisons')
plt.yscale('log')  # Log scale for y-axis
plt.xscale('log')  # Log scale for y-axis
plt.title('Key Comparisons vs Input Size')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(hybrid_sizes, hybrid_times, 'o-', label=f'HybridSort (S={S})')
plt.plot(hybrid_sizes, merge_times, 's-', label=f'MergeSort')
plt.plot(hybrid_sizes, theoretical, '--', label=r'Theoretical $O(n \log n)$')
plt.xlabel('Input size (n)')
plt.ylabel('Time Taken (seconds)')
plt.yscale('log')  # Log scale for y-axis
plt.xscale('log')  # Log scale for y-axis
plt.title('Time Taken vs Input Size')
plt.legend()
plt.grid(True)
plt.show()
