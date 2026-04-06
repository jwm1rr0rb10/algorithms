def coin_change(coins, amount):
    # Initialize DP array
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Build up the DP table
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage
coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))  # Output: 3 (11 = 5 + 5 + 1)