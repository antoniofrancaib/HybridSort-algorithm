import time
import numpy as np
import matplotlib.pyplot as plt
from sorting_algorithms import HybridSort, MergeSort
from generate_data import generate_data


def test_sorter_with_varying_S(sorter, data, S_values):
    comparisons = []
    times_taken = []

    for S in S_values:
        start_time = time.time()
        sorter.sort(data.copy(), S)
        end_time = time.time()

        comparisons.append(sorter.comparison_count)
        times_taken.append(end_time - start_time)

        sorter.comparison_count = 0

    return comparisons, times_taken


fixed_size = 1000
data = generate_data(fixed_size, fixed_size, 10001)[0]
S_values = list(range(1, 1000, 10))

hybrid_sorter = HybridSort()
hybrid_comparisons, hybrid_times = test_sorter_with_varying_S(hybrid_sorter, data, S_values)

merge_sorter = MergeSort()

start_time = time.time()
merge_sorter.sort(data)
end_time = time.time()

constant_merge_comparisons = merge_sorter.comparison_count
constant_merge_time = end_time - start_time

plt.figure(figsize=(7, 5))
plt.plot(S_values, hybrid_comparisons, 'o-', label='HybridSort')
plt.axhline(y=constant_merge_comparisons, color='r', linestyle='-', label='MergeSort')
plt.xlabel('Threshold (S)')
plt.ylabel('Key Comparisons')

plt.title('Key Comparisons vs Threshold')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(7, 5))
plt.plot(S_values, hybrid_times, 'o-', label='HybridSort')
plt.axhline(y=constant_merge_time, color='r', linestyle='-', label='MergeSort')
plt.xlabel('Threshold (S)')
plt.ylabel('Time Taken (seconds)')

plt.title('Time Taken vs Threshold')
plt.legend()
plt.grid(True)
plt.show()

"""largest_indices = np.argsort(hybrid_times)[-4:]
corresponding_S_values = [S_values[i] for i in largest_indices]

print("The 4 S values corresponding to the largest hybrid times are:", corresponding_S_values)"""
