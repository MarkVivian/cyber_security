            # --- HASH TABLE IMPLEMENTATION (O(1) Complexity) ---
'''
- A hash table is a data structure that maps keys to values for highly efficient lookup.
- It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
- Uses a math function to find exact location of data. Insufficient for range queries.

- It has a time complexity of O(1) for average case lookups, insertions, and deletions.
- However, in the worst case (due to collisions), the time complexity can degrade to O(n).

- This implementation uses chaining to handle collisions.
    * Chaining involves maintaining a list of all elements that hash to the same index.
    * When a collision occurs, the new element is simply added to the list at that index.
    * The prime number 31 is used in the hash function to help distribute keys more uniformly across the table.
        > 31 is chosen because it is an odd prime, which helps in reducing collisions.
        > This is the industry standard for string hashing in many programming languages.

    
'''
class HashTable:
    def __init__(self, size):
        self.size = size
        # Create an empty list of "None"
        self.table = [ [] for _ in range(size) ]

    # 1. The Hashing Algorithm (Simple Sum)
    def _get_hash(self, key):
        ascii_sum = 0
        print(f"ascii value is {ascii_sum} ")
        for char in key:
            ascii_sum = (ascii_sum * 31 + ord(char)) # ord() gets the ASCII number
        
        # The Modulo ensures the index fits in our table size
        return ascii_sum % self.size 

    # 2. Add Data
    def add(self, key, value):
        index = self._get_hash(key)
        self.table[index].append((key, value)) # Put value in that slot
        print(f"Inserted '{key}' at Index {index}")

    def get(self, key):
        index = self._get_hash(key)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                print(f"Found '{key}' at Index {index} with value: {v}")
        return None

    # 3. Visualizer
    def print_table(self):
        print("\n--- VISUAL VIEW OF TABLE ---")
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item}")
        print("----------------------------\n")


# --- EXECUTION ---
# Let's create a small table of size 5
my_db = HashTable(9)

# Example 1: Simple Insert
my_db.add("Cat", "Cat Data") 
# "Cat" sum is 280. 280 % 5 = 0. Goes to Index 0.

my_db.add("God", "God Data")
# "God" sum is 297. 297 % 5 = 2. Goes to Index 2.

my_db.add("Dog", "Dog Data")
# "Dog" sum is 297. 297 % 5 = 2. Goes to Index 2.

my_db.print_table()

# Example 2: THE COLLISION (The "Act" Problem)
my_db.add("Act", "Act Data") 
# "Act" sum is 280. 280 % 5 = 0. 
# OOPS! It overwrote "Cat Data"!

my_db.print_table()

my_db.get("Dog")  # Should return "Dog Data"