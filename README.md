# HybridSort Project

<div align="center"><i>Combining the Strengths of MergeSort & InsertionSort</i></div>

---

## 📌 Overview

In traditional sorting methods, **MergeSort** shines with its ability to efficiently handle large datasets. Conversely, **InsertionSort** boasts swiftness with smaller arrays, thanks to its minimal overhead compared to the recursive tendencies of MergeSort. This project taps into the advantages of both, involving:

- 🚀 Employing MergeSort for larger arrays.
- 🔀 Transitioning to InsertionSort when the array size is ≤ the preset threshold, <code>S</code>.

With this, we aim for a performance pinnacle, harnessing the best of both realms.

## 🌟 Key Features

- 💡 **Threshold-based Sorting**: Seamlessly swaps between MergeSort and InsertionSort depending on data size.
- 📊 **Optimized Performance**: Striving to eclipse traditional MergeSort across various datasets.
- ⚙️ **Customizable**: Adapt the threshold to explore performance variations.

## 🔍 Implementation Details

- 🟢 The array is recursively split (as in traditional MergeSort).
- 🔴 When the size of the split array is less than or equal to <code>S</code>, InsertionSort is employed for sorting.
- 🔵 The sorted sub-arrays are subsequently merged back into one.
