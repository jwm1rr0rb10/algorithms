def findAnagrams(s, p):
    from collections import Counter
    
    result = []
    p_count = Counter(p)
    s_count = Counter()
    window = len(p)

    for i, char in enumerate(s):
        s_count[char] += 1
        if i >= window:
            left_char = s[i - window]
            s_count[left_char] -= 1
            if s_count[left_char] == 0:
                del s_count[left_char]
        if s_count == p_count:
            result.append(i - window + 1)
    return result

# Example usage:
print(findAnagrams("cbaebabacd", "abc"))  # Output: [0, 6]