# Counting Sort (Сортировка подсчётом)

**Сортировка подсчётом** — это первый алгоритм в нашем списке, который не основывается на сравнениях. Это значит, что элементы не сортируются путём попарного сравнения, как в Quick Sort, Merge Sort, Heap Sort, Bubble Sort, Insertion Sort и Selection Sort.

---

## Основная идея

Сортировка подсчётом работает путём подсчёта количества вхождений каждого уникального элемента во входном массиве. Затем, используя эту информацию, вычисляются точные позиции каждого элемента в выходном отсортированном массиве.

---

## Ограничения

Сортировка подсчётом эффективна только при следующих условиях:

- Элементы должны быть целыми числами (или такими данными, которые можно однозначно сопоставить с целыми числами, например, символами).
- Диапазон значений (минимум и максимум) должен быть известен и не слишком велик. Если диапазон очень большой, потребуется много памяти для вспомогательного массива.

---

## Этапы алгоритма

Допустим, мы хотим отсортировать массив `arr` по возрастанию, и все его элементы находятся в диапазоне от `min_val` до `max_val`:

1. **Определить диапазон:** Найти максимальное (и, возможно, минимальное) значение в `arr`.
2. **Создать массив подсчёта:** Создать вспомогательный массив `count` размера `max_val - min_val + 1`, заполненный нулями.
3. **Посчитать вхождения:** Пройти по `arr` и увеличить счётчик в `count` для каждого значения.
4. **Вычислить позиции (накопительная сумма):** Модифицировать `count` так, чтобы `count[i]` содержал количество элементов ≤ значению, соответствующему индексу `i`. Это даёт финальную позицию каждого значения.
5. **Создать выходной массив:** Создать выходной массив того же размера, что и `arr`.
6. **Заполнить выходной массив:** Пройти по `arr` в обратном порядке (для стабильности), размещая значения по рассчитанным позициям и уменьшая их счётчик.
7. **Скопировать результат:** Если нужно — скопировать `output` обратно в `arr` для сортировки на месте.

---

## Пример

**Вход:** `[4, 2, 2, 8, 3, 3, 1]`  
**Диапазон значений:** 1 — 8

1. **Определить диапазон:** `max_val = 8`
2. **Массив подсчёта (`count`):** `[0, 1, 2, 2, 1, 0, 0, 0, 1]` (индексы 0-8)
3. **Позиции (накопительная сумма):** `[0, 1, 3, 5, 6, 6, 6, 6, 7]`
4. **Заполнение выхода:**  
   - Каждый элемент встаёт на своё место (см. подробный разбор в описании выше)
5. **Результат:** `[1, 2, 2, 3, 3, 4, 8]`

---

## ✅ Реализация на Go

```go
package main

import (
	"fmt"
)

// countingSort сортирует массив неотрицательных целых чисел
func countingSort(arr []int) []int {
	n := len(arr)
	if n == 0 {
		return arr
	}

	// 1. Найти максимальное значение
	maxVal := arr[0]
	for _, value := range arr {
		if value > maxVal {
			maxVal = value
		}
	}

	// 2. Создать массив подсчёта
	count := make([]int, maxVal+1)

	// 3. Посчитать вхождения
	for _, value := range arr {
		count[value]++
	}

	// 4. Посчитать накопительные суммы (позиции)
	for i := 1; i <= maxVal; i++ {
		count[i] += count[i-1]
	}

	// 5. Создать выходной массив
	output := make([]int, n)

	// 6. Заполнить выходной массив в обратном порядке (для стабильности)
	for i := n - 1; i >= 0; i-- {
		value := arr[i]
		pos := count[value] - 1
		output[pos] = value
		count[value]--
	}

	return output
}

// countingSortFullRange — сортировка для чисел с отрицательными значениями
func countingSortFullRange(arr []int) []int {
	n := len(arr)
	if n == 0 {
		return arr
	}

	minVal, maxVal := arr[0], arr[0]
	for _, value := range arr {
		if value < minVal {
			minVal = value
		}
		if value > maxVal {
			maxVal = value
		}
	}
	valueRange := maxVal - minVal + 1
	offset := -minVal

	count := make([]int, valueRange)
	for _, value := range arr {
		count[value+offset]++
	}
	for i := 1; i < valueRange; i++ {
		count[i] += count[i-1]
	}
	output := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		value := arr[i]
		pos := count[value+offset] - 1
		output[pos] = value
		count[value+offset]--
	}
	return output
}

func main() {
	data := []int{4, 2, 2, 8, 3, 3, 1}
	fmt.Println("Исходный массив:", data)
	sortedData := countingSort(data)
	fmt.Println("Отсортированный массив:", sortedData)

	data2 := []int{-5, -10, 0, 8, 10, 4, 5, -10, 0}
	fmt.Println("Исходный массив:", data2)
	sortedData2 := countingSortFullRange(data2)
	fmt.Println("Отсортированный массив:", sortedData2)
}
```

---

## ✅ Реализация на Python

### Для неотрицательных целых чисел

```python
def counting_sort_non_negative(arr):
    n = len(arr)
    if n == 0:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)
    for value in arr:
        count[value] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    output = [0] * n
    for i in range(n - 1, -1, -1):
        value = arr[i]
        pos = count[value] - 1
        output[pos] = value
        count[value] -= 1
    return output

# Пример использования:
data_counting_nn = [4, 2, 2, 8, 3, 3, 1, 0, 5, 7]
print("Исходный список (Counting Sort Non-Negative):", data_counting_nn)
sorted_data_counting_nn = counting_sort_non_negative(data_counting_nn)
print("Отсортированный список (Counting Sort Non-Negative):", sorted_data_counting_nn)
```

### Для полного диапазона (включая отрицательные)

```python
def counting_sort_full_range(arr):
    n = len(arr)
    if n == 0:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    value_range = max_val - min_val + 1
    offset = -min_val
    count = [0] * value_range
    for value in arr:
        count[value + offset] += 1
    for i in range(1, value_range):
        count[i] += count[i - 1]
    output = [0] * n
    for i in range(n - 1, -1, -1):
        value = arr[i]
        pos = count[value + offset] - 1
        output[pos] = value
        count[value + offset] -= 1
    return output

# Пример использования:
data_counting_full = [-5, -10, 0, 8, 10, 4, 5, -10, 0, 3]
print("\nИсходный список (Counting Sort Full Range):", data_counting_full)
sorted_data_counting_full = counting_sort_full_range(data_counting_full)
print("Отсортированный список (Counting Sort Full Range):", sorted_data_counting_full)
```

---

## Сложность

- **Время:** O(n + k), где `n` — количество элементов, а `k` — диапазон значений (`max_val - min_val + 1`).
- **Память:** O(n + k) на выходной и вспомогательный массивы.

---

## Преимущества

- Очень быстрый для небольших диапазонов целых чисел.
- Стабильная сортировка (относительный порядок одинаковых элементов сохраняется).

## Недостатки

- Работает только для целых чисел (или данных, которые можно преобразовать в целые).
- Требует знания диапазона значений.
- Расход памяти быстро растёт при большом диапазоне.

---

> _Сортировка подсчётом — отличный пример того, как знание дополнительных свойств ваших данных (диапазона значений) позволяет сортировать гораздо быстрее, чем алгоритмы на сравнениях!_

---