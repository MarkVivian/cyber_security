                            # INSERTION SORT ALGORITHM
'''
- Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.
- It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
- The algorithm works by dividing the array into a sorted and an unsorted region. It repeatedly takes the first element from the unsorted region and inserts it into the correct position in the sorted region.

- Time Complexity:
    * O(n^2) in the average and worst case,
    * O(n) in the best case (when the array is already sorted).

- Space Complexity:
    * O(1) as it is an in-place sorting algorithm.

- How it works:
    * Start with the second element of the array (the first element is considered sorted).
    * Compare the current element with the elements in the sorted region (to its left).
    * Shift all larger sorted elements to the right to make space for the current element.
    * Insert the current element into its correct position in the sorted region.
'''

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

results = insertion_sort([12, 11, 65, 13, 5, 6])
print("Sorted array is:", results)