                                    # BUBBLE SORT ALGORITHM
'''
- Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- The pass through the list is repeated until the list is sorted.
- The algorithm gets its name because smaller elements "bubble" to the top of the list.

- Time Complexity:
    * O(n^2) in the average and worst case, 
    * O(n) in the best case (when the array is already sorted).

- space complexity:
    * O(1) as it is an in-place sorting algorithm.

- How it works:
    * Start at the beginning of the array.
    * Compare the first two elements.
    * If the first element is greater than the second, swap them.

- What does the range(0, n-i-1) mean:
    * In the bubble sort algorithm, the outer loop runs 'n' times (where 'n' is the length of the array).
    * The inner loop runs from 0 to n-i-1 because with each pass through the array, the largest unsorted element "bubbles up" to its correct position at the end of the array.
    * Therefore, after 'i' passes, the last 'i' elements are already sorted and do not need to be checked again.
    * This optimization reduces the number of comparisons needed in each subsequent pass.
'''
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swap = False
        # last i elements are already sorted
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # the reason we are subtracting i is because
                # > after the first pass, the largest element is at the end
                # > meaning after every consicutive pass, the last i elements are already the largest and sorted.
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
            if not swap:
                break
    return arr

results = bubble_sort([64, 34, 25, 12, 22, 11, 90])
print("Sorted array is:", results)