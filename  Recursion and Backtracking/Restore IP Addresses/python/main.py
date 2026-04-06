def restore_ip_addresses(s):
    result = []

    def backtrack(start, path):
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return
        for length in range(1, 4):
            if start + length > len(s):
                break
            segment = s[start:start+length]
            if (len(segment) > 1 and segment[0] == '0') or int(segment) > 255:
                continue
            path.append(segment)
            backtrack(start + length, path)
            path.pop()  # Backtracking

    backtrack(0, [])
    return result

# Example usage:
print(restore_ip_addresses("25525511135"))
# ['255.255.11.135', '255.255.111.35']