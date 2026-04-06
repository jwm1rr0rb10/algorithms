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