
def merge_sort(array):
    # 1. Stop if the array has 0 or 1 elements (already sorted)
    if len(array) <= 1:
        return

    # 2. Split the array into two halves
    middle_point = len(array) // 2
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # 3. Recursively sort both halves
    merge_sort(left_part)
    merge_sort(right_part)

    # 4. Set up indexes to track both halves and the original array
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # 5. Compare elements and place the smaller one into the original array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # 6. Copy any remaining elements from either half
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


# Run the program and display the result
if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)
    merge_sort(numbers)
    print('Sorted array: ')
    print(numbers)
