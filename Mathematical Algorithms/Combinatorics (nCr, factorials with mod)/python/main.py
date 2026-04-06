MOD = 10**9 + 7
MAX = 10**6 + 10

fact = [1] * MAX
inv_fact = [1] * MAX

# Precompute factorials
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD

# Fast exponentiation
def mod_pow(a, b, mod):
    result = 1
    while b:
        if b % 2:
            result = result * a % mod
        a = a * a % mod
        b //= 2
    return result

# Precompute inverse factorials
inv_fact[MAX - 1] = mod_pow(fact[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# Example
print(nCr(10, 3))  # Output: 120