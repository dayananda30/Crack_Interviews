def InsertionSort(arr):
    for item in range(1,len(arr)):
        key = arr[item]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = item - 1
        while j>= 0 and key <arr[j]:
            arr[j+1] = arr[j]
            j = j -1
        arr[j+1] = key


if __name__ == '__main__':
    arr = [12,7,5,9,4,2,1]
    InsertionSort(arr)
    print(arr)


