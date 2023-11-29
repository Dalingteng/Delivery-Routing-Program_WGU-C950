# Create HashTable class using chaining
class HashTable:
    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert a new item into hash table and update the existed item in hash table
    def insert(self, key, item):
        # get the bucket list where this item will go
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # update the item if it is already in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True
        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Search for an item in hash table with matching key
    # Return the item if found, or None if not found
    def search(self, key):
        # get the bucket list where this key would be
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # search for the key in the bucket list
        for kv in bucket_list:
            if kv[0] == key:
                return kv[1]
        return None

    # Remove an item from hash table with matching key
    def remove(self, key):
        # get the bucket list where this item will be removed from
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # remove the item from the bucket list if it is found
        if key in bucket_list:
            bucket_list.remove(key)
