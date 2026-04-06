# 🧠 Activity Selection: Explanation and Example

## 📌 What is the Activity Selection Problem?

The **Activity Selection** problem asks:  
Given a list of activities with start and end times, select the maximum number of non-overlapping activities that can be performed by a single person or resource.

---

## 🎯 Why is it Important?

- Models real-world scheduling problems (e.g., meeting rooms, CPU task scheduling)  
- Demonstrates the power of greedy algorithms  
- Forms the basis for interval scheduling and resource allocation

---

## ⚙️ How Does the Algorithm Work?

### Step 1: Sort Activities by End Time

- Greedy choice: always pick the activity that finishes earliest

### Step 2: Select Compatible Activities

- Initialize the end time of the last selected activity  
- Iterate through the sorted list:
  - If the start time of the current activity ≥ end time of the last selected → select it

---

## 🧪 Python Example

```python
def activity_selection(activities):
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    
    selected = []
    last_end = 0

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected

# Example usage
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
print(activity_selection(activities))
# Output: [(1, 3), (4, 6), (6, 7), (8, 9)]
```

---

## ⏱️ Complexity
- Time: O(n log n) — due to sorting
- Space: O(1) — if done in-place, or O(n) if storing selected list

---

## 🧭 Applications
- Meeting room scheduling
- sCPU job scheduling
- Resource allocation
- Timeline conflict resolution

---

## ✅ Summary
- Activity Selection is a classic greedy problem
- The key is to always pick the activity that ends earliest
- Sorting by end time ensures optimality

---