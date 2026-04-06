def manacher(s):
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n  # p[i]: max radius of palindrome centered at i
    c = r = 0    # c: center of rightmost palindrome, r: its right boundary
    for i in range(n):
        mirr = 2 * c - i
        if i < r:
            p[i] = min(r - i, p[mirr])
        a, b = i + 1 + p[i], i - 1 - p[i]
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        if i + p[i] > r:
            c, r = i, i + p[i]
    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

# Example:
s = "babad"
print(manacher(s))  # Output: "bab" or "aba"