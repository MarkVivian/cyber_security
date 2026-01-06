                                        # RADIX SORT IMPLEMENTATION
'''
- Radix Sort is a non-comparative integer sorting algorithm that sorts numbers by processing individual digits.
- It works by grouping numbers based on their digits, starting from the least significant digit (LSD) to the most significant digit (MSD).
- Radix Sort uses a stable sub-sorting algorithm (like Counting Sort) to sort the numbers based on each digit.

- Time Complexity:
    * O(d * (n + k)), where d is the number of digits in the largest number, n is the number of elements in the array, and k is the range of the input (the maximum value).

- Space Complexity:
    * O(n + k) due to the auxiliary arrays used in the stable sorting algorithm.

- How it works:
    * Determine the maximum number to know the number of digits.
    * Starting from the least significant digit, use a stable sorting algorithm (like Counting Sort) to sort the array based on the current digit.
    * Repeat the process for each digit until all digits have been processed.
'''

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n  # Output array
    count = [0] * 10  # Count array for digits (0 to 9)

    # Store count of occurrences in count[]
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit. exp is 10^i where i is the current digit number
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr

# Example usage:
arr = [170, 45, 75, 90, 802, 242, 66]
print(radix_sort(arr))
