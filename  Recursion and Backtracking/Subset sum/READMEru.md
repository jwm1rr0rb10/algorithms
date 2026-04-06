# Задача о сумме подмножества — Рекурсивный (бэктрекинг) подход

## Что такое задача о сумме подмножества?

Дано множество (или список) целых чисел и целевая сумма T. Нужно определить, существует ли подмножество, сумма элементов которого равна T. В этой версии требуется только проверить существование такого подмножества.

**Пример:**  
Множество: {10, 7, 5, 18, 12, 20, 15}, Цель T = 35  
Возможные решения: {10, 5, 20} или {7, 18, 10}

---

## Подход с рекурсией и бэктрекингом

Для каждого элемента выбираем: включить его или нет, и рекурсивно двигаемся дальше. Бэктрекинг позволяет отсекать пути, если сумма превышена или решение невозможно.

### Алгоритм

Пусть `canFindSubsetSum(index, current_sum, target_sum, nums)` — рекурсивная функция:
- **Базовый случай 1 (успех):** Если `current_sum == target_sum` ⇒ вернуть `True`.
- **Базовый случай 2 (неудача/отсечение):** Если `current_sum > target_sum` или `index == len(nums)` ⇒ вернуть `False`.
- **Рекурсивный шаг:**
  - Включить `nums[index]` и рекурсировать.
  - Исключить `nums[index]` и рекурсировать.
  - Если хотя бы один путь приводит к успеху — вернуть `True`.

Начальный вызов: `canFindSubsetSum(0, 0, target_sum, nums)`

---

## Пример на Go

```go
package main

import "fmt"

func canFindSubsetSumHelper(index int, currentSum int, targetSum int, nums []int) bool {
	if currentSum == targetSum {
		return true
	}
	if currentSum > targetSum || index >= len(nums) {
		return false
	}
	if canFindSubsetSumHelper(index+1, currentSum+nums[index], targetSum, nums) {
		return true
	}
	if canFindSubsetSumHelper(index+1, currentSum, targetSum, nums) {
		return true
	}
	return false
}

func CanSubsetSum(nums []int, targetSum int) bool {
	return canFindSubsetSumHelper(0, 0, targetSum, nums)
}

func main() {
	nums1 := []int{10, 7, 5, 18, 12, 20, 15}
	target1 := 35
	fmt.Printf("Множество: %v, Цель: %d\n", nums1, target1)
	if CanSubsetSum(nums1, target1) {
		fmt.Println("Существует подмножество с суммой", target1)
	} else {
		fmt.Println("Нет подмножества с суммой", target1)
	}
}
```

---

## Объяснение (Go)

- **CanSubsetSum:** Точка входа, вызывает рекурсивный помощник.
- **canFindSubsetSumHelper:**
  - Базовые случаи: найдено (`currentSum == targetSum`) или неудача/отсечение.
  - Рекурсивно пробуем включить и исключить текущий элемент.

---

## Пример на Python

```python
def can_find_subset_sum_helper(index, current_sum, target_sum, nums):
    if current_sum == target_sum:
        return True
    if current_sum > target_sum or index >= len(nums):
        return False
    if can_find_subset_sum_helper(index + 1, current_sum + nums[index], target_sum, nums):
        return True
    if can_find_subset_sum_helper(index + 1, current_sum, target_sum, nums):
        return True
    return False

def can_subset_sum(nums, target_sum):
    return can_find_subset_sum_helper(0, 0, target_sum, nums)

# Пример использования:
nums1 = [10, 7, 5, 18, 12, 20, 15]
target1 = 35
print(f"Множество: {nums1}, Цель: {target1}")
if can_subset_sum(nums1, target1):
    print(f"Существует подмножество с суммой {target1}")
else:
    print(f"Нет подмножества с суммой {target1}")
```

---

## Объяснение (Python)

- **can_subset_sum:** Точка входа.
- **can_find_subset_sum_helper:** Та же логика, что и в Go — пробуем включить/исключить каждый элемент.

---

## Анализ сложности

| Метрика           | Сложность        | Пояснение                                         |
|:------------------|:-----------------|:--------------------------------------------------|
| **Время**         | O(2^N)           | Для каждого элемента: включить или исключить.     |
| **Память**        | O(N)             | Глубина стека рекурсии до N.                      |

---

## Практические замечания

- Задача о сумме подмножества — **NP-полная**; этот метод годится только для небольших N (~20–25).
- Для больших N или продакшена используют динамическое программирование (псевдополиномиальное время).
- Этот рекурсивный шаблон лежит в основе многих комбинаторных/оптимизационных задач.

---

## Применение на практике

- **Задача о рюкзаке:** Частный случай — задача о сумме подмножества.
- **Задача о разбиении:** Разделить множество на два равных по сумме подмножества.
- **Криптография:** Некоторые атаки сводятся к задаче суммы подмножества.
- **Генерация тестовых данных:** Создание наборов с заданной суммой.
- **Финансы:** Выбор активов на заданную сумму.

---

## Полезные ссылки

- [Задача о сумме подмножества — Википедия](https://ru.wikipedia.org/wiki/Задача_о_сумме_подмножества)
- [Subset Sum — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/subset-sum-problem-dp-25/)
- [Задача о разбиении](https://ru.wikipedia.org/wiki/Задача_о_разбиении)
- [Задача о рюкзаке](https://ru.wikipedia.org/wiki/Задача_о_рюкзаке)

---

## Практика на LeetCode

| Сложность | Задача                            | Ссылка                                                                          |
|-----------|-----------------------------------|---------------------------------------------------------------------------------|
| Средняя   | Partition Equal Subset Sum        | [№416 Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/) |
| Средняя   | Target Sum                        | [№494 Target Sum](https://leetcode.com/problems/target-sum/)                     |
| Средняя   | Subsets                           | [№78 Subsets](https://leetcode.com/problems/subsets/)                            |
| Средняя   | Subsets II                        | [№90 Subsets II](https://leetcode.com/problems/subsets-ii/)                      |
| Средняя   | Combination Sum                   | [№39 Combination Sum](https://leetcode.com/problems/combination-sum/)            |

---