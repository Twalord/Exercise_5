# Overall more comments and explanations


def assign_value(target_list, target_index, source_list, source_index): 
    # Variable names, nameing convention for functions
    # Assigns the values
    target_list[target_index] = source_list[source_index]



def merge_sort(merge_list):
# Shortened variable names, snakecase for python naming conventions
    # Recursively sorts merge_list using the merge sort algorithm.
    if len(merge_list) > 1: # Deleted redundant statements
        # Find the middle point to divide the array into two halves
        mid = len(merge_list) // 2
        left_half = merge_list[:mid]
        right_half = merge_list[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Initialize indices for merging
        left_index = 0
        right_index = 0
        merge_index = 0

        # Merge the sorted halves
        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                assign_value(merge_list, merge_index, left_half, left_index)
                left_index += 1
            else:
                assign_value(merge_list, merge_index, right_half, right_index)
                right_index += 1
            merge_index += 1

        # Copy any remaining elements of left_half
        while left_index < len(left_half):
            merge_list[merge_index] = left_half[left_index]
            left_index += 1
            merge_index += 1

        # Copy any remaining elements of right_half
        while right_index < len(right_half):
            merge_list[merge_index] = right_half[right_index]
            right_index += 1
            merge_index += 1


import matplotlib.pyplot as plt

# Example list to be sorted
example_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

# Plot the original list
x = range(len(example_list))
plt.plot(x, example_list, label = 'Original')
plt.legend()
plt.show()

# Sort the list using merge sort
merge_sort(example_list)

# Plot the sorted list
plt.plot(x, example_list, label = 'Sorted')
plt.legend()
plt.show()