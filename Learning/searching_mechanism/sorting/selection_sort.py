                            # SELECTION SORT ALGORITHM
'''
- Selection Sort is a simple sorting algorithm that divides the input list into two parts: a sorted and an unsorted region.
- It repeatedly selects the smallest (or largest, depending on sorting order) element from the unsorted region and moves it to the end of the sorted region.
- The algorithm maintains two subarrays in a given array:
    1) The subarray which is already sorted.
    2) The remaining subarray which is unsorted.

- Time Complexity:
    * O(n^2) in all cases (best, average, worst) because it always scans the entire unsorted portion of the array.

- Space Complexity:
    * O(1) as it is an in-place sorting algorithm.

- How it works:
    * Start with the first element of the array as the minimum.
    * Compare this minimum with the rest of the elements to find the smallest element.
    * Swap the found minimum element with the first element.
    * Move to the next position and repeat the process until the entire array is sorted.
'''

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the minimum is the first element of the unsorted region
        min_index = i

        # Iterate through the unsorted region to find the smallest element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted region
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

results = selection_sort([64, 25, 12, 22, 11])
print("Sorted array is:", results)