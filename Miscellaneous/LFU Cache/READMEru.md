# 🔍 LFU Cache (Кэш с наименьшей частотой использования)

## 📌 Описание задачи

LFU (Least Frequently Used) Cache — это политика вытеснения кэша, при которой удаляется элемент с **наименьшей частотой использования**, чтобы освободить место для новых данных. В отличие от LRU (Least Recently Used), который ориентируется на недавнее использование, LFU фокусируется на **частоте** доступа. При равной частоте, удаляется наименее недавно использованный элемент.

## 💡 Идея и подход

Для эффективной реализации LFU кэша используются:

* **Основной HashMap**: `key -> node` (доступ за O(1)).
* **Частотный словарь**: `frequency -> двусвязный список` с узлами той же частоты.
* **min\_freq**: текущая минимальная частота в кэше.

### Операции

* **get(key)**:

  * Вернуть -1, если ключа нет.
  * Обновить частоту узла и переместить в соответствующий список.
  * Обновить `min_freq`, если нужно.

* **put(key, value)**:

  * Если capacity == 0, ничего не делать.
  * Если ключ уже существует, обновить значение и частоту.
  * Если ключ новый и кэш полон, удалить элемент с минимальной частотой.
  * Добавить новый узел с freq = 1, обновить словари и `min_freq`.

## 🧪 Пример на Python

```python
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

# --- Пример использования ---
lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))  # 1
lfu.put(3, 3)       # Удаляется ключ 2
print(lfu.get(2))  # -1
print(lfu.get(3))  # 3
lfu.put(4, 4)       # Удаляется ключ 1
print(lfu.get(1))  # -1
print(lfu.get(3))  # 3
print(lfu.get(4))  # 4
```

## ⏱️ Сложность

* **Время**:

  * `get()`, `put()` — O(1) в среднем.
* **Память**:

  * O(N), где N — ёмкость кэша.

## ⚠️ Особенности

* **Разрешение конфликтов**: При равной частоте удаляется LRU-элемент.
* **Граничные случаи**: при capacity = 0 кэш не работает.
* **Сложность реализации**: LFU сложнее LRU, но эффективнее при долгосрочном доступе к одним и тем же данным.

## 🧭 Применения

* Кэширование в **процессорах**
* Кэширование в **CDN/вебе**
* Кэширование **результатов запросов** в БД
* **Замещение страниц** в ОС
* **Фильтрация сетевых пакетов**

---

## 🔗 Полезные ссылки

* [GeeksForGeeks - LFU Cache](https://www.geeksforgeeks.org/lfu-cache-implementation/)
* [LeetCode 460 - LFU Cache](https://leetcode.com/problems/lfu-cache/)
* [Wikipedia - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_frequently_used_%28LFU%29)

---

## 🧩 Связь с LeetCode

Задача LeetCode 460 — LFU Cache — это классическая задача на проектирование, включающая:

* Создание собственных структур данных (Node, LinkedList).
* Комбинацию HashMap + частотные списки.
* Эффективную реализацию политики вытеснения.
* Обработку граничных случаев и поддержание O(1) сложности.

Это сложная, но полезная задача для освоения принципов кэширования с учётом частоты доступа.
