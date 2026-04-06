def characterReplacement(s: str, k: int) -> int:
    from collections import defaultdict

    count = defaultdict(int)
    max_count = 0
    left = 0
    result = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_count = max(max_count, count[s[right]])

        # If more than k replacements needed, shrink window from left
        if (right - left + 1) - max_count > k:
            count[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result

# Example usage:
print(characterReplacement("AABABBA", 1))  # Output: 4