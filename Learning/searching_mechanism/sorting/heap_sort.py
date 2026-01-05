                                    # HEAP SORT ALGORITHM
'''
- Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort elements.
- It works by first building a max heap from the input data, and then repeatedly extracting the maximum element from the heap and rebuilding the heap until all elements are sorted.
- Heap Sort is particularly efficient for large datasets and has a good worst-case performance.

- Time Complexity:
    * O(n log n) in all cases (best, average, worst) due to the heap operations.

- Space Complexity:
    * O(1) as it is an in-place sorting algorithm.

- How it works:
    * Build a max heap from the input array.
    * Swap the root of the heap (the maximum element) with the last element of the heap.
    * Reduce the size of the heap by one and heapify the root element to maintain the max heap property.

'''

def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1     # left = 2*i + 1
    right = 2 * i + 2    # right = 2*i + 2

    # See if left child of root exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # See if right child of root exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
heap_sort(arr)
