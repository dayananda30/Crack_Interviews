list = [23, 4, 5, 1, 45, 3]


def bubbleSort(arr):
    i = 0
    while i < len(arr):
        for j in range(0, len(arr) - 1, 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j + 1]
                arr[j + 1] = arr[j]
                arr[j] = temp
        i = i + 1
    return arr
    #print(arr)



res = bubbleSort(list)
print(res)


