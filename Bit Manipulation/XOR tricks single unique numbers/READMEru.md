# XOR-трюки для поиска уникальных чисел

## Описание задачи

Побитовый XOR (`^`) — мощный инструмент для поиска уникальных элементов в массивах, где остальные встречаются по два или k раз. Вот основные приёмы:

---

## Поиск уникального числа (остальные по два раза)

Если каждое число встречается дважды, кроме одного:
- XOR всех элементов: пары обнуляются, останется уникальное.

**Пример на Python:**
```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Пример:
print(singleNumber([2,2,1]))  # 1
```

---

## Поиск двух уникальных чисел (остальные по два раза)

Если ровно два числа встречаются по разу, остальные — по два:
1. XOR всех чисел — получаем `a ^ b`.
2. Находим бит, где `a` и `b` различаются.
3. Делим числа по этому биту, XORим каждую группу.

**Пример на Python:**
```python
def singleNumber(nums):
    xor = 0
    for num in nums:
        xor ^= num
    diff = xor & -xor
    a = b = 0
    for num in nums:
        if num & diff:
            a ^= num
        else:
            b ^= num
    return [a, b]

# Пример:
print(singleNumber([1,2,1,3,2,5]))  # [3, 5]
```

---

## Поиск уникального числа (остальные по k раз)

Если все элементы встречаются k раз, кроме одного:
- Для каждого бита считаем количество единиц.
- Если count % k != 0, этот бит принадлежит уникальному числу.

**Пример на Python (k = 3):**
```python
def singleNumber(nums):
    result = 0
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1:
                count += 1
        if count % 3:
            if i == 31:
                result -= (1 << 31)
            else:
                result |= (1 << i)
    return result

# Пример:
print(singleNumber([2,2,3,2]))  # 3
```

---

## Почему это работает

- XOR коммутативен и ассоциативен.
- `a ^ a = 0` — пары обнуляются.
- Для k-раз — поразрядный подсчёт выявляет уникальный шаблон.

---

## Применение

- Проверка целостности данных
- Поиск выбросов в больших массивах
- Задачи на собеседованиях и олимпиадах

---

## Полезные ссылки

- [LeetCode #136 — Single Number (en)](https://leetcode.com/problems/single-number/)
- [LeetCode #260 — Single Number III (en)](https://leetcode.com/problems/single-number-iii/)
- [LeetCode #137 — Single Number II (en)](https://leetcode.com/problems/single-number-ii/)
- [Побитовые операции — Википедия](https://ru.wikipedia.org/wiki/Побитовая_операция)

---