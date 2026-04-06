# 🧮 Fractional Knapsack: Explanation and Example

## 📌 What is the Fractional Knapsack Problem?

The **Fractional Knapsack** problem asks:  
Given a set of items, each with a weight and a value, and a knapsack with a weight capacity, determine the maximum total value that can be obtained by taking whole or fractional parts of items.

Unlike the 0/1 Knapsack, you can take fractions of items.

---

## 🎯 Why is it Important?

- Models real-world resource allocation problems  
- Demonstrates greedy strategy optimality  
- Used in logistics, finance, and bandwidth allocation

---

## ⚙️ How Does the Algorithm Work?

### Step 1: Compute value-to-weight ratio for each item  
- Sort items in descending order of value/weight

### Step 2: Greedily fill the knapsack  
- Take as much as possible from the highest ratio item  
- If the item fits fully, take it  
- If not, take the fraction that fits

---

## 🧪 Python Example

```python
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
```

---

## ⏱️ Complexity
- Time: O(n log n) — due to sorting
- Space: O(1) — if sorting in-place

---

## 🧭 Applications
- Resource allocation with divisible goods
- Bandwidth distribution
- Portfolio optimization
- Load balancing

---

## ✅ Summary
- Fractional Knapsack allows taking parts of items
- Greedy strategy is optimal due to the value/weight ratio
- Efficient and widely applicable in real-world scenarios

---