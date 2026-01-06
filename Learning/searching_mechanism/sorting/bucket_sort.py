                                            # BUCKET SORT ALGORITHM
'''
- Bucket Sort is a distribution-based sorting algorithm that divides the input array into several 'buckets' and then sorts each bucket individually, either using another sorting algorithm or by recursively applying the bucket sort.
- It is particularly effective when the input is uniformly distributed over a range.
- The algorithm works by distributing the elements into a number of buckets, sorting those buckets, and then concatenating them back together.

- Time Complexity:
    * O(n + k) on average, where n is the number of elements and k is the number of buckets. In the worst case, it can degrade to O(n^2) if all elements fall into a single bucket.

- Space Complexity:
    * O(n + k) due to the additional space required for the buckets.

- How it works:
    * Create an array of empty buckets.
    * Distribute the input elements into the buckets based on a hashing function or range.
    * Sort each bucket individually using a suitable sorting algorithm or recursively applying bucket sort.
    * Concatenate the sorted buckets to form the final sorted array.
'''

def bucket_sort(arr, bucket_size=5):
    if len(arr) == 0:
        return arr

    # Determine minimum and maximum values
    min_value = min(arr)
    max_value = max(arr)

    # Initialize buckets
    bucket_count = (max_value - min_value) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    # Distribute input array values into buckets
    for num in arr:
        index = (num - min_value) // bucket_size
        buckets[index].append(num)

    # Sort each bucket and concatenate the results
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))  # You can use any sorting algorithm here

    return sorted_array

# Example usage:
arr = [29, 25, 3, 49, 9, 37, 21, 43]
sorted_arr = bucket_sort(arr)
print(sorted_arr)