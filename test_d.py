import time
import numpy as np
from sorting_algorithms import HybridSort, MergeSort
from generate_data import generate_data


data_10mil = generate_data(10000000, 10000000, 10001, seed = 42)[0]

hybrid_sorter = HybridSort()

start_time = time.time()
hybrid_sorter.sort(data_10mil.copy(), 16)
end_time = time.time()

hybrid_time = end_time - start_time
hybrid_comparisons = hybrid_sorter.comparison_count

merge_sorter = MergeSort()

start_time = time.time()
merge_sorter.sort(data_10mil.copy())
end_time = time.time()

merge_time = end_time - start_time
merge_comparisons = merge_sorter.comparison_count

print(f"HybridSort - Comparisons: {hybrid_comparisons}, Time: {hybrid_time} seconds")
print(f"MergeSort - Comparisons: {merge_comparisons}, Time: {merge_time} seconds")
