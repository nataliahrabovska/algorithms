def binary_search(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def findThreeNumbers(A, P):
    A.sort()
    arr_size = len(A)
    if arr_size < 3 or arr_size > 1000:
        print("Кількість елементів у масиві має бути від 3 до 1000")
        return False

    for i in range(0, arr_size):
        if A[i] < 1 or A[i] > 10 ** 9:
            print(f"неправильне значення A[i]")
            return False

    if P < 1 or P > 3 * 10 ** 9:
        print(f"неправильне значення P")
        return False

    for i in range(0, arr_size - 2):
        for j in range(i + 1, arr_size - 1):
            x = P - A[i] - A[j]
            k = binary_search(A, j + 1, arr_size-1, x)
            if k != -1:
                print("Такі числа є:", A[i], ", ", A[j], ", ", A[k])
                return True

    print("Нема таких чисел")
    return False


# A = [1, 4, 45, 6, 10, 8]
# P = 50
# arr_size = len(A)
#
# findThreeNumbers(A, P)
