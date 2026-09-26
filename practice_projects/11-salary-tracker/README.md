# Salary Tracker

A small Python OOP project for managing employee levels and salaries.

The **Salary Tracker** uses properties and validation to make sure an employee's name, level, and salary follow a set of rules. Employees can be promoted to higher levels, and their salary automatically updates to the minimum salary for that level.

## Features

* Create employees with a name and level
* Automatically assign a base salary based on the employee's level
* Validate employee names and levels
* Prevent invalid employee levels
* Prevent employees from being moved to a lower level
* Prevent selecting the same level again
* Automatically update salary after a promotion
* Prevent salaries from falling below the minimum for the employee's level
* Provide readable `str()` and `repr()` representations

## How It Works

The project defines four employee levels, each with a minimum salary:

```text
Trainee    → $1,000
Junior     → $2,000
Mid-level  → $3,000
Senior     → $4,000
```

When an employee is created, their salary is automatically determined from their level.

For example:

```python
employee = Employee('Charlie Brown', 'trainee')
```

creates an employee with:

```text
Charlie Brown: trainee
Base salary: $1000
```

If the employee is promoted:

```python
employee.level = 'junior'
```

their salary automatically becomes `$2000`.

## The `Employee` Class

The `Employee` class stores:

* `name`
* `level`
* `salary`

It also contains the `_base_salaries` class attribute, which stores the minimum salary associated with each level.

### Name

The `name` property validates that the employee's name is a string before storing it.

### Level

The `level` property controls promotions and validates that:

* The level is a string.
* The level exists.
* The employee isn't selecting their current level again.
* The employee cannot move to a lower level.

### Salary

The `salary` property makes sure that:

* The salary is a number.
* The salary is not below the minimum salary for the employee's current level.

## Example

```python
charlie_brown = Employee('Charlie Brown', 'trainee')

print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')

charlie_brown.level = 'junior'
```

The promotion updates both the employee's level and salary.

## Concepts Practiced

This project focused heavily on Python's object-oriented features:

* Classes and objects
* Class attributes
* Instance attributes
* Properties
* Getters and setters
* Attribute validation
* `TypeError`
* `ValueError`
* `hasattr()`
* `__str__`
* `__repr__`
* Dictionaries
* Encapsulation
* Controlled state changes

## What I Learned

This project helped me understand **properties and setters more practically**.

Instead of allowing attributes to change freely, the setters can control what happens whenever an attribute is assigned.

For example:

```python
employee.level = 'junior'
```

doesn't simply replace a value. Python runs the `level` setter, which validates the new level, checks the employee's current level, updates the salary, and then stores the new value.

This made the idea of **encapsulation and controlled attributes** much clearer.

## Future Improvements

* Add employee IDs
* Add departments and job titles
* Add bonuses and raises
* Track promotion history
* Add multiple employees
* Calculate total payroll
* Save employee data to a file
* Build a command-line interface

---

Built as part of my Python learning journey while practicing object-oriented programming and property-based validation.
