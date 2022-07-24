"""
If target = nums[mid], return mid.
If target < nums[mid], discard all elements in the right search space, including the middle element,
                        i.e., nums[mid…high]. Now our new high would be mid-1.
If target > nums[mid], discard all elements in the left search space, including the middle element,
                        i.e., nums[low…mid]. Now our new low would be mid+1.

Time complexity:
Best Case : log2n
ex: log10(1000) = 3 (10*10*10)
"""


def binary_search_algorithm(nums, target):
    low = 0
    high = len(nums) - 1

    while high >= low:
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        if target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    nums = [2, 3, 5, 7, 8, 10, 12, 15, 18, 20]
    target = 7
    isFound = binary_search_algorithm(nums, target)
    if isFound != -1:
        print("Target Found at Index : {}".format(isFound))
    else:
        print("Element is not Found in the given List")

