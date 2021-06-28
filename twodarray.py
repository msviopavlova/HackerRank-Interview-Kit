import math


def hourglassSum(arr):
    # Write your code here

    x = 0
    y = 1
    new_array = []

    for _ in range(4):
        count = arr[0][x] + arr[0][y] + arr[0][(y+1)] + arr[1][y] + arr[2][x] + arr[2][y] + arr[2][(y+1)]
        count_two = arr[1][x] + arr[1][y] + arr[1][(y + 1)] + arr[2][y] + arr[3][x] + arr[3][y] + arr[3][(y + 1)]
        count_three = arr[2][x] + arr[2][y] + arr[2][(y + 1)] + arr[3][y] + arr[4][x] + arr[4][y] + arr[4][(y + 1)]
        count_four = arr[3][x] + arr[3][y] + arr[3][(y + 1)] + arr[4][y] + arr[5][x] + arr[5][y] + arr[5][(y + 1)]
        x = x + 1
        y = y + 1
        new_array.append(count)
        new_array.append(count_two)
        new_array.append(count_three)
        new_array.append(count_four)


    maximum = max(new_array)
    print(new_array)

    return maximum













array = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]


hourglassSum(array)