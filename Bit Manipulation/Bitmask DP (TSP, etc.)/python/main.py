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