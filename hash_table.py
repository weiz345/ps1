class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # TODO: Implement for 12.1
        pass

    def insert(self, key, value):
        # TODO: Implement for 12.2
        pass

    def get(self, key):
        # TODO: Implement for 12.2
        pass

    def remove(self, key):
        # TODO: Implement for 12.2
        pass
            
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