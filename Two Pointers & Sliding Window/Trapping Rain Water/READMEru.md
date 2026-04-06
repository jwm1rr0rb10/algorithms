# Ловушка для дождевой воды (Trapping Rain Water)

## Описание задачи

Дан массив неотрицательных целых чисел `height`, где ширина каждой "стены" равна 1. Необходимо вычислить, сколько воды может быть собрано после дождя между стенами.

**Пример:**  
Вход: height = [0,1,0,2,1,0,1,3,2,1,2,1]  
Выход: 6  
Пояснение: На данном профиле высот можно собрать 6 единиц воды (см. наглядное объяснение в диаграмме).

---

## Идея алгоритма и подход

- Используется метод двух указателей для эффективного подсчёта накопленной воды:
  - Инициализируем два указателя, `left` и `right`, на концах массива.
  - Поддерживаем переменные `left_max` и `right_max` — максимальная высота слева и справа.
  - На каждом шаге:
    - Если `height[left] < height[right]`, двигаем левый указатель и обновляем `left_max`. Вода над позицией `left` — это `left_max - height[left]`.
    - Иначе двигаем правый указатель и обновляем `right_max`. Вода над позицией `right` — это `right_max - height[right]`.
- Суммируем объёмы воды на каждой позиции.

---

## Пример на Python

```python
def trap(height):
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

# Пример использования:
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # Вывод: 6
```

---

## Анализ сложности

- **Время:** O(n), один проход по массиву.
- **Память:** O(1), используется только несколько переменных.

---

## Применение в жизни

- Моделирование накопления воды в ландшафтной архитектуре или строительстве.
- Анализ гистограмм или сенсорных данных для поиска впадин и скоплений.
- Симуляция наводнений и моделирование водоёмов.

---

## Полезные ссылки

- [Trapping Rain Water — LeetCode](https://leetcode.com/problems/trapping-rain-water/)
- [Техника двух указателей — GeeksforGeeks (RU)](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Визуализация задачи Trapping Rain Water (YouTube)](https://www.youtube.com/watch?v=ZI2z5pq0TqA)

---

## Практика на LeetCode

| Сложность | Задача                     | Ссылка                                                                              |
|-----------|----------------------------|-------------------------------------------------------------------------------------|
| Сложная   | Ловушка для дождевой воды  | [#42 Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)       |
| Средняя   | Контейнер с наибольшим количеством воды | [#11 Container With Most Water](https://leetcode.com/problems/container-with-most-water/) |
| Средняя   | Trapping Rain Water II     | [#407 Trapping Rain Water II](https://leetcode.com/problems/trapping-rain-water-ii/) |

---