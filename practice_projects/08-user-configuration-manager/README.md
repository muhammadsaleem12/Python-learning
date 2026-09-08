# ⚙️ User Configuration Manager

A simple Python utility for managing user settings through a dictionary.

The program allows you to **add, update, delete, and view** settings while checking whether a setting already exists before making changes.

It was built as a practical exercise to strengthen my understanding of **dictionaries, functions, conditionals, string methods, and loops**.

---

## ✨ Features

* ➕ Add new settings
* 🔄 Update existing settings
* 🗑️ Delete settings
* 👀 View all current settings
* 🚫 Prevent adding duplicate settings
* ⚠️ Handle attempts to update or delete settings that don't exist

Example settings:

```python
{
    "theme": "dark",
    "language": "english",
    "brightness": "medium"
}
```

---

## 🧩 How It Works

The project is split into four simple functions:

### `add_setting()`

Adds a new setting if the key doesn't already exist.

```text
Setting 'volume' added with value 'high' successfully!
```

### `update_setting()`

Changes the value of an existing setting.

```text
Setting 'theme' updated to 'light' successfully!
```

### `delete_setting()`

Removes a setting from the configuration.

```text
Setting 'language' deleted successfully!
```

### `view_settings()`

Displays all currently stored settings in a readable format.

```text
Current User Settings:
Theme: light
Brightness: medium
Volume: high
```

---

## 🛠️ Python Concepts Practiced

* Dictionaries
* Functions
* `if / elif`
* `in` operator
* Dictionary `.items()`
* Adding and deleting dictionary entries
* String `.lower()` and `.capitalize()`
* Loops
* Tuples
* Function arguments
* Returning values

---

## ▶️ Run

```bash
python main.py
```

The included test calls demonstrate each of the four operations.

---

## 🧠 What I Learned

This project gave me more practice working with dictionaries as actual **data storage** rather than just using them for simple examples.

I also got more comfortable designing separate functions for different operations and using conditions to control what happens when a setting exists or doesn't exist.

It's a small project, but it's another step toward being able to use Python concepts together to build useful programs.

**Built with Python 🐍**
