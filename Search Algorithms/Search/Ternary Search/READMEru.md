# Тернарный поиск

## Что это такое

Тернарный поиск — это алгоритм поиска из класса "разделяй и властвуй". Как и бинарный поиск, он работает на отсортированных данных, но делит диапазон не пополам, а на три части. Тернарный поиск редко используется для поиска элемента в массиве (для этого лучше подходит бинарный поиск), но часто применяется для поиска минимума или максимума у унимодальной функции на отрезке.

---

## Как работает (поиск элемента в отсортированном массиве)

1. Начинаем с интервала поиска `[low, high]`.
2. Вычисляем две точки:
   - `mid1 = low + (high - low) // 3`
   - `mid2 = high - (high - low) // 3`
   (`mid1 < mid2`)
3. Сравниваем искомое значение с `data[mid1]` и `data[mid2]`:
    - Если `target == data[mid1]`: вернуть `mid1`.
    - Если `target == data[mid2]`: вернуть `mid2`.
    - Если `target < data[mid1]`: ищем в левой трети `[low, mid1 - 1]`.
    - Если `target > data[mid2]`: ищем в правой трети `[mid2 + 1, high]`.
    - Если `data[mid1] < target < data[mid2]`: ищем в средней трети `[mid1 + 1, mid2 - 1]`.
4. Повторяем, пока элемент не найден или диапазон не опустеет (`low > high`).

**Важное условие:** Массив (или список) должен быть отсортирован!

---

## Сложность

- **Время:** $O(\log_3 n)$, что эквивалентно $O(\log n)$, но тернарный поиск делает больше сравнений на каждом шаге, чем бинарный, поэтому обычно медленнее для поиска элемента.
- **Память:**
    - Итеративно: $O(1)$
    - Рекурсивно: $O(\log_3 n)$

---

## Когда использовать

- Для **поиска элемента в массиве** — обычно *не рекомендуется* (бинарный поиск лучше).
- Для **поиска минимума/максимума у унимодальной функции** на отрезке: тернарный поиск — стандартный подход.

---

## Пример на Go (поиск элемента в отсортированном слайсе)

```go
package main

import "fmt"

// TernarySearch ищет target в отсортированном слайсе data.
// Возвращает индекс target, если найден, иначе -1.
func TernarySearch(data []int, target int) int {
	low := 0
	high := len(data) - 1

	for low <= high {
		mid1 := low + (high-low)/3
		mid2 := high - (high-low)/3

		if data[mid1] == target {
			return mid1
		}
		if data[mid2] == target {
			return mid2
		}

		if target < data[mid1] {
			high = mid1 - 1
		} else if target > data[mid2] {
			low = mid2 + 1
		} else {
			low = mid1 + 1
			high = mid2 - 1
		}
	}
	return -1
}

func main() {
	sortedData := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	targets := []int{38, 10}

	for _, target := range targets {
		index := TernarySearch(sortedData, target)
		if index != -1 {
			fmt.Printf("Элемент %d найден по индексу %d\n", target, index)
		} else {
			fmt.Printf("Элемент %d не найден\n", target)
		}
	}
}
```

---

## Пример на Python (поиск элемента в отсортированном списке)

```python
def ternary_search(data, target):
    """
    Ищет target в отсортированном списке data с помощью тернарного поиска.
    Возвращает индекс target, если найден, иначе -1.
    """
    low = 0
    high = len(data) - 1

    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3

        if data[mid1] == target:
            return mid1
        if data[mid2] == target:
            return mid2

        if target < data[mid1]:
            high = mid1 - 1
        elif target > data[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1

# Пример использования
sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
targets = [38, 10]

for target in targets:
    index = ternary_search(sorted_data, target)
    if index != -1:
        print(f"Элемент {target} найден по индексу {index}")
    else:
        print(f"Элемент {target} не найден")
```

---

## Примечание

Тернарный поиск редко используется для поиска элементов в массивах (бинарный поиск почти всегда лучше). Основное применение — оптимизация (поиск минимума/максимума у унимодальных функций).