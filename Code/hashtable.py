#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys
        """Time Complexity -
            Best Case:
            Worst Case:
            """

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)

        return all_values
        """Time Complexity -
            Best Case: O(n/b)
            Average Case: O(n/b)
            As the values() undergoes a for loop, showing everu bucket and the keys inside and
            the values inside these keys,
            it is ideal for this loop to keep going, and show everything, including what
            has been added or removed. This is why both cases would be
            """

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items
        """Time Complexity -
            Best Case: O(n/b)
            Average Case: O(n/b)
            Both cases would loop, as it is the same as the values() but instead of just
            showing the values, it would show the items in the buckets as well.
            """

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        item_count = 0
        for bucket in self.buckets:
            for item in bucket.items():
                item_count += 1

        return item_count
        """Time Complexity -
            Best Case: O(n)
            Average Case: O(n)
            Like the linked lists's length(), the process loops n number of times through all buckets and counts
            the number of key-value entries in each bucket.
            """

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        bucket = self.buckets[hash(key) % len(self.buckets)]
        for item_key, value in bucket.items():
                if item_key == key:
                    return True
        return False
        """Time Complexity -
            Best Case: O(1)
            Average Case: O(n/b)
            The best case would be searching the hash table and finding if the key is true or false in one
            sweep. The average case would be looking through all the buckets first and then finding it.
            """

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[hash(key) % len(self.buckets)]

        for item_key, value in bucket.items():
            if item_key == key:
                return value

        raise KeyError(f'Key not found: {key}')
        """Time Complexity -
            Best Case: O(1)
            Average Case: O(n/b)
            The best case would be the process running once and finding the key right away,
            the average case would be looking through every bucket until it finds the key.
            """

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        bucket = self.buckets[hash(key) % len(self.buckets)]

        item = bucket.find(lambda item: item[0] == key)
        if item != None:
            bucket.replace(item, (key, value))
        else:
            bucket.append((key, value))
        """Time Complexity -
            Best Case: O(1)
            Average Case: O(n/b)
            Set() would have the best case as O(1) because in the best case scenario
            you would want set to run once, as it instantly finds the key and inserts the value.
            An average case would be the process going through each bucket to find said key
            to insert the value into.
            """

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        bucket = self.buckets[hash(key) % len(self.buckets)]

        item = bucket.find(lambda item: item[0] == key)

        if item is not None:
            bucket.delete(item)
        else:
            raise KeyError(f'Key not found: {key}')

        """Time Complexity -
            Best Case: O(1)
            Average Case: O(n/b)
            Delete() would have the best case being O(1) because it means it only ran through
            one process to find and delete the key from the hash table.
            """


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

        print('contains({!r}): {}'.format('X', ht.contains('X')))
        print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

            print('contains(X): {}'.format(ht.contains('X')))
            print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
