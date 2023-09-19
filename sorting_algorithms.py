import numpy as np


class HybridSort:
    def __init__(self):
        self.comparison_count = 0

    def insertion_sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0:
                self.comparison_count += 1
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break
            arr[j + 1] = key
        return arr

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.comparison_count += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return np.array(result)

    def sort(self, arr, threshold):
        # Note S = 1 makes hybrid_sort = merge_sort and S = len(data) makes hybrid_sort = insertion_sort

        if len(arr) <= threshold:
            return self.insertion_sort(arr)

        mid = len(arr) // 2
        left = self.sort(arr[:mid], threshold)
        right = self.sort(arr[mid:], threshold)

        return self.merge(left, right)


class MergeSort:
    def __init__(self):
        self.comparison_count = 0

    def merge(self, left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            self.comparison_count += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return np.array(result)

    def sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])

        return self.merge(left, right)
