def area(m, n):
    array = []

    for i in range(m):
        if i % 2 == 0:
            for j in range(n):
                array.append((i, j))
        else:
            for j in reversed(range(n)):
                array.append((i, j))

    return array


def plant(m, n, counts):
    planting_sequence = area(m, n)

    result = []
    for i, j in planting_sequence:
        result.append(counts[i][j])

    return result
