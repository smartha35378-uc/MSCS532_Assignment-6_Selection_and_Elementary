
from selection_algorithms import deterministic_select, randomized_select
from data_structures import Stack, Queue, LinkedList

def demo_selection():
    arr = [7, 2, 1, 8, 6, 3, 5, 4]
    k = 3
    print("Array:", arr)
    print("Deterministic Select:", deterministic_select(arr.copy(), k))
    print("Randomized Select:", randomized_select(arr.copy(), k))

def demo_data_structures():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    print("Stack pop:", stack.pop())

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    print("Queue dequeue:", queue.dequeue())

    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    print("Linked List:", ll.traverse())

if __name__ == "__main__":
    demo_selection()
    demo_data_structures()
