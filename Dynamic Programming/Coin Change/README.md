# Coin Change: Explanation and Example

## What is the Coin Change Problem?

The Coin Change problem is a classic dynamic programming problem that asks:  
Given a set of coin denominations and a total amount, what is the minimum number of coins needed to make up that amount?  
If it’s not possible, return -1.

---

## How does the Coin Change DP Algorithm work?

- **State:** `dp[i]` — the minimum number of coins needed to make the amount `i`.
- **Transition:** For each coin, for each amount from `coin` to `amount`,  
  update `dp[i] = min(dp[i], dp[i - coin] + 1)`.
- **Base case:** `dp[0] = 0` (zero coins to make amount 0).

The algorithm builds up the solution from 0 to the target amount.

---

## Python Example

```python
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
```

---

## Complexity

- **Time:** O(n * amount), where n is the number of coin denominations
- **Space:** O(amount)

---

## Where is it used?

- Making change in vending machines and ATMs
- Resource allocation and budgeting
- Video game currency systems

---

## When to use Coin Change DP?

- When you need the optimal (minimum) number of coins for a given amount
- When coin denominations are arbitrary, not just standard (like 1, 5, 10, 25)

---

## Real-life example

Suppose you need to make $11 using coins of 1, 2, and 5 units. The Coin Change algorithm quickly tells you the minimum number of coins required (3: 5 + 5 + 1).