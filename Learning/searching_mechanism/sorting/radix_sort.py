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
