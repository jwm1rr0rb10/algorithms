# Покраска домов — Динамическое программирование

## Описание задачи

Дан ряд из `n` домов, каждый можно покрасить в один из `k` цветов.  
Стоимость покраски каждого дома в определённый цвет задана матрицей `costs` размера `n x k`, где `costs[i][j]` — стоимость покраски дома `i` цветом `j`.  
Два соседних дома не могут быть покрашены в один и тот же цвет.

**Цель:**  
Минимизировать общую стоимость покраски всех домов.

---

## Идея алгоритма и подход

- Используем динамическое программирование:
  - Пусть `dp[i][j]` — минимальная стоимость покраски домов до дома `i`, если дом `i` покрашен цветом `j`.
  - Для каждого дома и цвета: `dp[i][j] = costs[i][j] + min(dp[i-1][c])` для всех `c ≠ j`.
  - Для первого дома: `dp[0][j] = costs[0][j]`.
  - Ответ: `min(dp[n-1])`.

---

## Пример на Python

```python
def min_cost(costs):
    if not costs or not costs[0]:
        return 0
    n, k = len(costs), len(costs[0])
    dp = [cost for cost in costs[0]]
    for i in range(1, n):
        new_dp = [0]*k
        for j in range(k):
            new_dp[j] = costs[i][j] + min(dp[c] for c in range(k) if c != j)
        dp = new_dp
    return min(dp)

# Пример использования:
costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]
print(min_cost(costs))  # Вывод: 10
```

---

## Анализ сложности

- **Время:** O(n * k²) (можно оптимизировать до O(n * k) для k > 2)
- **Память:** O(k) (используется скользящий массив)

---

## Применения

- Планирование с ограничениями
- Распределение ресурсов
- Варианты задачи раскраски графа

---

## Полезные ссылки

- [Paint House — LeetCode #256 (англ.)](https://leetcode.com/problems/paint-house/)
- [Paint House II — LeetCode #265 (англ.)](https://leetcode.com/problems/paint-house-ii/)
- [GeeksforGeeks: Задача о покраске домов (англ.)](https://www.geeksforgeeks.org/paint-house-algorithm/)

---

## Практика на LeetCode

| Сложность  | Задача             | Ссылка                                                              |
|------------|--------------------|---------------------------------------------------------------------|
| Средняя    | Paint House        | [#256 Paint House](https://leetcode.com/problems/paint-house/)      |
| Сложная    | Paint House II     | [#265 Paint House II](https://leetcode.com/problems/paint-house-ii/)|