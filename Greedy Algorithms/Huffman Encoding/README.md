# 🧵 Huffman Encoding: Explanation and Example

## 📌 What is Huffman Encoding?

**Huffman Encoding** is a greedy algorithm used for lossless data compression.  
It assigns variable-length binary codes to input characters based on their frequencies — more frequent characters get shorter codes.

---

## 🎯 Why is it Important?

- Forms the basis of many compression formats (e.g., ZIP, JPEG, MP3)  
- Guarantees optimal prefix codes for a given frequency distribution  
- Widely used in file compression, network transmission, and data storage

---

## ⚙️ How Does the Algorithm Work?

### Step 1: Count character frequencies  
- Build a frequency table from the input data

### Step 2: Build a priority queue (min-heap)  
- Each node is a character and its frequency

### Step 3: Construct the Huffman Tree  
- While more than one node in the heap:
  - Remove two nodes with the lowest frequencies
  - Merge them into a new node with combined frequency
  - Insert the new node back into the heap

### Step 4: Generate codes  
- Traverse the tree:
  - Left edge → add "0"
  - Right edge → add "1"
- Leaf nodes represent characters and their codes

---

## 🧪 Python Example

```python
import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = Counter(text)
    heap = [Node(char, freq[char], None, None) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq, left, right)
        heapq.heappush(heap, merged)

    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node.char is not None:
        codebook[node.char] = prefix
    else:
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

# Example usage
text = "huffman"
tree = build_huffman_tree(text)
codes = generate_codes(tree)
print(codes)
```

---

## ⏱️ Complexity
- Time: O(n log n) — due to heap operations
- Space: O(n) — for the tree and codebook

---

## 🧭 Applications
- File compression (ZIP, GZIP)
- Multimedia encoding (JPEG, MP3)
- Network data transmission
- Compiler design (lexical analysis)

---

## ✅ Summary
- Huffman Encoding builds an optimal prefix code using a greedy strategy
- It minimizes the total number of bits needed to encode a message
- Efficient, elegant, and widely used in real-world compression systems

---