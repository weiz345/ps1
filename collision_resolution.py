import time
import random
import string

class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        # Check if key already exists -> update
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def get(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False


class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size
        self.tombstone = object()

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for _ in range(self.size):
            if self.keys[index] is None or self.keys[index] is self.tombstone:
                self.keys[index] = key
                self.values[index] = value
                return
            elif self.keys[index] == key:
                self.values[index] = value
                return
            index = (index + 1) % self.size
        raise Exception("Hash table is full")

    def get(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.keys[index] is None:
                return None
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def remove(self, key):
        index = self._hash(key)
        for _ in range(self.size):
            if self.keys[index] is None:
                return False
            if self.keys[index] == key:
                self.keys[index] = self.tombstone
                self.values[index] = None
                return True
            index = (index + 1) % self.size
        return False


def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def compare_performance():
    separate_chaining = SeparateChainingHashTable(20000)
    linear_probing = LinearProbingHashTable(20000)
    test_data = [(generate_random_string(10), i) for i in range(10000)]

    # Insert performance
    sc_insert_start = time.time()
    for key, value in test_data:
        separate_chaining.insert(key, value)
    sc_insert_end = time.time()

    lp_insert_start = time.time()
    for key, value in test_data:
        linear_probing.insert(key, value)
    lp_insert_end = time.time()

    print(f"Separate Chaining insert time: {sc_insert_end - sc_insert_start:.6f}")
    print(f"Linear Probing insert time: {lp_insert_end - lp_insert_start:.6f}")

    # Lookup performance
    sc_lookup_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        separate_chaining.get(key)
    sc_lookup_end = time.time()

    lp_lookup_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        linear_probing.get(key)
    lp_lookup_end = time.time()

    print(f"Separate Chaining lookup time: {sc_lookup_end - sc_lookup_start:.6f}")
    print(f"Linear Probing lookup time: {lp_lookup_end - lp_lookup_start:.6f}")

    # Remove performance
    sc_remove_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        separate_chaining.remove(key)
    sc_remove_end = time.time()

    lp_remove_start = time.time()
    for _ in range(1000):
        key, _ = random.choice(test_data)
        linear_probing.remove(key)
    lp_remove_end = time.time()

    print(f"Separate Chaining remove time: {sc_remove_end - sc_remove_start:.6f}")
    print(f"Linear Probing remove time: {lp_remove_end - lp_remove_start:.6f}")


if __name__ == "__main__":
    compare_performance()
