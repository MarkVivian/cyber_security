                                        # MERGE SORT ALGORITHM
'''
- Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts both halves, and then merges the sorted halves back together.
- It is more efficient than simple algorithms like Bubble Sort, Insertion Sort, and Selection Sort, especially for larger datasets.
- The algorithm works by recursively splitting the array until each subarray contains a single element (which is inherently sorted), and then merging those subarrays back together in sorted order.

- Time Complexity:
    * O(n log n) in all cases (best, average, worst) due to the divide-and-conquer approach.

- Space Complexity:
    * O(n) because it requires additional space for the temporary arrays used during the merging process.

- How it works:
    * If the array has one or zero elements, it is already sorted; return it.
    * Otherwise, divide the array into two halves.
    * Recursively apply merge sort to both halves.
    * Merge the two sorted halves back together into a single sorted array.
'''

def merge(left, right):
    merged = []
    i = j = 0

    # Merge the two arrays while maintaining order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # If there are remaining elements in left, add them
    while i < len(left):
        merged.append(left[i])
        i += 1

    # If there are remaining elements in right, add them
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

merge_results = merge_sort([4,2,1,8,7])
print(list(merge_results))