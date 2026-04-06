# Поиск в ширину (BFS, Breadth-First Search)

## Что это такое

**Поиск в ширину (BFS)** — базовый алгоритм для обхода или поиска в деревьях и графах. BFS исследует все вершины текущего “уровня” (всех соседей стартовой вершины), прежде чем перейти к вершинам следующего уровня.

---

## Как работает

Представьте, что вы бросаете камень в пруд: BFS распространяется как круги по воде — сначала посещаются вершины на расстоянии 1 от старта, потом на расстоянии 2, и так далее.

**Шаги алгоритма:**
1. Начинаем с выбранной стартовой вершины.
2. Добавляем стартовую вершину в очередь и помечаем её как посещённую.
3. Пока очередь не пуста:
    - Удаляем вершину из начала очереди. Обрабатываем (посещаем) её.
    - Для каждого непосещённого соседа:
        - Помечаем как посещённого.
        - Добавляем в конец очереди.

BFS естественно реализуется с помощью очереди (FIFO — “первым вошёл, первым вышел”).

---

## Сложность

| Сложность         | Значение                |
|:-----------------:|:----------------------:|
| **Время**         | O(V + E)               |
| **Память**        | O(V) (в худшем случае) |

- **V** — количество вершин
- **E** — количество рёбер  
- Каждая вершина и каждое ребро обрабатываются не более одного раза.

---

## Применение

- **Поиск кратчайшего пути в невзвешенном графе:** BFS гарантирует кратчайший путь (по количеству рёбер) от начальной вершины до всех достижимых.
- **Обход дерева по уровням**
- **Поиск всех вершин в заданном расстоянии**
- **Веб-краулеры (поиск страниц в интернете)**
- **Поиск компонент связности**
- **Основа построения остовного дерева (например, идея Prim, хотя Prim использует приоритетную очередь)**

---

## Пример на Go

```go
package main

import "fmt"

type Graph map[int][]int

func BFS(graph Graph, startNode int) {
	visited := make(map[int]bool)
	queue := []int{startNode}
	visited[startNode] = true

	for len(queue) > 0 {
		currentNode := queue[0]
		queue = queue[1:]

		fmt.Printf("Посещена вершина: %d\n", currentNode)

		for _, neighbor := range graph[currentNode] {
			if !visited[neighbor] {
				visited[neighbor] = true
				queue = append(queue, neighbor)
			}
		}
	}
}

func main() {
	graph := Graph{
		0: {1, 2},
		1: {0, 3, 4},
		2: {0, 5},
		3: {1},
		4: {1},
		5: {2},
		6: {7},
		7: {6},
	}

	fmt.Println("Обход BFS начиная с вершины 0:")
	BFS(graph, 0)
}
```

---

## Пример на Python

```python
from collections import deque

graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2],
    6: [7],
    7: [6],
}

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)

    while queue:
        current = queue.popleft()
        print(f"Посещена вершина: {current}")

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("Обход BFS начиная с вершины 0:")
bfs(graph, 0)
```

---

## Объяснение

- В обоих примерах граф представлен в виде списка смежности.
- Для BFS используется очередь (срез в Go, `deque` в Python) и множество посещённых вершин.
- Каждая вершина обрабатывается в порядке её обнаружения, что обеспечивает обход по уровням.
- В Python для очереди используется `collections.deque` (операции добавления и удаления с двух концов — O(1)).

---

## Полезные ссылки

- [Wikipedia: Поиск в ширину](https://ru.wikipedia.org/wiki/Обход_в_ширину)
- [GeeksforGeeks: Breadth-First Search (EN)](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [Visualgo: BFS Анимация (EN)](https://visualgo.net/en/dfsbfs)
- [LeetCode Explore: Graph BFS (EN)](https://leetcode.com/explore/learn/card/graph/619/breadth-first-search-in-graph/)

---

## Задачи LeetCode для тренировки BFS

### Лёгкие

|    # | Название                                          | Ссылка                                                                            |
| :--- | :------------------------------------------------ | :-------------------------------------------------------------------------------- |
|  542 | 01 Matrix                                         | [LeetCode 542](https://leetcode.com/problems/01-matrix/)                          |
|  733 | Flood Fill                                        | [LeetCode 733](https://leetcode.com/problems/flood-fill/)                         |
|  994 | Rotting Oranges                                   | [LeetCode 994](https://leetcode.com/problems/rotting-oranges/)                    |

### Средние

|    # | Название                                          | Ссылка                                                                            |
| :--- | :------------------------------------------------ | :-------------------------------------------------------------------------------- |
|  200 | Number of Islands                                 | [LeetCode 200](https://leetcode.com/problems/number-of-islands/)                  |
|  130 | Surrounded Regions                                | [LeetCode 130](https://leetcode.com/problems/surrounded-regions/)                 |
|  752 | Open the Lock                                     | [LeetCode 752](https://leetcode.com/problems/open-the-lock/)                      |
|  785 | Is Graph Bipartite?                               | [LeetCode 785](https://leetcode.com/problems/is-graph-bipartite/)                 |
|  994 | Rotting Oranges                                   | [LeetCode 994](https://leetcode.com/problems/rotting-oranges/)                    |

### Сложные

|    # | Название                                          | Ссылка                                                                            |
| :--- | :------------------------------------------------ | :-------------------------------------------------------------------------------- |
|  847 | Shortest Path Visiting All Nodes                  | [LeetCode 847](https://leetcode.com/problems/shortest-path-visiting-all-nodes/)   |
| 1192 | Critical Connections in a Network                 | [LeetCode 1192](https://leetcode.com/problems/critical-connections-in-a-network/) |

---

**Совет:**  
BFS не подходит для графов с весами рёбер (разные стоимости перехода). Для поиска кратчайших путей в таких графах используйте [алгоритм Дейкстры](https://ru.wikipedia.org/wiki/Алгоритм_Дейкстры).
