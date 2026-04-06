# 🎲 Комбинаторика: nCr и факториалы по модулю

## 📌 Описание задачи

Во многих задачах нужно вычислять биномиальные коэффициенты:

- `C(n, r) = n! / (r! × (n - r)!)`


При больших `n` или при необходимости вычислений по модулю (например, 10⁹+7), нужно использовать модульную арифметику.

---

## 💡 Идея и подход

Чтобы эффективно вычислять `C(n, r) % mod`:

1. **Предвычислить факториалы**  
   `fact[i] = i! % mod` для всех `i` до `n`.

2. **Предвычислить обратные факториалы**  
   С помощью малой теоремы Ферма (если `mod` — простое):  
   `inv_fact[i] = (fact[i])^(mod - 2) % mod`

3. **Вычислить C(n, r)**  
   `C(n, r) % mod = fact[n] × inv_fact[r] × inv_fact[n - r] % mod`

---

## 🧪 Пример на Python

```python
MOD = 10**9 + 7
MAX = 10**6 + 10

fact = [1] * MAX
inv_fact = [1] * MAX

# Предвычисление факториалов
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD

# Быстрое возведение в степень
def mod_pow(a, b, mod):
    result = 1
    while b:
        if b % 2:
            result = result * a % mod
        a = a * a % mod
        b //= 2
    return result

# Предвычисление обратных факториалов
inv_fact[MAX - 1] = mod_pow(fact[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n - r] % MOD

# Пример
print(nCr(10, 3))  # Вывод: 120
```

---

## ⏱️ Сложность
- Предобработка: O(n)
- Запрос: O(1)
- Память: O(n)

---

## 🧭 Применение
- Подсчёт сочетаний и размещений
- Динамическое программирование с комбинаторикой
- Задачи на вероятности
- Криптография
- Треугольник Паскаля по модулю

---

## 🔗 Полезные ссылки
- [**CP-Algo Binomial Coefficients**](https://cp-algorithms.com/combinatorics/binomial-coefficients.html)
- [**GeeksForgeeks - nCr%p**](https://www.geeksforgeeks.org/compute-ncr-p-set-1-introduction-and-dynamic-programming-solution/)
