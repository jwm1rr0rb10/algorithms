# Минимальное окно, содержащее подстроку

## Описание задачи

Даны две строки `s` и `t` длиной `m` и `n` соответственно. Необходимо вернуть минимальную по длине подстроку из `s`, которая содержит все символы строки `t` (с учётом повторов). Если такой подстроки не существует, вернуть пустую строку `""`.

**Пример:**  
Вход: s = "ADOBECODEBANC", t = "ABC"  
Выход: "BANC"  
Пояснение: Минимальное окно в `s`, содержащее все символы из `t` — это "BANC".

---

## Идея алгоритма и подход

- Используется техника скользящего окна (два указателя) и хеш-таблицы (или массивы) для подсчёта символов.
- Создаём словарь `need` с количеством каждого символа из `t`.
- Расширяем правую границу окна, добавляя символы из `s`, пока не будут собраны все нужные символы.
- Затем пробуем сдвигать левую границу окна вправо, чтобы минимизировать длину подстроки, сохраняя все необходимые символы.
- Отслеживаем минимальную длину и начальную позицию найденного окна.

---

## Пример на Python

```python
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
            # Обновляем результат
            if (r - l + 1) < res_len:
                res = [l, r]
                res_len = r - l + 1
            # Убираем символ слева
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r+1] if res_len != float('inf') else ""

# Пример использования:
print(minWindow("ADOBECODEBANC", "ABC"))  # Вывод: "BANC"
```

---

## Анализ сложности

- **Время:** O(m + n), где m = len(s), n = len(t) (каждый символ обрабатывается максимум дважды).
- **Память:** O(1) при фиксированном алфавите (например, ASCII); иначе O(k), где k — число уникальных символов в `t`.

---

## Применение в жизни

- Анализ ДНК: поиск самого короткого сегмента, содержащего все необходимые нуклеотиды.
- Текстовый майнинг: извлечение минимального контекста для заданных ключевых слов.
- Обработка потоковых данных: нахождение минимальных сегментов с выполнением условий.
- Информационный поиск: подсветка в документе всех ключевых слов в кратчайшем фрагменте.

---

## Полезные ссылки

- [Minimum Window Substring — LeetCode](https://leetcode.com/problems/minimum-window-substring/)
- [Скользящее окно — GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Хеш-таблица — Википедия](https://ru.wikipedia.org/wiki/Хеш-таблица)

---

## Практика на LeetCode

| Сложность | Задача                                        | Ссылка                                                                                         |
|-----------|-----------------------------------------------|------------------------------------------------------------------------------------------------|
| Сложная   | Минимальное окно, содержащее подстроку        | [#76 Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)        |
| Средняя   | Самая длинная подстрока без повторяющихся символов | [#3 Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |
| Сложная   | Максимум в скользящем окне                    | [#239 Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)           |
| Средняя   | Перестановка в строке                         | [#567 Permutation in String](https://leetcode.com/problems/permutation-in-string/)             |

---