Bitmask DP (TSP, etc.)yeh # Bitmask DP (Динамическое программирование с битовыми масками)

## Описание алгоритма

Bitmask DP — это техника динамического программирования, в которой для представления множества состояний используется битовая маска (целое число, где каждый бит соответствует наличию элемента). Это позволяет эффективно сохранять и обрабатывать состояния, что особенно полезно при экспоненциальном числе различных подмножеств.

---

## Где применяется

- Задача коммивояжёра (TSP, Traveling Salesman Problem) для поиска минимального маршрута.
- Задачи на покрытие, разбиение, перебор подмножеств с ограничениями.
- Динамическое программирование по подмножествам и состояниям объектов.
- Алгоритмы на графах для небольшого числа вершин (до 20-22).

---

## Пример на Python (TSP — задача коммивояжёра)

```python
import sys

def tsp(cost):
    n = len(cost)
    dp = [[sys.maxsize] * n for _ in range(1 << n)]
    dp[1][0] = 0  # начинаем из города 0

    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or u == v:
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

    # Минимальная стоимость обхода всех городов и возврата в стартовый
    return min(dp[(1 << n) - 1][i] + cost[i][0] for i in range(n))

# Пример использования:
cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(cost_matrix))  # 80
```

---

## Как это работает

1. Состояние хранится как (mask, pos), где mask — битовая маска посещённых городов, pos — текущая позиция.
2. Для каждого состояния перебираются все возможные следующие переходы к ещё не посещённым городам.
3. Результаты для каждого состояния сохраняются в массиве dp, чтобы избежать повторных вычислений.
4. Итог — минимальная стоимость маршрута, проходящего через все города.

---

## Сложность

- **Время:** O(2^n * n^2) — для n городов.
- **Память:** O(2^n * n) — для хранения всех состояний.

---

## Применения

- Оптимизация маршрутов, задач на покрытия, перебор всех подмножеств.
- Задачи на минимальный путь, разбиение, игры с состояниями.

---

## Полезные ссылки

- [Bitmask DP — LeetCode](https://leetcode.com/tag/bit-manipulation/)
- [Bitmask DP — CP Algorithms](https://cp-algorithms.com/dynamic_programming/travelling_salesman_problem.html)
- [TSP — Википедия](https://ru.wikipedia.org/wiki/Задача_коммивояжёра)

---

## Практика на LeetCode

| Сложность | Задача                                   | Ссылка                                                        |
|-----------|------------------------------------------|---------------------------------------------------------------|
| Hard      | Traveling Salesman Problem               | [TSP — GeeksforGeeks](https://www.geeksforgeeks.org/traveling-salesman-problem-dp-implementation/) |
| Medium    | Partition to K Equal Sum Subsets         | [#698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |
| Medium    | Count Subsets With Max Bitwise OR        | [#2044](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) |

---