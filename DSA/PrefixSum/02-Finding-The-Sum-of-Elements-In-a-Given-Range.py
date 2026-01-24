def find_sum_of_elements_in_a_range(array,left, right):
    prefix_sum = [ ]
    prefix_sum.append(array[0])
    for i in range(1,len(array)):
        prefix_sum.append(prefix_sum[i-1] + array[i])
    print(array)
    print(prefix_sum)

    return (prefix_sum[right]-prefix_sum[left-1])

print(find_sum_of_elements_in_a_range([1,2,3,4,5,6,7,8,9], 1,3))

