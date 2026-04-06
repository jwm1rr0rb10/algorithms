# Задача умножения матриц с минимизацией числа операций (Matrix Chain Multiplication, MCM)

## Описание задачи

Дан массив размеров матриц: для цепочки из n матриц A₁, A₂, ..., Aₙ, где размеры Aᵢ — p[i-1] x p[i].  
Нужно расставить скобки так, чтобы минимизировать общее количество скалярных умножений.

**Пример:**  
Ввод: p = [40, 20, 30, 10, 30] (матрицы: 40x20, 20x30, 30x10, 10x30)  
Вывод: 26000  
Пояснение: Лучшее скобкирование: ((A₁×A₂)×(A₃×A₄)), минимальное число умножений — 26000.

---

## Идея и подход

- Используется динамическое программирование:
  - Пусть `dp[i][j]` — минимальное число умножений для перемножения матриц с i по j включительно.
  - Для каждой длины цепочки перебираем все разбиения между i и j.
  - Рекуррентная формула:  
    `dp[i][j] = min(dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j])`, где i ≤ k < j.
  - База: dp[i][i] = 0 (одна матрица не умножается).

---

## Пример на Python

```python
def matrix_chain_order(p):
    n = len(p) - 1
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for l in range(2, n + 1):        # длина цепочки
        for i in range(1, n - l + 2):
            j = i + l - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[1][n]

# Пример использования:
p = [40, 20, 30, 10, 30]
print(matrix_chain_order(p))  # Выведет 26000
```

---

## Анализ сложности

- **Время:** O(n³)
- **Память:** O(n²)

---

## Применения

- Оптимизация скобок при умножении матриц
- Компиляторы и оптимизация выражений
- Планирование вычислений в линейной алгебре и графах

---

## Полезные ссылки

- [Matrix Chain Multiplication — LeetCode](https://leetcode.com/problems/minimum-cost-to-multiply-matrices/)
- [MCM — GeeksforGeeks](https://www.geeksforgeeks.org/matrix-chain-multiplication-dp-8/)
- [Wikipedia: Matrix Chain Multiplication](https://ru.wikipedia.org/wiki/Задача_о_скобках)

---

## Практика на LeetCode

| Сложность | Задача                              | Ссылка                                                                                      |
|-----------|-------------------------------------|---------------------------------------------------------------------------------------------|
| Тяжёлая   | Minimum Cost to Multiply Matrices   | [#312 Minimum Cost to Multiply Matrices](https://leetcode.com/problems/minimum-cost-to-multiply-matrices/)|
| Тяжёлая   | Burst Balloons (аналог MCM)         | [#312 Burst Balloons](https://leetcode.com/problems/burst-balloons/)                       |