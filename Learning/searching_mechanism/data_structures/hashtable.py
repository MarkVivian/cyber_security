class HashTables:
    # create the buckets for the hash table
    def __init__(self, size=10):
        self.size : int = size
        self.buckets : list[list[tuple[str, str]]] = [[] for i in range(size)]
        # the bucket will look like this: [[], [], [], [], [], [], [], [], [], []]
        # the bucket with data : [[("key1", "value1")], [], [("key2", "value2")], [], [], [], [], [], [], []]

    # hash function to convert the key into an index for the bucket
    def _hash_index(self, key) -> int:
        total : int = 0
        for char in key:
            # ord function returns the unicode code point for a single character
            total += ord(char)

        return total % self.size # the modulus operator ensures that the index is within the bounds of the bucket size 
        # the modulus always returns a value between 0 and size-1, which is the valid range of indices for the bucket list
        # e.g 127 % 10 = 7, so the key will be stored in bucket index 7
        # 149 % 10 = 9, so the key will be stored in bucket index 9 


    def set(self, key, value) -> None :
        # compute the index for the key using the hash function
        index : int = self._hash_index(key)
        # retrieve the bucket at the computed index
        bucket : list[tuple[str, str]] = self.buckets[index]

        # check if the key already exists in the bucket, if it does, update the value.
        # if the bucket is empty this loop will be skipped and the new key-value pair will be added to the bucket.
        for i, (ky, vl) in enumerate(bucket):
            if ky == key:
                bucket[i] = (key, value)
                return 
        # if the key does not exist in the bucket, add a new key-value pair to the bucket.
        bucket.append((key, value))


    def get(self, key) -> str | None :
        index : int = self._hash_index(key)
        bucket : list[tuple[str, str]] = self.buckets[index]

        for i, (ky, vl) in enumerate(bucket):
            if ky == key:
                print(f"found key {key} with value {vl}")
                return ky 
            
        print(f"key {key} not found in bucket index {index}")
        return None 
    

    def delete(self, key):
        index : int = self._hash_index(key)
        bucket : list[tuple[str, str]] = self.buckets[index]

        for i, (ky, vl) in enumerate(bucket):
            if ky == key:
                # remove the key-value pair from the bucket using the pop method, which removes the item at the specified index and returns it.
                bucket.pop(i)
                return 

            

ht = HashTables()
ht.set("name",  "Mark")
ht.set("city",  "Nanyuki")
ht.set("field", "cybersecurity")

print(ht.get("name"))    # Mark
print(ht.get("city"))    # Nanyuki
print(ht.get("field"))   # cybersecurity

ht.set("name", "Mark K.")    # update existing key
print(ht.get("name"))         # Mark K.

ht.delete("city")
print(ht.get("city"))         # None