
import math


class HeapMin(object):

    def __init__(self, a_list=[]):
        self.heap = []
        self._heapify_min_list(a_list)

    def _heapify_min_list(self, a_list):
        self.heap = []
        for node in a_list:
            self.push_node(node)

    def exist(self, index) -> bool:
        return index <= len(self.heap)

    def left(self, index) -> int:
        return index * 2

    def right(self, index) -> int:
        return index * 2 + 1

    def parent(self, index) -> int:
        return index // 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def heapify_min(self, index):
        # print('Heapify>>')
        parent = self.parent(index)
        left = self.left(index)
        right = self.right(index)
        if self.exist(parent):
            if self.heap[index] < self.heap[parent]:
                self.swap(index, parent)
                self.heapify_min(parent)
        elif self.exist(left):
            if self.heap[index] > self.heap[left]:
                self.swap(index, left)
                self.heapify_min(left)
        elif self.exist(right):
            if self.heap[index] > self.heap[right]:
                self.swap(index, right)
                self.heapify_min(right)

    def push_node(self, node):
        print(f'Push node: {node}')
        self.heap.append(node)
        index = len(self.heap) - 1
        self.heapify_min(index)

    def pop_node(self) -> int:
        print('Pop node')
        if self.heap:
            node = self.heap[0]
            self._heapify_min_list(self.heap[1:])
            return node
        else:
            return None

    def _heap_height(self, size) -> int:
        return math.floor(math.log(size, 2))+1

    def print_heap(self):
        print('Print heap')
        height = self._heap_height(len(self.heap))

        node_index = 0
        for level in range(height):
            max_node_level_count = 2**level
            space_count = 2**height // max_node_level_count
            max_node_level_index = max_node_level_count - 1

            node_level_index = 0
            str = ''
            while node_level_index <= max_node_level_index and node_index < len(self.heap):
                # print(f'node level index: {node_level_index}')
                # print(f'node index: {node_index}')
                # print(f'max node level index: {max_node_level_index}')
                # print(f'max index: {len(self.heap)}')
                # print('---')

                str += f'{" " * space_count}{self.heap[node_index]}'

                node_index += 1
                node_level_index += 1

            print(str)


a = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
heap = HeapMin(a)
heap.print_heap()
# heap.push_node(0)
# heap.print_heap()
# heap.push_node(11)
# heap.print_heap()

sorted_a = []
node = heap.pop_node()
while node:
    sorted_a.append(node)
    node = heap.pop_node()

print(sorted_a)
