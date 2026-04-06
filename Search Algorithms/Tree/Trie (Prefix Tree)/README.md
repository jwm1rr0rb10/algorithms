# Trie (Prefix Tree)

---

## Problem Description

A **Trie** (prefix tree) is a specialized data structure for storing a set of strings (usually words), enabling fast search, insert, and delete operations, as well as efficient prefix queries.

Key idea:  
- Each node stores part of a string (usually a character).
- A path from the root to a node represents a prefix.

---

## Approach (Algorithm)

Each node contains:
- Children (usually a dictionary: char → node).
- End-of-word flag (is_end or word_end).

**Operations:**
1. **insert(word):** sequentially create nodes for each character, mark the end of the word.
2. **search(word):** traverse by characters, check for nodes and end-of-word flag.
3. **startsWith(prefix):** traverse by characters, only check for node existence.

---

## Python Example

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

# Example usage:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))      # True
```

---

## Applications

- Fast word lookup in large dictionaries.
- Prefix search (autocomplete).
- Counting unique prefixes, finding the longest prefix.
- LeetCode/interview problems involving words and prefixes.

---

## When to Use

- When you need fast search for words/prefixes among a large set.
- For autocomplete, search suggestions, etc.

---

## When Not to Use

- For small dictionaries (set is easier).
- When memory is critical (Trie has higher overhead than set/map).

---

## Complexity

- **Time:** O(L), where L is the length of the word/prefix (for any operation).
- **Space:** O(N*L), where N is the number of words, L is average length.

---

## Useful Links

- [LeetCode — Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [Trie — Wikipedia](https://en.wikipedia.org/wiki/Trie)