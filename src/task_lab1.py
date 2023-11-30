def area(m, n):
    array = []

    for j in range(n):
        if j % 2 == 0:
            for i in range(m):
                array.append((i, j))
        else:
            for i in reversed(range(m)):
                array.append((i, j))

    return array


def plant(counts):
    m = len(counts)
    n = len(counts[0])
    planting_sequence = area(m, n)

    result = []
    for i, j in planting_sequence:
        result.append(counts[i][j])

    return result
