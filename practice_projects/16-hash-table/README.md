# 🗂️ Hash Table — Python

A simple hash table implementation built from scratch using Python. This project demonstrates how keys can be converted into hash values to store, retrieve, and remove data efficiently while handling hash collisions.

Instead of relying on Python's built-in dictionary for the entire implementation, this project uses a custom `HashTable` class to explore the underlying concepts.

## ✨ Features

- 🔑 **Hashing:** Converts strings into numeric hash values.
- ➕ **Add:** Stores key-value pairs in the collection.
- 🔍 **Lookup:** Retrieves values using their original keys.
- 🗑️ **Remove:** Deletes a specific key-value pair.
- 🤝 **Collision Handling:** Stores multiple keys with the same hash value in a nested dictionary.
- 🧹 **Automatic Cleanup:** Removes empty buckets after deleting their last key.

## 🧪 Example

```python
table = HashTable()

table.add("cat", 10)
table.add("act", 20)

print(table.lookup("cat"))  # 10
print(table.lookup("act"))  # 20

table.remove("cat")

print(table.lookup("cat"))  # None
print(table.lookup("act"))  # 20
```

### Output

```text
10
20
None
20
```

## ⚙️ How It Works

### 1. Hashing

The `hash()` method adds the Unicode values of each character in a string using Python's built-in `ord()` function.

For example, `"cat"` and `"act"` produce the same hash because they contain the same characters, even though their order differs.

This creates a **hash collision**.

### 2. Collision Handling

To handle collisions, the collection stores a nested dictionary at each hash value.

Conceptually, the data looks like this:

```text
collection
└── hash value
    ├── "cat": 10
    └── "act": 20
```

Both keys can exist at the same hash value because the nested dictionary stores them separately.

### 3. Adding and Looking Up Values

The `add()` method calculates the hash, creates a bucket if necessary, and stores the key-value pair.

The `lookup()` method calculates the same hash and checks the bucket for the exact key. If the key doesn't exist, it returns `None`.

### 4. Removing Values

The `remove()` method deletes only the requested key. If the bucket becomes empty, it removes that bucket from the main collection.

## 🧠 Python Concepts Practiced

- Classes and objects
- Constructors and instance attributes
- Dictionaries and nested dictionaries
- Loops and conditional statements
- Functions and return values
- The `ord()` function
- Hashing and hash collisions
- Adding, retrieving, and deleting data
- Checking whether keys exist
- Handling missing keys without raising an error

## 🚀 How to Run

Make sure Python is installed and save the code in `main.py`.

Run the program:

```bash
python main.py
```

## ⚠️ Limitations

This is a learning implementation rather than a production-ready hash table.

- The hash function is intentionally simple and can produce many collisions.
- The collection uses Python dictionaries internally to manage buckets.
- The implementation does not resize or rehash its collection.
- Hash values are not guaranteed to be unique for different keys.

## 🎯 Project Goal

The goal of this project is to understand how hashing, key-value storage, and collision handling work together.

Building this implementation helps develop a foundation for understanding data structures and the design choices behind dictionary-like collections.

---

**Built with Python 🐍**

*A hands-on project exploring hash tables and key-value data structures.*