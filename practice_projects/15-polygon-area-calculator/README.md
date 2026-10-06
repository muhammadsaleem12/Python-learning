# 📐 Polygon Area Calculator

A Python project that uses **Object-Oriented Programming (OOP)** to model rectangles and squares and perform different geometric calculations.

The project demonstrates how a `Square` can inherit functionality from a `Rectangle` while maintaining its own rules for equal width and height.

## ✨ Features

The calculator can:

* 📏 Calculate the **area**
* 📐 Calculate the **perimeter**
* 🔺 Calculate the **diagonal**
* 🖼️ Generate a simple **ASCII picture**
* 📦 Determine how many times one shape can fit inside another
* 🔄 Change the dimensions of rectangles and squares
* 🧬 Demonstrate inheritance between `Rectangle` and `Square`

## 🧱 Project Structure

```text
Polygon Area Calculator
│
├── Rectangle
│   ├── Width & height
│   ├── Area
│   ├── Perimeter
│   ├── Diagonal
│   ├── Picture
│   └── Amount of another shape inside
│
└── Square
    ├── Inherits from Rectangle
    ├── Keeps equal dimensions
    └── Adds set_side()
```

## 🧠 Python Concepts Practiced

This project focuses heavily on **Object-Oriented Programming**.

### Classes & Objects

`Rectangle` and `Square` are classes used to create shape objects.

```python
rect = Rectangle(10, 5)
sq = Square(9)
```

### Inheritance

`Square` inherits from `Rectangle`:

```python
class Square(Rectangle):
```

This allows the square to reuse methods such as:

```text
get_area()
get_perimeter()
get_diagonal()
get_picture()
get_amount_inside()
```

### `super()`

The square uses:

```python
super().__init__(side, side)
```

to initialize the rectangle portion of the object while giving the square equal width and height.

### Method Overriding

`Square` overrides methods such as:

```text
set_width()
set_height()
__str__()
```

because a square must always maintain equal dimensions.

## 📊 Example

A rectangle with a width of `16` and height of `8` can contain a square with a side of `4`.

```text
Rectangle: 16 × 8
Square:     4 × 4
```

The calculator determines how many complete squares can fit:

```text
4 × 2 = 8 squares
```

## 🖼️ Shape Pictures

The project can also generate a simple text representation.

For example:

```text
*****
*****
*****
```

This represents a rectangle with a width of `5` and height of `3`.

If either dimension is greater than `50`, the program prevents an excessively large picture from being generated.

## 🚀 Running the Project

Make sure Python is installed, then run:

```bash
python main.py
```

Example output will include calculations such as:

```text
50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8
```

## 🎯 What This Project Teaches

The main purpose of this project is not just calculating geometric formulas.

It demonstrates an important OOP relationship:

```text
             Rectangle
                 │
                 │ inherits
                 ▼
              Square
```

A square is a specialized type of rectangle in this implementation, but it needs additional rules to make sure its width and height always remain equal.

This makes the project a practical exercise in **inheritance, method overriding, object state, and code reuse**.

---

**Built with Python 🐍**

*Another step forward in learning Object-Oriented Programming.*
