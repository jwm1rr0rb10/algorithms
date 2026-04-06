# Trie (Префиксное дерево, бор)

---

## Описание задачи

**Trie** (трай, префиксное дерево, бор) — это специализированная структура данных для хранения множества строк (обычно слов), позволяющая быстро искать, вставлять и удалять строки, а также реализовывать эффективные операции с префиксами.

Главная идея:  
- Каждый узел хранит часть строки (обычно — символ).
- Путь от корня до узла соответствует префиксу строки.

---

## Подход (алгоритм)

В каждом узле:
- Дети (обычно словарь char → node).
- Флаг конца слова (is_end или word_end).

**Операции:**
1. **insert(word):** последовательно создаём узлы для каждого символа, отмечаем конец слова.
2. **search(word):** идём по символам, проверяем наличие узлов и флаг конца слова.
3. **startsWith(prefix):** идём по символам, проверяем только наличие узлов.

---

## Пример на Python

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

# Пример использования:
trie = Trie()
trie.insert("apple")
print(trie.search("apple"))    # True
print(trie.search("app"))      # False
print(trie.startsWith("app"))  # True
trie.insert("app")
print(trie.search("app"))      # True
```

---

## Применение

- Проверка наличия слова в большом словаре.
- Поиск по префиксу (autocomplete).
- Счёт уникальных префиксов, поиск самого длинного префикса.
- Решение задач LeetCode/интервью на слова и префиксы.

---

## Когда использовать

- Когда нужно быстро искать строки/префиксы среди большого количества слов.
- Для реализации автодополнения, поисковых подсказок.

---

## Когда не стоит использовать

- Для небольших словарей (проще использовать set).
- Если важна экономия памяти (у Trie overhead по памяти выше, чем у set/map).

---

## Сложность

- **Время:** O(L), где L — длина слова/префикса (на любую операцию).
- **Память:** O(N*L), где N — число слов, L — средняя длина.

---

## Полезные ссылки

- [LeetCode — Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
- [Trie — Википедия](https://ru.wikipedia.org/wiki/Бор_(структура_данных))