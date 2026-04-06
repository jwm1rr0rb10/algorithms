def rabin_karp(text, pattern):
    n, m = len(text), len(pattern)
    if m > n:
        return []

    base = 256  # Number of possible characters
    mod = 10**9 + 7  # Large prime to avoid overflow

    pattern_hash = 0
    window_hash = 0
    h = 1  # base^(m-1) % mod

    for i in range(m - 1):
        h = (h * base) % mod

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        window_hash = (base * window_hash + ord(text[i])) % mod

    result = []
    for i in range(n - m + 1):
        # If the hashes match, do a direct string comparison
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:
                result.append(i)
        # Calculate hash for next window
        if i < n - m:
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
            if window_hash < 0:
                window_hash += mod
    return result

# Example usage:
text = "abracadabra"
pattern = "abra"
print(rabin_karp(text, pattern))  # Output: [0, 7]