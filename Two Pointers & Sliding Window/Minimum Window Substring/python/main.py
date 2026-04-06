from collections import Counter, defaultdict

def minWindow(s, t):
    if not t or not s:
        return ""
    need = Counter(t)
    window = defaultdict(int)
    have, need_count = 0, len(need)
    res, res_len = [-1, -1], float('inf')
    l = 0

    for r, c in enumerate(s):
        window[c] += 1
        if c in need and window[c] == need[c]:
            have += 1

        while have == need_count:
            # Update result
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            # Pop from the left
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""

# Example usage:
print(minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"