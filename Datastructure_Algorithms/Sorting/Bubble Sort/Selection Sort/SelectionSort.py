def SelectionSort(arr):
    element = 0
    while element < len(arr):
        min = arr[element]
        i = element + 1
        while i < len(arr):
            if arr[i] < min:
                min = arr[i]
            i = i + 1
        min_index = arr.index(min)
        arr[element],arr[min_index] = arr[min_index],arr[element]
        element = element + 1
    return arr


if __name__ == '__main__':
    arr = [12,7,5,9,4,2]
    res = SelectionSort(arr)
    print(res)



