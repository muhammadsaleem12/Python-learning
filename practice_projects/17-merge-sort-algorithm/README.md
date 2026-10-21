# 🔀 Merge Sort Algorithm in Python

**Divide. Sort. Merge.**

A simple Python implementation of the **Merge Sort algorithm**, demonstrating how recursion and the divide-and-conquer approach can efficiently sort a list of numbers.

## ✨ Overview

Merge Sort is a sorting algorithm that breaks a list into smaller halves, sorts those halves recursively, and merges them back together in ascending order.

This project helped me explore recursion, list slicing, index tracking, and how smaller problems can be combined to solve a larger one.

## ⚙️ How It Works

Merge Sort follows three main steps:

1. **Divide** — Split the array into two halves until each half contains one or zero elements.
2. **Conquer** — Recursively sort each half.
3. **Merge** — Compare elements from both sorted halves and combine them into one sorted array.

## 🧠 Algorithm Visualization

For example, consider this unsorted array:

`[4, 10, 6, 14, 2, 1, 8, 5]`

The algorithm repeatedly divides the array into smaller parts, then merges them in sorted order.

**The result:**

`[1, 2, 4, 5, 6, 8, 10, 14]`

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- A terminal or code editor

### Run the Project

1. Clone this repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd merge-sort-algorithm
   ```

3. Run the Python file:

   ```bash
   python merge_sort.py
   ```

## 💻 Example Output

```text
Unsorted array:
[4, 10, 6, 14, 2, 1, 8, 5]

Sorted array:
[1, 2, 4, 5, 6, 8, 10, 14]
```

## 📊 Time & Space Complexity

| Case | Complexity |
|---|---|
| Best Case | O(n log n) |
| Average Case | O(n log n) |
| Worst Case | O(n log n) |
| Auxiliary Space | O(n) |

Merge Sort maintains \(O(n \log n)\) time complexity across all cases. This implementation uses additional lists when splitting the array, requiring \(O(n)\) auxiliary space overall.

## 🛠️ Concepts Practiced

- Recursion and base cases
- Divide-and-conquer algorithms
- List slicing in Python
- Index management
- Comparing and merging sorted lists
- Time and space complexity

## 🎯 Project Goal

The goal of this project is to strengthen my understanding of algorithms and problem-solving in Python by implementing a classic sorting algorithm from scratch.

This is part of my ongoing journey to improve my Python programming skills and build a stronger foundation in software development.

---

**Built with 🐍 Python**

*One algorithm at a time. One step closer to mastering Python.*