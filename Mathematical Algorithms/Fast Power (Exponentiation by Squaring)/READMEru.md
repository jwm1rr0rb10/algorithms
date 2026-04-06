
# ⚡ Быстрое возведение в степень (Exponentiation by Squaring)

## 📌 Описание задачи

Быстрое возведение в степень используется для вычисления `a^b % mod`, особенно при больших `b` (до 10¹⁸ и выше).  
Наивный способ работает за O(b), но **возведение в степень через разложение** (Exponentiation by Squaring) — за O(log b).

---

## 💡 Идея и подход

Основная идея:

- Если `b` чётное:  
  `a^b = (a^(b/2))^2`

- Если `b` нечётное:  
  `a^b = a × a^(b - 1)`

Таким образом, степень уменьшается вдвое на каждом шаге.

---

## 🧪 Пример на Python

```python
def fast_pow(a, b, mod):
    result = 1
    a %= mod
    while b > 0:
        if b % 2 == 1:
            result = result * a % mod
        a = a * a % mod
        b //= 2
    return result

# Пример
print(fast_pow(2, 10, 1000))  # Вывод: 24 (2^10 = 1024, 1024 % 1000 = 24)
```

---

## ⏱️ Сложность
- Время: O(log b)
- Память: O(1) (в итеративной версии)

---

## 🧭 Применение
- Модульное возведение в степень (RSA, малая теорема Ферма)
- Вычисление обратных элементов в комбинаторике
- Быстрое возведение матриц в степень
- Быстрое вычисление чисел Фибоначчи

---

## 🔗 Полезные ссылки
- [**CP Algo *Binary Exponentiation**](https://cp-algorithms.com/algebra/binary-exp.html)
- [**GeeksForgeeks Modular Exponentiation**](https://www.geeksforgeeks.org/modular-exponentiation-power-in-modular-arithmetic/)