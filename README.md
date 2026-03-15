# Assignment 6: Selection Algorithms and Elementary Data Structures

## Project Description
This project was developed for an advanced study of medians, order statistics, and elementary data structures. The implementation focuses on two classical selection strategies for identifying the `k`th smallest element in an unsorted collection, alongside foundational linear data structures implemented in Python. The goal is not only to demonstrate correctness, but also to examine the practical tradeoffs between deterministic and randomized selection methods.

The repository combines algorithm implementation, empirical timing, and simple driver-based demonstrations. In that sense, it serves both as a programming submission and as a compact experimental study of algorithmic behavior.

## Repository Contents

- `main.py`: entry point that runs the selection benchmark and demonstrates the data structures
- `selection_algorithms/deterministic_select.py`: deterministic selection using the median-of-medians strategy
- `selection_algorithms/randomized_quickselect.py`: randomized quickselect implementation
- `selection_algorithms/performance_test.py`: benchmark script for comparing execution time
- `data_structures/stack.py`: stack implementation based on a Python list
- `data_structures/queue.py`: queue implementation based on a Python list
- `data_structures/linked_list.py`: singly linked list implementation
- `data_structures/array_operations.py`: basic array wrapper with elementary operations

## Instructions to Run the Code

### Environment Setup
The project can be executed with Python 3. A virtual environment is recommended for reproducibility.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the Full Program
Execute the main driver to run the benchmark and view the data structure demonstrations.

```bash
python3 main.py
```

### Run the Benchmark Only
If only the algorithmic comparison is needed, execute the benchmark module directly.

```bash
python3 -m selection_algorithms.performance_test
```

## Implementation Overview

### Selection Algorithms
The project implements two approaches to the selection problem:

- `median_of_medians(arr, k)`: a deterministic selection algorithm that recursively chooses a pivot using the median-of-medians method. This approach is designed to guarantee linear worst-case time complexity.
- `quickselect(arr, k)`: a randomized selection algorithm that chooses a pivot uniformly from the input and recursively explores only the relevant partition. This approach has expected linear-time behavior, but not the same worst-case guarantee as the deterministic method.

In both cases, `k` is treated as a zero-based index. For example, `k = len(arr) // 2` selects the median position for arrays of odd length and the upper middle position for arrays of even length.

### Elementary Data Structures
The repository also includes simple implementations of:

- a stack with `push`, `pop`, `peek`, and `is_empty`
- a queue with `enqueue`, `dequeue`, and `is_empty`
- a singly linked list with insertion, deletion, and display
- a basic array wrapper with insertion, deletion, indexed access, and display

These structures are intentionally minimal and emphasize conceptual clarity over engineering optimization.

## Experimental Procedure
The benchmark in `selection_algorithms/performance_test.py` generates random input arrays of sizes `1000`, `5000`, and `10000`. For each input size, it selects the middle order statistic using both deterministic select and randomized quickselect, then records the elapsed execution time.

The timing experiment is limited in scope by design. It is intended to provide a practical comparison of the two approaches on representative random inputs rather than a comprehensive performance study across many distributions or repeated statistical trials.

## Summary of Findings
The observed benchmark behavior supports the standard theoretical interpretation of the two algorithms.

- Randomized quickselect was consistently faster than deterministic select on the tested random inputs.
- Deterministic select exhibited predictable growth as input size increased, which is consistent with its stronger worst-case complexity guarantee.
- The median-of-medians implementation incurred noticeably higher constant-factor overhead due to recursive pivot construction, repeated partitioning, and sorting of small subgroups.
- Quickselect benefited from a much simpler pivot-selection mechanism, making it more efficient in practice for the input distributions tested here.

Representative output from one execution of `python3 main.py` is shown below:

```text
Size: 1000
Deterministic Select Time: 0.000677
Randomized Quickselect Time: 0.000288

Size: 5000
Deterministic Select Time: 0.005397
Randomized Quickselect Time: 0.002133

Size: 10000
Deterministic Select Time: 0.010490
Randomized Quickselect Time: 0.003636
```

From an analytical perspective, the results illustrate an important distinction between asymptotic guarantees and empirical performance. Although deterministic select is theoretically attractive because of its worst-case linear bound, the additional computational overhead makes it less competitive than randomized quickselect on moderate-sized random inputs. This outcome is common in practice and reflects the broader principle that asymptotic optimality does not always imply superior observed runtime.

## Limitations

- The benchmark currently evaluates only random inputs, even though helper support exists for sorted and reverse-ordered data generation.
- The experiment is based on single-run timings rather than averaged results over many trials.
- The queue implementation uses `list.pop(0)`, which is `O(n)` and therefore not ideal for large-scale queue workloads.
- The code is written for instructional clarity and algorithmic demonstration rather than production efficiency.

## Demonstration Output
In addition to the benchmark, `main.py` demonstrates the behavior of the elementary data structures. A representative output is shown below:

```text
Stack Example
Pop: 20

Queue Example
Dequeue: 1

Linked List Example
5 -> 10 -> 15 -> None
```

## Conclusion
This project demonstrates both the conceptual and practical aspects of selection algorithms and elementary data structures. The deterministic and randomized selection methods each satisfy the functional objective of locating the `k`th smallest element, but their empirical behavior differs in meaningful ways. The benchmark results show that randomized quickselect is the stronger practical performer for the tested input sizes, while deterministic select remains valuable as a method with stronger theoretical guarantees. Together, the implementations provide a concise study of the relationship between algorithm design, computational complexity, and observed runtime behavior.
