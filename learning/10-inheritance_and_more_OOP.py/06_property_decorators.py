'''Property Decorators'''
# Property (Getter): A decorator (@property) that turns a class method into a read-only attribute. It allows you to access the return value of a method using simple dot notation (object.name) without using parentheses ().

# Setter: A decorator (@<property_name>.setter) that allows you to intercept and validate data when someone tries to assign a new value to a property using the assignment operator (object.name = "value").


class Employee:

    # The PROPERTY (Getter) - Triggers when you READ e.name
    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    # The SETTER - Triggers when you WRITE to e.name
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


# --- Testing the Code ---
e = Employee()

# 1. This triggers the SETTER. It automatically creates e.fname and e.lname
e.name = "Kevin Levin"

# 2. This proves the setter worked behind the scenes
print(e.fname)  # Output: Kevin
print(e.lname)  # Output: Levin

# 3. This triggers the PROPERTY (Getter) to combine them back together
print(e.name)  # Output: Kevin Levin


# The Property (Getter) is like a window. Anyone can look through it to see what is inside, but they cannot reach through it to change anything.

# The Setter is like a security guard at the door. If someone brings a new piece of furniture, the guard checks it first. If it passes inspection, the guard places it inside for you.