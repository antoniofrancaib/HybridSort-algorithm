import time
import numpy as np
from sorting_algorithms import HybridSort
from generate_data import generate_data
import matplotlib.pyplot as plt

datasets = generate_data(1000, 100000, 10001, seed = 42)

S_values = range(1, 100)
results = []

for data in datasets:
    data_results = []
    for S in S_values:
        sorter = HybridSort()

        start_time = time.time()
        sorter.sort(data.copy(), S)
        end_time = time.time()

        data_results.append((S, sorter.comparison_count, end_time - start_time))

        sorter.comparison_count = 0

    results.append(data_results)

avg_comparisons = []
avg_times = []

for S in S_values:
    total_comparisons = sum([result[S - 1][1] for result in results])
    total_time = sum([result[S - 1][2] for result in results])

    avg_comparisons.append(total_comparisons / len(datasets))
    avg_times.append(total_time / len(datasets))

plt.figure(figsize=(7, 5))
plt.plot(S_values, avg_comparisons, 'o-', label="Comparisons")
plt.xlabel('S Value')
plt.ylabel('Average Number of Comparisons')
plt.title('Average Number of Comparisons vs. S Value')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('comparisons_vs_S_value.png')

plt.show()


plt.figure(figsize=(7, 5))
plt.plot(S_values, avg_times, 's-', label="Time Taken")
plt.xlabel('S Value')
plt.ylabel('Average Time Taken (seconds)')
plt.title('Average Time Taken vs. S Value')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig('time_taken_vs_S_value.png')

plt.show()

min_comp_index = avg_comparisons.index(min(avg_comparisons))
S_min_comparisons = S_values[min_comp_index]

min_time_index = avg_times.index(min(avg_times))
S_min_time = S_values[min_time_index]

print(f"The value of S with the minimal number of comparisons is: {S_min_comparisons}")
print(f"The value of S with the minimal time taken is: {S_min_time}")

