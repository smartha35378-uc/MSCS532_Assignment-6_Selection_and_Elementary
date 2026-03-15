
# Assignment 6 – Medians, Order Statistics, and Data Structures

## Overview
This repository contains implementations and performance testing of selection algorithms (kth smallest element) and core data structures.

- `selection_algorithms/deterministic_select.py`: deterministic median-of-medians select.
- `selection_algorithms/randomized_quickselect.py`: randomized quickselect approach.
- `selection_algorithms/performance_test.py`: benchmark runner for runtime comparisons.
- `data_structures/stack.py`, `queue.py`, `linked_list.py`, `array_operations.py`: elementary data structures operations.
- `main.py`: driver script showcasing both selection and data structure behavior.

## Getting Started

1. Create a Python environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Run the main demo:

```bash
python main.py
```

3. Run selection performance tests manually:

```bash
python -m selection_algorithms.performance_test
            or 
python3 -m selection_algorithms.performance_test
```

## What the Code Does

- Deterministic selection finds the kth smallest in worst-case linear time using median-of-medians partitioning.
- Randomized quickselect chooses a random pivot and is expected linear time on average.
- Performance tests compare runtime of deterministic vs randomized selection across varying input sizes.
- Data structure modules provide push/pop, enqueue/dequeue, insert/delete, search and utility methods for arrays, stacks, queues, and singly linked lists.

## Findings (Summary)

- ✅ Deterministic select is stable in performance; runtime grows predictably with input size.
- ✅ Randomized quickselect is faster on average for typical random inputs but can vary due to pivot randomness.
- ⚠️ Deterministic has higher constant overhead, but better worst-case guarantees.
- 📊 The benchmark output in `performance_test.py` validates algorithmic complexity and demonstrates tradeoffs.

## Running the Tests

If automated tests exist in the project (not present in this assignment skeleton), run:

```bash
pytest
```

## Notes

- Ensure Python 3.8+ is used.
- If you modify data structures or select functions, re-run `main.py` and `performance_test.py` to confirm behavior.

