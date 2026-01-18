"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

def maximum_avg_subarray(array: [], k: int) -> float:
    n = len(array)

    if (n<k):
        return float("Not valid")

    window_sum = sum(array[:k])
    window_avg = float(window_sum/k)

    max_window_avg = window_avg

    for i in range(n-k):
        window_sum = window_sum - array[i] + array[i+k]
        window_avg = float(window_sum / k)

        max_window_avg = max(window_avg, max_window_avg)
    return  max_window_avg

print(maximum_avg_subarray([1,12,-5,-6,50,3] , 4))

