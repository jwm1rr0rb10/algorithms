def longestPalindrome(s: str) -> str:
    if not s:
        return ""
    start, max_len = 0, 1
    n = len(s)
    for i in range(n):
        # Odd length palindrome
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
        # Even length palindrome
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start, max_len = l, r - l + 1
            l -= 1
            r += 1
    return s[start:start + max_len]

# Example usage:
print(longestPalindrome("babad"))  # Output: "bab" or "aba"