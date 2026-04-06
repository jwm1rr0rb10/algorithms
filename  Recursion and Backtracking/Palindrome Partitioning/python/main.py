def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def backtrack(s, start, path, result):
    if start == len(s):
        result.append(list(path))
        return
    for end in range(start, len(s)):
        if is_palindrome(s, start, end):
            path.append(s[start:end+1])
            backtrack(s, end + 1, path, result)
            path.pop()

def partition(s):
    result = []
    backtrack(s, 0, [], result)
    return result

# Example usage:
s = "aab"
print(partition(s))
# Output: [['a', 'a', 'b'], ['aa', 'b']]