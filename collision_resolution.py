import time
import random
import string

class SeparateChainingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # TODO: Implement for 12.4
        pass

    def insert(self, key, value):
        # TODO: Implement for 12.4
        pass

    def get(self, key):
        # TODO: Implement for 12.4
        pass

    def remove(self, key):
        # TODO: Implement for 12.4
        pass

class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash(self, key):
        # TODO: Implement for 12.4
        pass

    def insert(self, key, value):
        # TODO: Implement for 12.4
        pass

    def get(self, key):
        # TODO: Implement for 12.4
        pass

    def remove(self, key):
        # TODO: Implement for 12.4
        pass

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def compare_performance():
    separate_chaining = SeparateChainingHashTable(10000)
    linear_probing = LinearProbingHashTable(10000)
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

    print(f"Separate Chaining insert time: {sc_insert_end - sc_insert_start}")
    print(f"Linear Probing insert time: {lp_insert_end - lp_insert_start}")

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

    print(f"Separate Chaining lookup time: {sc_lookup_end - sc_lookup_start}")
    print(f"Linear Probing lookup time: {lp_lookup_end - lp_lookup_start}")

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

    print(f"Separate Chaining remove time: {sc_remove_end - sc_remove_start}")
    print(f"Linear Probing remove time: {lp_remove_end - lp_remove_start}")

if __name__ == "__main__":
    compare_performance()