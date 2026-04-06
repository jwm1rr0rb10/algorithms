# 🧵 Кодирование Хаффмана: Объяснение и пример

## 📌 Что такое кодирование Хаффмана?

**Кодирование Хаффмана** — это жадный алгоритм для сжатия данных без потерь.  
Он присваивает символам переменные по длине двоичные коды на основе их частоты — чем чаще символ, тем короче его код.

---

## 🎯 Зачем это нужно?

- Лежит в основе многих форматов сжатия (ZIP, JPEG, MP3)  
- Гарантирует оптимальные префиксные коды для заданного распределения частот  
- Применяется в файловом сжатии, передаче данных и хранении информации

---

## ⚙️ Как работает алгоритм?

### Шаг 1: Подсчитать частоты символов  
- Построить таблицу частот из входного текста

### Шаг 2: Построить приоритетную очередь (min-heap)  
- Каждый узел — это символ и его частота

### Шаг 3: Построить дерево Хаффмана  
- Пока в куче больше одного узла:
  - Извлечь два узла с наименьшими частотами
  - Объединить их в новый узел с суммарной частотой
  - Поместить новый узел обратно в кучу

### Шаг 4: Сгенерировать коды  
- Обход дерева:
  - Левый переход → добавить "0"
  - Правый переход → добавить "1"
- Листовые узлы содержат символы и их коды

---

## 🧪 Пример на Python

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

# Пример использования
text = "huffman"
tree = build_huffman_tree(text)
codes = generate_codes(tree)
print(codes)
```

---

## ⏱️ Сложность
- Время: O(n log n) — из-за операций с кучей
- Память: O(n) — для дерева и таблицы кодов

---

## 🧭 Применение
- Сжатие файлов (ZIP, GZIP)
- Кодирование мультимедиа (JPEG, MP3)
- Передача данных по сети
- Построение лексических анализаторов

---

## ✅ Итог
- Кодирование Хаффмана строит оптимальный префиксный код с помощью жадной стратегии
- Минимизирует общее количество битов для кодирования сообщения
- Эффективен, элегантен и широко используется в системах сжатия данных

---