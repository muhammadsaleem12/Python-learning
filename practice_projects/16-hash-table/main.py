class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        total = 0

        for char in string:
            total = total + ord(char)

        return total

    def add(self, key, value):
        index = self.hash(key)  # Calculate the hash index for the key

        if index not in self.collection:  # Check if this index already exists
            self.collection[index] = {}  # Create an empty dictionary at this index

        self.collection[index][key] = value  # Store the key-value pair inside the dictionary

    def remove(self, key):
        index = self.hash(key) # Calculate the Hash of the key

        if index in self.collection: # Check if the hash index exists
            if key in self.collection[index]: # Check if the key exists at that index
                del self.collection[index][key] # Delete only the requested key-value pair

                if not self.collection[index]: # Check if the nested dictionary is empty
                    del self.collection[index] # Delete the empty dictionary from the collection
            

    def lookup(self, key):
        index = self.hash(key)  # Calculate the hash index for the given key

        if index in self.collection:  # Check if that index exists in the collection
            if key in self.collection[index]:  # Check if the exact key exists at that index
                return self.collection[index][key]  # Return the value stored for that key

        return None  # Return None if the index or key doesn't exist




table = HashTable()

table.add("cat", 10)
table.add("act", 20)

print(table.lookup("cat"))  # 10
print(table.lookup("act"))  # 20

table.remove("cat")

print(table.lookup("cat"))  # None
print(table.lookup("act"))  # 20