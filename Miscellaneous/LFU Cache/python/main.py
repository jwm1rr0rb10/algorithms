class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

    def is_empty(self):
        return self.size == 0

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_dll = {}

    def _update_frequency(self, node):
        freq = node.freq
        self.freq_to_dll[freq].remove_node(node)
        if self.freq_to_dll[freq].is_empty() and freq == self.min_freq:
            self.min_freq += 1
        node.freq += 1
        if node.freq not in self.freq_to_dll:
            self.freq_to_dll[node.freq] = DoublyLinkedList()
        self.freq_to_dll[node.freq].add_node_to_head(node)

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update_frequency(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._update_frequency(node)
        else:
            if self.size == self.capacity:
                lfu_list = self.freq_to_dll[self.min_freq]
                node_to_remove = lfu_list.remove_tail()
                del self.key_to_node[node_to_remove.key]
                self.size -= 1
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            if 1 not in self.freq_to_dll:
                self.freq_to_dll[1] = DoublyLinkedList()
            self.freq_to_dll[1].add_node_to_head(new_node)
            self.min_freq = 1
            self.size += 1

# --- Example Usage ---
lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # 1
lfu.put(3, 3)       # Evicts key 2
print(lfu.get(2))  # -1
print(lfu.get(3))  # 3
lfu.put(4, 4)       # Evicts key 1
print(lfu.get(1))  # -1
print(lfu.get(3))  # 3
print(lfu.get(4))  # 4