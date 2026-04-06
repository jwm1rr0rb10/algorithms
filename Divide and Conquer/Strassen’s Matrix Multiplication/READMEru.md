# Strassen’s Matrix Multiplication — Разделяй и властвуй (Divide & Conquer)

## Описание задачи

**Алгоритм Штрассена** — это быстрый способ перемножения двух квадратных матриц, использующий принцип "разделяй и властвуй". Позволяет перемножать матрицы быстрее, чем стандартный алгоритм, особенно для больших размеров.

**Задача:**  
Даны две квадратные матрицы A и B размера 2^n × 2^n. Требуется вычислить их произведение C = A × B.

**Пример:**
```python
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
# Ответ: [[19, 22], [43, 50]]
```

## Алгоритм (Strassen)

1. Разделить каждую матрицу на четыре подматрицы одинакового размера:
    - A = |A11 A12|
          |A21 A22|
    - B = |B11 B12|
          |B21 B22|
2. Вычислить 7 специальных произведений (M1–M7) вместо 8, как в обычном алгоритме:
    - M1 = (A11 + A22) × (B11 + B22)
    - M2 = (A21 + A22) × B11
    - M3 = A11 × (B12 - B22)
    - M4 = A22 × (B21 - B11)
    - M5 = (A11 + A12) × B22
    - M6 = (A21 - A11) × (B11 + B12)
    - M7 = (A12 - A22) × (B21 + B22)
3. Собрать результат из сумм и разностей этих произведений.

### Пример кода на Python

```python
def add_matrix(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2

    # Разделяем матрицы на 4 блока
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # 7 произведений по Штрассену
    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))
    M2 = strassen(add_matrix(A21, A22), B11)
    M3 = strassen(A11, sub_matrix(B12, B22))
    M4 = strassen(A22, sub_matrix(B21, B11))
    M5 = strassen(add_matrix(A11, A12), B22)
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))

    # Собираем результат
    def combine(C11, C12, C21, C22):
        top = [c11 + c12 for c11, c12 in zip(C11, C12)]
        bottom = [c21 + c22 for c21, c22 in zip(C21, C22)]
        return top + bottom

    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)
    C12 = add_matrix(M3, M5)
    C21 = add_matrix(M2, M4)
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)
    return combine(C11, C12, C21, C22)

# Пример использования:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(strassen(A, B))  # [[19, 22], [43, 50]]
```

## Временная сложность

- O(n^log2(7)) ≈ O(n^2.81)

## Где применять

- Быстрое перемножение больших квадратных матриц (например, в научных расчетах, обработке изображений, компьютерном зрении).
- Когда важна асимптотическая скорость для очень больших матриц.

## Недостатки

- Для маленьких матриц стандартное умножение быстрее из-за накладных расходов.
- Не подходит для неквадратных или неразмерных 2^n матриц без дополнительной обработки.
- Требует дополнительной памяти.

---

## Полезные ссылки

- [Wikipedia: Алгоритм Штрассена](https://ru.wikipedia.org/wiki/Алгоритм_Штрассена)
- [Хабр: Быстрое умножение матриц](https://habr.com/ru/articles/112966/)
- [YouTube: Визуализация алгоритма Штрассена (ru)](https://www.youtube.com/watch?v=6-4vYyq8eHc)

---

## Задачи на LeetCode

- [3127. Beautiful Tiling (Hard, требует умножения больших матриц)](https://leetcode.com/problems/beautiful-tiling/)
- [LCP 50. Treasure (Hard, работа с матричными операциями)](https://leetcode.com/problems/treasure/)
- [552. Student Attendance Record II (Hard, DP + matrix expo)](https://leetcode.com/problems/student-attendance-record-ii/)

---