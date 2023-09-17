# HASH TABLES

## Introduction

A hash table is a data structure that stores key-value pairs. It uses a hash function to map the key to a location in the table, where the value is stored. This allows fast look-up and retrieval of values based on the key.

## Implementation

The following is a simple implementation of a hash table in Python:

```python
class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def set(self, key, value):
        index = self.hash(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash(key)
        return self.table[index]

## Usage

To use the hash table, we first need to create an instance of the `HashTable` class. We then use the `set()` method to add key-value pairs to the table. The `get()` method can be used to retrieve the value associated with a given key.

The following example shows how to use the hash table:

```python
hash_table = HashTable(10)
hash_table.set("name", "John Doe")
hash_table.set("age", 30)

print(hash_table.get("name"))  # Output: John Doe
print(hash_table.get("age"))  # Output: 30
```
## Collision Handling

When two keys hash to the same location in the table, a collision occurs. There are several ways to handle collisions, such as:

* **Open addressing:** This involves probing for the next available location in the table.
* **Chaining:** This involves creating a linked list of key-value pairs at the collision location.
* **Double hashing:** This involves using a second hash function to map the key to a different location in the table.

The following code shows how to handle collisions using open addressing:

```python
class HashTable:
        def __init__(self, size):
                self.size = size
                self.table = [None] * size
        def hash(self, key):
                return key % self.size

        def set(self, key, value):
