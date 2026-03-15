
from selection_algorithms.performance_test import run_test
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.linked_list import LinkedList

def test_data_structures():

    print("\nStack Example")
    s = Stack()
    s.push(10)
    s.push(20)
    print("Pop:", s.pop())

    print("\nQueue Example")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    print("Dequeue:", q.dequeue())

    print("\nLinked List Example")
    ll = LinkedList()
    ll.insert(5)
    ll.insert(10)
    ll.insert(15)
    ll.display()

if __name__ == "__main__":
    print("Running Selection Algorithm Performance Tests")
    run_test()

    test_data_structures()
