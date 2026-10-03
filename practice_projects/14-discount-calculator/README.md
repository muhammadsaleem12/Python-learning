# 💰 Discount Calculator

A clean, object-oriented Python project that calculates the **best possible price** for a product by checking multiple discount strategies.

Instead of applying one hard-coded discount, the program evaluates different discount rules and automatically chooses the **lowest valid price**.

## ✨ What Does It Do?

The Discount Calculator supports multiple types of discounts:

* 📊 **Percentage Discount** — reduces the price by a percentage.
* 💵 **Fixed Amount Discount** — subtracts a specific amount from the price.
* 👑 **Premium User Discount** — gives premium users a special discount.
* 🧠 **Best Price Calculation** — compares all applicable discounts and selects the cheapest price.

### Example

For a **$50 Wireless Mouse** purchased by a Premium user:

| Discount          |     Result |
| ----------------- | ---------: |
| Original Price    |     $50.00 |
| 10% Discount      |     $45.00 |
| $5 Fixed Discount |     $45.00 |
| Premium Discount  |     $40.00 |
| **Best Price**    | **$40.00** |

## 🧱 Project Structure

The project demonstrates several important Python OOP concepts:

```text
Discount Calculator
│
├── Product
│   └── Stores product information
│
├── DiscountStrategy
│   └── Defines the interface for discount rules
│
├── PercentageDiscount
│   └── Percentage-based discount
│
├── FixedAmountDiscount
│   └── Fixed-price discount
│
├── PremiumUserDiscount
│   └── Premium-user discount
│
└── DiscountEngine
    └── Finds the best available price
```

## 🧠 Concepts Practiced

This project was built to practice:

* Classes and objects
* Constructors with `__init__`
* Instance attributes
* Methods
* Type hints
* `__str__()`
* Abstract Base Classes (`ABC`)
* Abstract methods
* Inheritance
* Method overriding
* Polymorphism
* Lists and list comprehensions
* Loops
* Conditional logic
* Working with multiple objects
* Comparing calculated values with `min()`

## 🚀 How It Works

The program follows a simple process:

```text
Create Product
     ↓
Create Discount Strategies
     ↓
Check which discounts apply
     ↓
Calculate each applicable price
     ↓
Compare all prices
     ↓
Return the lowest price
```

The `DiscountEngine` doesn't need to know how every discount works. It simply asks each strategy:

> "Does this discount apply?"

If the answer is yes, it calculates the discounted price and adds it to the list of possible prices.

Finally, `min()` finds the lowest price.

## ▶️ Running the Project

Make sure Python is installed, then run:

```bash
python main.py
```

Example output:

```text
Best price for Wireless Mouse for Premium user: $40.00
```

## 🔧 Adding More Discount Types

One of the useful parts of this design is that new discount strategies can be added without rewriting the `DiscountEngine`.

For example, future versions could support:

* 🎂 Birthday discounts
* 🎟️ Coupon codes
* 🛒 Bulk purchase discounts
* 🆕 New-user discounts
* 🎄 Seasonal discounts
* 💎 VIP discounts

Each new discount can have its own rules while following the same `DiscountStrategy` structure.

## 🎯 Project Goal

The goal of this project was not simply to calculate a discounted price.

It was to practice designing a system where **different discount rules can coexist and be easily extended**.

This is a small project, but the same idea of separating different behaviors into independent strategies can be useful in much larger applications.

---

**Built with Python 🐍**

*A small project for practicing Object-Oriented Programming and the Strategy Pattern.*
