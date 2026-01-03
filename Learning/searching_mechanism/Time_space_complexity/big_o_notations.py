                                # BIG O NOTATIONS
'''
- Big O notation is a mathematical representation used to describe the performance or complexity of an algorithm.
    
    ^ O  
    |       
    |   { O(N!) - Factorial Time }
    |
    |   { O(2^N) - Exponential Time }
    |
    |   { O(N^3) - Cubic Time }
    |
    |   { O(N^2) - Quadratic Time }
    |
    |   { O(N log N) - Linearithmic Time }
    |
    |   { O(N) - Linear Time }
    |
    |   { O(log N) - Logarithmic Time }
    |
    |   { O(1) - Constant Time }
    |
    |----------------------------------> N ( Input Size )

'''

           # O(1) - CONSTANT TIME
'''    TIME COMPLEXITY EXPLANATION '''
def constant_time_example(data, index):
    # Accessing an element by index in a list is O(1)
    return data[index]

print(constant_time_example([10, 20, 30, 40, 50], 2))  # Example usage

'''    SPACE COMPLEXITY EXPLANATION '''
def constant_space_example(n):
    # This function uses O(1) space regardless of input size
    a = 10


              # O(log N) - LOGARITHMIC TIME
'''    TIME COMPLEXITY EXPLANATION '''
def binary_search(sorted_data, target):
    left, right = 0, len(sorted_data) - 1 # Initialize pointers.

    while left <= right:
        mid = (left + right) // 2 # Find the middle index. it floors automatically.
        if sorted_data[mid] == target:
            return mid
        elif sorted_data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1  # Target not found

print(binary_search([1, 3, 5, 7, 9, 11, 31, 245, 1982], 7))  # Example usage

'''    SPACE COMPLEXITY EXPLANATION  '''
def logarithmic_space_example(n):
    # This function uses O(log N) space due to recursion depth
    if n <= 1:
        return n
    return logarithmic_space_example(n // 2) + 1

logarithmic_space_example(16)  # Example usage


           # O(N) - LINEAR TIME
'''    TIME COMPLEXITY EXPLANATION '''
def linear_time_example(data):
    # Iterating through all elements in a list is O(N)
    for item in data:
        print(item)

linear_time_example([10, 20, 30, 40, 50])  # Example usage

'''    SPACE COMPLEXITY EXPLANATION '''
def linear_space_example(n):
    # This function uses O(N) space to store the list
    result = []
    for i in range(n):
        result.append(i)
    return result
linear_space_example(5)  # Example usage


            # O(N log N) - LINEARITHMIC TIME
'''
            TIME COMPLEXITY EXPLANATION
- Merge Sort is a classic example of an O(N log N) algorithm.
- It divides the list into halves (log N) and then merges them back together (N).
- How it works:
    * Divide the list into halves until each sublist contains a single element. (log N divisions)
    * Merge the sublists back together in sorted order. (N merges)
    * Thus the overall time complexity is O(N log N).

- Understanding the merge_sort(data[:mid]) and merge_sort(data[mid:]) calls:
    * `merge_sort(data[:mid])` recursively sorts the left half of the list.
    * `merge_sort(data[mid:])` recursively sorts the right half of the list.

- what happens when the value is passed to merge_sort is less than or equal to 1?
    * When the length of the list is less than or equal to 1, the base case is reached, and the function returns the list as is, since a list with one or zero elements is already sorted.

- The merge function combines two sorted lists into one sorted list by comparing the elements of both lists and appending the smaller element to the result list until all elements from both lists are merged.
- To optimize further, we could implement in-place merging to reduce space complexity, but that would complicate the algorithm.
    EG.
        def merge(left, right):
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result    

- To print the sorted result, you can modify the merge_sort function to print the final sorted list after the merge operation.            
'''
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    print(f"the array of the left is {data[:mid]}")  # Print the left half being merged
    left_half = merge_sort(data[:mid])
    print(f"the array of the right is {data[mid:]}")  # Print the right half being merged    
    right_half = merge_sort(data[mid:])
    print(f"Merging {list(left_half)} and {list(right_half)}")  # Print the two halves before merging

    print(f"the merge value is {list(merge(left_half, right_half))}")  # Print the merged result
    return merge(left_half, right_half)

print(list(merge_sort([38, 27, 43, 3, 9, 82, 10])))  # Example usage


'''   
            SPACE COMPLEXITY EXPLANATION   
- why does logarithmic space have a +1 in the return statement while the linearithmic space has +n?
    * In logarithmic space, the +1 accounts for the current function call in the recursion stack, while in linearithmic space, the +n accounts for the additional space used to store elements during the merge process.
    * In the logarithmic space complexity function, there is no additional space required for merging.
'''
def linearithmic_space_example(n):
    # This function uses O(N log N) space due to the merge sort process
    if n <= 1:
        return n
    return linearithmic_space_example(n // 2) + n

linearithmic_space_example(8)  # Example usage


                # O(N^2) - QUADRATIC TIME
'''    
        TIME COMPLEXITY EXPLANATION 
- Bubble Sort is a classic example of an O(N^2) algorithm.
- It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- This process is repeated until the list is sorted.        
'''
def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]  # Swap
    return data

bubble_sort([64, 34, 25, 12, 22, 11, 90])  # Example usage


            # CUBIC TIME - O(N^3)
'''   
        TIME COMPLEXITY EXPLANATION
- A classic example of an O(N^3) algorithm is the naive approach to matrix multiplication.
- In this approach, we use three nested loops to multiply two matrices.
- Each element in the resulting matrix is computed by taking the dot product of the corresponding row from the first matrix and the column from the second matrix.
'''
def matrix_multiply(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])  # Example usage

                # FACTORIAL TIME - O(N!)
'''
        TIME COMPLEXITY EXPLANATION
- A classic example of an O(N!) algorithm is generating all permutations of a list.
- The number of permutations of a list of size N is N!, which means the time complexity grows factorially with the size of the input.
'''
def generate_permutations(data):
    if len(data) == 0:
        return [[]]
    
    permutations = []
    for i in range(len(data)):
        current = data[i]
        remaining = data[:i] + data[i+1:]
        for p in generate_permutations(remaining):
            permutations.append([current] + p)
    return permutations

generate_permutations([1, 2, 3])  # Example usage


                # EXPONENTIAL TIME - O(2^N)
'''
        TIME COMPLEXITY EXPLANATION
- A classic example of an O(2^N) algorithm is the recursive calculation of Fibonacci numbers.
- Each call to the Fibonacci function results in two additional calls, leading to an exponential growth in the number of calls as N increases.
- Real use cases for the fibonacci sequence include:
    * Computer algorithms (e.g., Fibonacci heap data structure)
    * Biological settings (e.g., branching in trees, arrangement of leaves on a stem)
    * Financial markets (e.g., technical analysis and trading strategies)
'''
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(5)  # Example usage