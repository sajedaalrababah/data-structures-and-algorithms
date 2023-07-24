class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        """
        Sets the key-value pair in the hashtable, handling collisions as needed.
        If the given key already exists, replaces its value with the new value.

        Args:
            key: The key to set in the hashtable.
            value: The corresponding value for the key.

        Returns:
            None
        """
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        """
        Retrieves the value associated with the given key from the hashtable.

        Args:
            key: The key to retrieve the value for.

        Returns:
            The value associated with the given key, or None if the key doesn't exist.
        """
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def has(self, key):
        """
        Checks if the given key exists in the hashtable.

        Args:
            key: The key to check for existence.

        Returns:
            bool: True if the key exists in the hashtable, False otherwise.
        """
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return True
        return False

    def keys(self):
        """
        Returns a collection of all unique keys in the hashtable.

        Returns:
            list: A list of all unique keys in the hashtable.
        """
        keys = []
        for bucket in self.table:
            for kvp in bucket:
                keys.append(kvp[0])
        return list(set(keys))

    def hash(self, key):
        """
        Calculates the hash value of the given key.

        Args:
            key: The key to calculate the hash value for.

        Returns:
            int: The hash value of the key.
        """
        return self._hash(key)