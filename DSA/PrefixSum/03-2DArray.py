
def find_sum_of_2d_array(arr, r, c):
    length = len(arr)

    # number of rows
    rows = len(arr)

    # number of columns
    columns = len(arr[0])

    prefix = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append("0")
        prefix.append(row)
    print(prefix)

    for i in range(rows):
        for j in range(columns):
            prefix[i][j] = array[i][j]
            if i > 0:
                prefix[i][j] += prefix[i - 1][j]
            if j > 0:
                prefix[i][j] += prefix[i][j - 1]
            if i > 0 and j > 0:
                prefix[i][j] -= prefix[i - 1][j - 1]
    print(prefix)
    return prefix[r][c]



array = [
    [1,2,3,6],
    [4,5,6,5],
    [3,4,5,1],
    [2,6,7,8]
]

print(find_sum_of_2d_array(array,1,1))
