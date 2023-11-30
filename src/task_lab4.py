from collections import deque


def add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)


def is_cyclic_connected(adj_list, start, V, visited):
    parent = [-1] * V
    q = deque()
    visited[start] = True
    q.append(start)

    while q:
        current = q.popleft()
        for neighbor in adj_list[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                parent[neighbor] = current
            elif parent[current] != neighbor:
                return True
    return False


def is_cyclic_disconnected(adj_list, V):
    visited = [False] * V
    for i in range(V):
        if not visited[i] and is_cyclic_connected(adj_list, i, V, visited):
            return True
    return False


with open("../input.txt", "r") as file:
    V = int(file.readline())
    adjacency_list = [[] for i in range(V)]
    for line in file:
        source, target = map(int, line.split())
        if source >= V:
            V = source + 1
            adjacency_list.extend([[] for _ in range(V - len(adjacency_list))])
        if target >= V:
            V = target + 1
            adjacency_list.extend([[] for _ in range(V - len(adjacency_list))])
        add_edge(adjacency_list, source, target)

result = "True" if is_cyclic_disconnected(adjacency_list, V) else "False"

with open("../output.txt", "w") as output_file:
    output_file.write(result)
