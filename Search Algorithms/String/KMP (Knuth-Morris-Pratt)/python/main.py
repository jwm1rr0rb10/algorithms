def compute_prefix_function(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0

    for i in range(1, m):
        while length > 0 and pattern[i] != pattern[length]:
            length = lps[length - 1]
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
    return lps

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    if m == 0:
        return []
    lps = compute_prefix_function(pattern)
    result = []
    i = j = 0

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                result.append(i - m)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

# Example usage:
text = "ababcababcabc"
pattern = "ababc"
print(kmp_search(text, pattern))  # Output: [0, 5]