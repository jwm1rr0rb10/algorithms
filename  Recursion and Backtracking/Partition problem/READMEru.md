# Задача о разбиении множества — Рекурсивный (бэктрекинг) подход

## Где применяется задача о разбиении множества

Задача о разбиении (Partition Problem) спрашивает, можно ли разделить данное множество положительных целых чисел на два подмножества с равными суммами. Это классическая комбинаторная задача и частный случай задачи о подмножестве с заданной суммой (Subset Sum Problem).

**Примеры применения:**
- Балансировка нагрузки между двумя серверами или группами.
- Справедливое распределение призов, ресурсов или предметов между двумя участниками.
- Оптимизация распределения задач, памяти или ресурсов.
- Планирование и анализ в логистике или управлении проектами.

---

## Сложность алгоритма

- **Временная сложность:**  
  O(2^N), где N — количество элементов во входном множестве.  
  Каждый элемент может быть либо включён в первое подмножество, либо нет (и тогда относится ко второму).

- **Пространственная сложность:**  
  O(N) — глубина стека рекурсии при бэктрекинге.

---

## Пример на Python

```python
def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False  # Если сумма нечётная, разбиение невозможно

    target = total // 2

    def backtrack(i, current_sum):
        # Нашли подмножество с нужной суммой
        if current_sum == target:
            return True
        # Превысили сумму или закончились элементы
        if current_sum > target or i == len(nums):
            return False
        # Пробуем включить или не включать текущий элемент
        return (backtrack(i + 1, current_sum + nums[i]) or
                backtrack(i + 1, current_sum))

    return backtrack(0, 0)

# Пример использования
print(can_partition([1, 5, 11, 5]))  # True ([1, 5, 5] и [11])
print(can_partition([1, 2, 3, 5]))   # False
```

### Пояснение к коду

- Сначала считается сумма всех элементов. Если сумма нечётная, разбиение невозможно.
- Рекурсивная функция `backtrack` пытается набрать половину суммы.
- На каждом шаге можно включить текущий элемент в подмножество или пропустить его.
- Если найдено подмножество с целевой суммой, функция возвращает True.

---

## Примеры из жизни

1. **Балансировка нагрузки:** Равномерное распределение задач между двумя серверами или сотрудниками.
2. **Деление ресурсов:** Честное распределение призов или предметов между двумя людьми.
3. **Планирование:** Назначение задач двум процессорам или командам для минимизации дисбаланса.
4. **Разработка игр:** Равномерное распределение ресурсов или создание сбалансированных команд.

---

# Полезные ссылки

- [Задача о разбиении — Википедия](https://ru.wikipedia.org/wiki/Задача_о_разбиении)
- [Задача о подмножестве с заданной суммой — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
- [Динамическое программирование и бэктрекинг — LeetCode Discuss (англ.)](https://leetcode.com/problems/partition-equal-subset-sum/solutions/)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)

---

# Практика на LeetCode

| Сложность | Задача                                    | Ссылка                                                                                   |
|-----------|-------------------------------------------|------------------------------------------------------------------------------------------|
| Средняя   | Partition Equal Subset Sum                | [№416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| Средняя   | Subset Sum                               | [№494 Target Sum](https://leetcode.com/problems/target-sum/)                             |
| Средняя   | Split Array Largest Sum                   | [№410 Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)    |
| Средняя   | Minimum Subset Sum Difference             | [№1049 Last Stone Weight II](https://leetcode.com/problems/last-stone-weight-ii/)        |
| Легкая    | Subsets                                  | [№78 Subsets](https://leetcode.com/problems/subsets/)                                    |
| Средняя   | Subsets II                               | [№90 Subsets II](https://leetcode.com/problems/subsets-ii/)                              |
| Средняя   | Combination Sum                          | [№39 Combination Sum](https://leetcode.com/problems/combination-sum/)                    |

---