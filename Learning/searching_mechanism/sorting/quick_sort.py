                                    # QUICK SORT ALGORITHM
'''
- Quick Sort is a highly efficient sorting algorithm that follows the divide-and-conquer paradigm.
- It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot.
- The sub-arrays are then sorted recursively.

- Time Complexity:
    * O(n log n) on average and in the best case,
    * O(n^2) in the worst case (which can occur when the smallest or largest element is always chosen as the pivot).

- Space Complexity:
    * O(log n) due to the recursive stack space used by the algorithm.

- How it works:
    * Choose a pivot element from the array.
    * Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
    * Recursively apply the same logic to the left and right sub-arrays.
    * Finally, combine the sorted sub-arrays and the pivot to get the sorted array.

'''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82]
print(quick_sort(arr))