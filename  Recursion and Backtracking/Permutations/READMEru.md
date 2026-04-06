# Перестановки — Рекурсивный (бэктрекинг) подход

## Что такое перестановка?
* Перестановка множества — это упорядоченное расположение его элементов.
* Например, для множества `{1, 2, 3}` все перестановки:
  `{1,2,3}, {1,3,2}, {2,1,3}, {2,3,1}, {3,1,2}, {3,2,1}`
* Число перестановок из n различных элементов — `n!` (n факториал).

---

## Как с помощью рекурсии и бэктрекинга генерировать перестановки?

* Построение каждой перестановки происходит поэлементно.
* Рекурсивная функция на каждом шаге выбирает один из оставшихся элементов и добавляет его к текущей перестановке.
* Когда длина текущей перестановки равна количеству элементов, получена полная перестановка.

### Подход с бэктрекингом:
* **Выбор:** Взять неиспользованный элемент.
* **Исследование:** Добавить его к перестановке и рекурсивно продолжить.
* **Откат (Бэктрекинг):** Удалить элемент и отметить его как доступный.
* Для отслеживания использованных элементов можно использовать булев массив или множество.

---

## Анализ сложности

### Временная сложность:
* Всего существует `N!` различных перестановок для N элементов.
* Каждая строится за `O(N)` (копирование или построение).
* **Итого:** `O(N! × N)`

### Пространственная сложность:
* **Вспомогательная:** `O(N)` для стека рекурсии, текущей перестановки и массива used.
* **Общая:** `O(N! × N)` для хранения всех перестановок.

---

## Пример на Go

```go
package main

import "fmt"

func generatePermutationsHelper(nums []int, currentPermutation []int, used []bool, result *[][]int) {
	if len(currentPermutation) == len(nums) {
		permutationCopy := make([]int, len(currentPermutation))
		copy(permutationCopy, currentPermutation)
		*result = append(*result, permutationCopy)
		return
	}
	for i := 0; i < len(nums); i++ {
		if !used[i] {
			currentPermutation = append(currentPermutation, nums[i])
			used[i] = true
			generatePermutationsHelper(nums, currentPermutation, used, result)
			currentPermutation = currentPermutation[:len(currentPermutation)-1]
			used[i] = false
		}
	}
}

func Permute(nums []int) [][]int {
	var result [][]int
	used := make([]bool, len(nums))
	generatePermutationsHelper(nums, []int{}, used, &result)
	return result
}

func main() {
	nums := []int{1, 2, 3}
	permutations := Permute(nums)
	fmt.Println("Перестановки для", nums, ":")
	for _, p := range permutations {
		fmt.Println(p)
	}
}
```

---

## Объяснение Go-кода

* **Permute** инициализирует выходной срез и массив used, затем вызывает вспомогательную функцию.
* **generatePermutationsHelper** рекурсивно строит перестановки:
  * **Базовый случай:** если длина текущей перестановки равна исходной, делаем копию и сохраняем.
  * **Рекурсивный шаг:** для каждого неиспользованного элемента выбираем, рекурсируем, затем откатываем выбор.

---

## Пример на Python

```python
def solve_permutations(nums):
    result = []
    n = len(nums)
    used = [False] * n

    def backtrack(current_permutation):
        if len(current_permutation) == n:
            result.append(list(current_permutation))
            return
        for i in range(n):
            if not used[i]:
                current_permutation.append(nums[i])
                used[i] = True
                backtrack(current_permutation)
                current_permutation.pop()
                used[i] = False

    backtrack([])
    return result

# Пример использования:
nums1 = [1, 2, 3]
permutations1 = solve_permutations(nums1)
print(f"Перестановки для {nums1}:")
for p in permutations1:
    print(p)
```

---

## Объяснение Python-кода

* `solve_permutations` инициализирует результат и массив used, затем вызывает `backtrack`.
* `backtrack`:
  * **Базовый случай:** если перестановка полная — сохраняем копию.
  * **Рекурсивный шаг:** для каждого неиспользованного элемента — выбрать, рекурсировать, откатить выбор.

---

## Полезные ссылки

- [Перестановка — Википедия](https://ru.wikipedia.org/wiki/Перестановка)
- [Permutations — LeetCode (англ.)](https://leetcode.com/problems/permutations/)
- [Бэктрекинг — GeeksforGeeks (англ.)](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [Комбинаторика — Brilliant.org (англ.)](https://brilliant.org/wiki/permutations/)

---

## Практика на LeetCode

| Сложность | Задача                           | Ссылка                                                                 |
|-----------|----------------------------------|------------------------------------------------------------------------|
| Средняя   | Permutations                     | [№46 Permutations](https://leetcode.com/problems/permutations/)        |
| Средняя   | Permutations II (с дубликатами)  | [№47 Permutations II](https://leetcode.com/problems/permutations-ii/)  |
| Средняя   | Next Permutation                 | [№31 Next Permutation](https://leetcode.com/problems/next-permutation/) |
| Средняя   | Letter Tile Possibilities        | [№1079 Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/) |
| Средняя   | Generate Parentheses             | [№22 Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) |
| Средняя   | Subsets                          | [№78 Subsets](https://leetcode.com/problems/subsets/)                  |

---