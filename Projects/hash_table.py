class HashTable:
    def __init__(self) -> None:
        self.collection = {}

    def hash(self, key: str) -> int:
    # returns a hashed value computed as the sum of the Unicode (ASCII) values of each character in the string.
        return sum(ord(c) for c in key)

    def add(self, key: str, value) -> None:
    # Adds a key-value to the hash table.
        hashed_value = self.hash(key)
        if hashed_value in self.collection:
            self.collection[hashed_value][key] = value
        else:
            self.collection[hashed_value] = {key: value}

    def remove(self, key: str) -> None:
    # Removes the corresponding key-value pair from the hash table.
        hashed_value = self.hash(key)
        if hashed_value in self.collection and key in self.collection[hashed_value]:
            self.collection[hashed_value].pop(key, None)

    def lookup(self, key: str):
    # Returns the corresponding value stored inside the hash table. If the key does not exist in the collection returns None.
        hashed_value = self.hash(key)
        if hashed_value in self.collection and key in self.collection[hashed_value]:
            return self.collection[hashed_value][key]
        return None
