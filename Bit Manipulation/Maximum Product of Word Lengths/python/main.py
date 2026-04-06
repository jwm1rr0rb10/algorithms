def maxProduct(words):
    n = len(words)
    masks = [0] * n
    lengths = [len(word) for word in words]
    
    for i, word in enumerate(words):
        for c in word:
            masks[i] |= 1 << (ord(c) - ord('a'))
    
    max_prod = 0
    for i in range(n):
        for j in range(i + 1, n):
            if masks[i] & masks[j] == 0:
                max_prod = max(max_prod, lengths[i] * lengths[j])
    return max_prod

# Example usage:
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(maxProduct(words))  # Output: 16 ("abcw" and "xtfn")