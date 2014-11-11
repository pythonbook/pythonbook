from binary_heap import Node
from binary_heap import Heap

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

heap = Heap()
heap.insert(n1)
heap.insert(n2)
heap.insert(n3)
heap.insert(n4)
heap.insert(n5)
heap.insert(n6)

val = heap.delete()
print(str(val.key))

val = heap.delete()
print(str(val.key))

val = heap.delete()
print(str(val.key))

