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
        self.count = 0  # number of key-value pairs
        self.load_factor_threshold = 0.7

    def calculate_load_factor(self):
        return self.count / self.size

    def insert(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))
        self.count += 1

        # Check load factor
        if self.calculate_load_factor() > self.load_factor_threshold:
            self.resize()

    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def resize(self):
        old_table = self.table
        old_size = self.size
        self.size *= 2  # double the table size
        self.table = [[] for _ in range(self.size)]
        self.count = 0  # will be updated by reinsertion

        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)  # rehash into new table

dht = DynamicHashTable(4)

dht.insert("apple", 1)
dht.insert("banana", 2)
dht.insert("cherry", 3)
print("Load factor:", dht.calculate_load_factor())  # 0.75 triggers resize

print(dht.get("banana"))  # 2
dht.remove("banana")
print(dht.get("banana"))  # None
