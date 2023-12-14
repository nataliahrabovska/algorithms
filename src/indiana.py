def main():
    with open('C:/Users/user/PycharmProjects/algo/ijones.in', 'r') as file:
        W, H = map(int, file.readline().split())
        matrix = [file.readline().strip() for _ in range(H)]

    number = [[0] * W for _ in range(H)]

    suma = dict()
    symb = 'a'
    while symb <= 'z':
        suma[symb] = 0
        symb = chr(ord(symb) + 1)

    for i in range(H):
        number[i][0] = 1
        suma[matrix[i][0]] += 1

    for col in range(1, W):
        tmp = dict()
        symb = 'a'
        while symb <= 'z':
            tmp[symb] = 0
            symb = chr(ord(symb) + 1)
        for row in range(H):
            c = matrix[row][col]
            number[row][col] = suma[matrix[row][col]]
            if matrix[row][col] != matrix[row][col - 1]:
                number[row][col] += number[row][col - 1]
            tmp[matrix[row][col]] += number[row][col]
        symb = 'a'
        while symb <= 'z':
            suma[symb] += tmp[symb]
            symb = chr(ord(symb) + 1)

    # Writing output to a file
    with open('C:/Users/user/PycharmProjects/algo/ijones.out', 'w') as file:
        if H == 1:
            file.write(str(number[0][W - 1]) + '\n')
        else:
            file.write(str(number[0][W - 1] + number[H - 1][W - 1]) + '\n')


if __name__ == "__main__":
    main()
