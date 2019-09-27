def BubbleSort(arr):
    for iteration in range(len(arr) - 1):
        #print("### {} ###".format(iteration))
        for cur in range(len(arr)-1):
            nxt = cur + 1
            if arr[cur] > arr[nxt]:
                arr[cur], arr[nxt] = arr[nxt], arr[cur]
    return arr


if __name__ == '__main__':
    arr = [12,7,5,9,4,2,1]
    BubbleSort(arr)
    print(arr)
