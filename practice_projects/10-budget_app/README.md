# Budget App

A simple Python budget management application built around **object-oriented programming**.

The app allows you to create different spending categories, record deposits and withdrawals, transfer money between categories, check available funds, and generate a visual spending chart.

## Features

* Create budget categories
* Deposit money into a category
* Withdraw money when sufficient funds are available
* Check the current balance
* Transfer money between categories
* Display a formatted ledger for each category
* Generate a vertical spending chart showing percentage spent by category

## How It Works

Each budget category is represented by a `Category` object.

Every category contains:

* A name
* A ledger containing its transactions

For example:

```text
**************Food**************
initial deposit       1000.00
groceries               -10.15
restaurant              -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

The spending chart then calculates how much of the total spending belongs to each category:

```text
Percentage spent by category
100| 
 90| 
 80| 
 70| 
 60| 
 50| 
 40| 
 30| o  
 20| o  
 10| o  o  
  0| o  o  
    ---------
     F  C  
     o  l  
     o  o  
     d  t  
        h  
        i  
        n  
        g
```

## Main Components

### `Category`

The `Category` class manages everything related to a budget category.

Important methods:

* `deposit()` — adds money to the ledger
* `withdraw()` — removes money if enough funds are available
* `get_balance()` — calculates the current balance
* `check_funds()` — checks whether a withdrawal is possible
* `transfer()` — moves money between categories
* `__str__()` — creates a readable representation of the ledger

### `create_spend_chart()`

This function analyzes the spending of all supplied categories and creates a vertical percentage chart.

It:

1. Finds the total amount spent.
2. Calculates each category's percentage of spending.
3. Rounds percentages down to the nearest 10.
4. Builds the chart from 100% to 0%.
5. Displays category names vertically.

## Concepts Practiced

This project brought several Python concepts together:

* Classes and objects
* Constructors and instance attributes
* Instance methods
* Lists and dictionaries
* Loops
* Conditional statements
* Functions
* String slicing
* String formatting and alignment
* Arithmetic calculations
* Negative values for withdrawals
* Object-to-object interaction
* `__str__`
* Working with collections of objects

## Example

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")

clothing = Category("Clothing")
clothing.deposit(500, "salary")

food.transfer(50, clothing)

print(food)
print(clothing)

print(create_spend_chart([food, clothing]))
```

## What I Learned

This project helped me move beyond simply creating classes and start thinking about **how multiple objects interact with each other**.

The `transfer()` method was especially useful because one `Category` object has to modify its own ledger while also updating another object's ledger.

The spending chart also gave me practice turning raw transaction data into a structured visual representation using calculations, loops, and string formatting.

## Future Improvements

* Add a command-line menu
* Save budgets to a file
* Load previous budgets when the program starts
* Add transaction dates
* Add monthly spending limits
* Improve the spending chart
* Add input validation

## Running the Project

Make sure Python is installed, then run:

```bash
python main.py
```

---

Built as part of my Python learning journey while practicing object-oriented programming and working with structured data.
