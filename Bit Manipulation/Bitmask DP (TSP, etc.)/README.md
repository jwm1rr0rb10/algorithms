# Bitmask DP (Dynamic Programming with Bitmasks)

## Algorithm Description

Bitmask DP is a dynamic programming technique in which the set of states is represented using a bitmask (an integer where each bit corresponds to the presence or absence of an element). This allows for efficient storage and processing of states, which is especially useful when the number of possible subsets is exponential.

---

## Where It Works

- Traveling Salesman Problem (TSP) to find the minimum-cost tour.
- Problems involving covering, partitioning, or iterating over subsets with constraints.
- Dynamic programming on subsets and states (games, optimal groupings).
- Graph algorithms with a small number of nodes (usually up to 20-22).

---

## Python Example (TSP — Traveling Salesman Problem)

```python
import sys

def tsp(cost):
    n = len(cost)
    dp = [[sys.maxsize] * n for _ in range(1 << n)]
    dp[1][0] = 0  # start from city 0

    for mask in range(1, 1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v) or u == v:
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + cost[u][v])

    # Minimum cost to visit all cities and return to the start
    return min(dp[(1 << n) - 1][i] + cost[i][0] for i in range(n))

# Example usage:
cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
print(tsp(cost_matrix))  # 80
```

---

## How It Works

1. The state is stored as (mask, pos), where mask is the bitmask of visited cities, and pos is the current position.
2. For each state, all possible next moves to unvisited cities are tried.
3. Results for each state are memoized in the dp array to avoid recomputation.
4. The final answer is the minimal cost of a route visiting all cities.

---

## Complexity

- **Time:** O(2^n * n^2) for n cities.
- **Space:** O(2^n * n) for storing all states.

---

## Applications

- Route optimization, covering problems, subset enumeration.
- Optimal path, partitioning, game states tracking.

---

## Useful Links

- [Bitmask DP — LeetCode](https://leetcode.com/tag/bit-manipulation/)
- [Bitmask DP — CP Algorithms](https://cp-algorithms.com/dynamic_programming/travelling_salesman_problem.html)
- [Traveling Salesman Problem — Wikipedia](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

---

## LeetCode Practice

| Difficulty | Problem                                | Link                                                          |
|------------|----------------------------------------|---------------------------------------------------------------|
| Hard       | Traveling Salesman Problem             | [TSP — GeeksforGeeks](https://www.geeksforgeeks.org/traveling-salesman-problem-dp-implementation/) |
| Medium     | Partition to K Equal Sum Subsets       | [#698](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/) |
| Medium     | Count Subsets With Max Bitwise OR      | [#2044](https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/) |

---