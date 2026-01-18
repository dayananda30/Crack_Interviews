def longest_substring_without_repeating_characters(array: []) -> ([],int):
    longest_substring = array[0]
    for start in range(len(array)-1):
        current_substring = array[start]
        for end in range(start+1, len(array)):
            if array[end-1] == array[end]:
                if len(current_substring) > len(longest_substring): #
                    longest_substring = current_substring
                break
            else:
                if array[end] not in current_substring:
                    current_substring = current_substring + (array[end]) # ge
                if len(current_substring) > len(longest_substring): # true
                    longest_substring = current_substring # ge

    return longest_substring, len(longest_substring)

sub_str, length1 = longest_substring_without_repeating_characters("geeksforgeeks")
print(sub_str)
print(len(sub_str))





