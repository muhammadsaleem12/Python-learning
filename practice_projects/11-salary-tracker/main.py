class Employee:
    # Class attribute: minimum salary for each employee level
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }
    # Creates a new Employee
    def __init__(self, name, level):
        self.name = name
        self.level = level
        # Get the base salary for the employee's level
        self.salary = Employee._base_salaries[level]

    # Controls how the object looks when printed
    def __str__(self):
        return f'{self.name}: {self.level}'

    # Controls how the object is represented for developers
    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    # ---------------- NAME ----------------

    # Getter: allows us to use employee.name
    @property
    def name(self):
        return self._name

    # Setter: controls what happens when employee.name = something
    @name.setter
    def name(self, new_name):
        # Make sure the name is a string
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    # ---------------- LEVEL ----------------

    # Getter
    @property
    def level(self):
        return self._level

    # Setter: controls changing the employee's level
    @level.setter
    def level(self, new_level):

        # Level must be a string
        if not isinstance(new_level, str):
            raise TypeError("'level' must be a string.")
        # Check that the level actually exists
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        # Don't allow selecting the same level again
        if hasattr(self, '_level') and new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        # Don't allow an employee to move to a lower level
        if hasattr(self, '_level') and Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")

        # Update salary according to the new level
        self.salary = Employee._base_salaries[new_level]
        # Store the new level
        self._level = new_level


    # ---------------- SALARY ----------------

    # Getter
    @property
    def salary(self):
        return self._salary

    # Setter: controls changing salary
    @salary.setter
    def salary(self, new_salary):
        # Salary must be a number
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        # Salary cannot be below the minimum for the employee's level
        if hasattr(self, '_level') and new_salary < Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')

# Testing the Code by Creating the Employee Object.
charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'