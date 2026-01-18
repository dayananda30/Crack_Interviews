def maximum_sum_of_subarray_k_elements(array: [], k: int) -> int:
    n = len(array)

    if (n < k):
        print("Always Window size should be less than the array size!")
        return -1

    window_sum = sum(array[:4])

    max_sum = window_sum
    for i in range(n - k):
        window_sum = window_sum - array[i] + array[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum


if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3]
    k = 3
    print(maximum_sum_of_subarray_k_elements(arr, k))
