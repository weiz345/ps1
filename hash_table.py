class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # Step 1: sum ASCII values of all characters
        total = sum(ord(c) for c in key)
        # Step 2: multiply by prime 31
        total *= 31
        # Step 3: modulo table size
        return total % self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        # check if key already exists → update
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # otherwise, append new
        bucket.append((key, value))

    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None  # key not found

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False  # key not found
    
ht = HashTable(1000)

ht.insert("apple", 42)
ht.insert("banana", 99)

print(ht.get("apple"))   # 42
print(ht.get("banana"))  # 99
print(ht.get("cherry"))  # None

ht.remove("apple")
print(ht.get("apple"))   # None
            
class DynamicHashTable(HashTable):
    def __init__(self, size):
        super().__init__(size)
        self.count = 0
        self.load_factor_threshold = 0.7

    def calculate_load_factor(self):
        # TODO: Implement for 12.3
        pass

    def insert(self, key, value):
        # TODO: Implement for 12.3
        pass

    def remove(self, key):
        # TODO: Implement for 12.3
        pass

    def resize(self):
        # TODO: Implement for 12.3
        pass