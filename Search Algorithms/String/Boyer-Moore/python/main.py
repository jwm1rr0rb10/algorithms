def bad_character_table(pattern):
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table

def boyer_moore_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    bad_char = bad_character_table(pattern)
    result = []
    shift = 0

    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            result.append(shift)
            shift += m - bad_char.get(text[shift + m], -1) if shift + m < n else 1
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))
    return result

# Example usage:
text = "ABAAABCD"
pattern = "ABC"
print(boyer_moore_search(text, pattern))  # Output: [4]