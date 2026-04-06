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

# Example usage:
costs = [
    [17, 2, 17],
    [16, 16, 5],
    [14, 3, 19]
]
print(min_cost(costs))  # Output: 10