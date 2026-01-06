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
def quick_sort(arr, lo=0, hi=None):
    if hi is None:
        hi = len(arr) - 1
    
    if lo >= hi:
        return 
    
    pivot = arr[hi]
    i = lo 

    print(f"array at i {arr[i]} and array at hi {arr[hi]}")
    print("<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>")
    for j in range(lo, hi):
        print(f"the value of lo: {lo}, hi: {hi}, i: {i}, j: {j}, pivot: {pivot}, arr: {arr}")
        print("-----")
        print(f"checking if arr[j] < pivot: {arr[j]} < {pivot}")
        if arr[j] < pivot:
            print(f"Swapping arr[i] {arr[i]} and arr[j] {arr[j]}")
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[hi] = arr[hi], arr[i]
    print(f"array at i {arr[i]} and array at hi {arr[hi]}")
    print(f"After partitioning: {arr}")
    print("=========")
    quick_sort(arr, lo, i - 1)
    print("(()()()()()()()()()()()()())")
    quick_sort(arr, i + 1, hi) 
    return arr   

# Example usage:
arr = [38, 43, 3, 9, 82, 27]
print(quick_sort(arr)) 