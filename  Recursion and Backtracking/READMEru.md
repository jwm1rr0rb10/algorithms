# Recursion and Backtracking Algorithms — Overview

Рекурсия и бэктрекинг — фундаментальные техники для решения задач перебора, поиска и генерации всех вариантов, когда важно попробовать все возможные комбинации или построить результат шаг за шагом, откатываясь (backtrack) при необходимости. Эти подходы часто используются для задач с ограничениями, поиска оптимального решения, а также там, где требуется перебрать все варианты.

---

## Основные алгоритмы и их сложности

| Алгоритм                                 | Временная сложность         | Пространственная сложность  |
|------------------------------------------|----------------------------|-----------------------------|
| **Permutations**                         | O(n × n!)                  | O(n) (stack)                |
| **N-Queens problem**                     | O(n!)                      | O(n²)                       |
| **Sudoku solver**                        | O(9^m) (m = empty cells)   | O(1)                        |
| **Subset sum**                           | O(2^n)                     | O(n) (stack)                |
| **Word Search**                          | O(N × 4^L)                 | O(L) (stack)                |
| **Combinations (n choose k)**            | O(C(n, k))                 | O(k) (stack)                |
| **All Combinations (any length)**        | O(2^n)                     | O(n) (stack), O(2^n×n) (res)|
| **Partition problem**                    | O(2^n)                     | O(n) (stack)                |
| **Palindrome Partitioning**              | O(2^n)                     | O(n) (stack)                |
| **Letter Combinations of a Phone Number**| O(4^n) (n = digits)        | O(n) (stack)                |
| **Restore IP Addresses**                 | O(1)                       | O(1) (stack)                |
| **Generate Parentheses**                 | O(4^n / √n)                | O(n) (stack)                |

---

## Применение: где хорошо работают

### 1. **Генерация вариантов**
- **Permutations, Combinations, Subsets, Generate Parentheses**
- Генерация всех возможных конфигураций (тесты, поиски, пароли, комбинации).

### 2. **Задачи на поиск с ограничениями**
- **N-Queens, Sudoku, Word Search, Partition problem, Palindrome Partitioning**
- Поиск решения при жёстких правилах (размещение, разбиение, определённые условия).

### 3. **Поиск путей и разбиение**
- **Word Search, Restore IP Addresses, Palindrome Partitioning**
- Поиск всех путей или способов разбить данные на валидные части.

### 4. **Комбинаторные оптимизационные задачи**
- **Subset sum, Partition problem**
- Поиск подмножеств с определённой суммой или свойством.

---

## Где применять с осторожностью (или **лучше не использовать** бэктрекинг напрямую)

- **Большие входные данные:** Экспоненциальная сложность быстро приводит к неработоспособности при n > 20–25.
- **Задачи, требующие оптимизации по времени:** Если подход допускает жадные, динамические, или жёстко алгоритмические решения — используйте их!
- **Где важна эффективность, а не полный перебор:** Например, численные задачи, простой поиск, сортировка, работа с потоками.

---

## Must-Have (Мастхев) алгоритмы

- **Permutations**: Задачи перестановок, генерации всех порядков.
- **Combinations, All Combinations (Subsets)**: Для всех вариантов выбора элементов.
- **Generate Parentheses**: Классика для парсеров и вложенных структур.
- **N-Queens**: Базовый пример бэктрекинга на доске и с ограничениями.

---

## Less Useful / Useless (в редких случаях нужны):

- **Sudoku solver**: Используйте только для учебных/малых задач. Подходит для демонстрации, но не для реальных больших судоку.
- **Restore IP Addresses**: Полезно только для узких задач парсинга.
- **Palindrome Partitioning**: Встречается не так часто в реальных проектах.

---

## Группировка по типу задачи

### **Генерация всех вариантов**
- Permutations
- Combinations (Fixed k and Any Length)
- Subsets (All Combinations)
- Generate Parentheses
- Letter Combinations of a Phone Number

### **Поиск с ограничениями**
- N-Queens
- Sudoku solver
- Word Search
- Partition problem
- Palindrome Partitioning

### **Разбиение и парсинг**
- Restore IP Addresses
- Palindrome Partitioning

---

## Советы

- **Бэктрекинг** — мощный инструмент, но используйте его только там, где нужен полный перебор или задача подразумевает множество вариантов решения.
- Если задача позволяет — ищите оптимизации: отсечения (pruning), запоминание (memoization), динамическое программирование.
- Для маленьких n (10–15) — не бойтесь использовать бэктрекинг для генерации или поиска.

---

## Ссылки

- [Backtracking — GeeksforGeeks](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [LeetCode Explore: Recursion](https://leetcode.com/explore/learn/card/recursion-i/)
- [LeetCode Explore: Backtracking](https://leetcode.com/explore/learn/card/recursion-ii/)

---