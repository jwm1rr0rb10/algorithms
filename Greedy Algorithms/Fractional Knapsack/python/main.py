def fractional_knapsack(capacity, items):
    # items: list of (value, weight)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0.0
    for value, weight in items:
        if capacity == 0:
            break
        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value

# Example usage
items = [(60, 10), (100, 20), (120, 30)]
capacity = 50
print(fractional_knapsack(capacity, items))  # Output: 240.0