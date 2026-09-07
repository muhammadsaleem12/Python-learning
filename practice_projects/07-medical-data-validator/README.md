# 🏥 Medical Data Validator

A Python project that validates the **structure and contents of medical records**.

The validator checks whether the data is in the expected format, whether each dictionary contains the correct keys, and whether individual values follow the required rules.

This project was built to practice **data validation, regular expressions, dictionaries, lists, functions, loops, and type checking**.

---

## 🎯 What Does It Validate?

Each medical record is expected to contain these six fields:

```text
patient_id
age
gender
diagnosis
medications
last_visit_id
```

The program performs **two levels of validation**.

### 1. Structure Validation

First, it checks whether the overall data has the correct structure.

For example:

* The input must be a `list` or `tuple`
* Each record must be a `dictionary`
* Each dictionary must contain exactly the expected keys

For example, this is valid:

```python
{
    'patient_id': 'P1001',
    'age': 34,
    'gender': 'Female',
    'diagnosis': 'Hypertension',
    'medications': ['Lisinopril'],
    'last_visit_id': 'V2301'
}
```

But a record with a missing or unexpected key will be rejected.

---

### 2. Value Validation

After the structure is correct, the program checks the actual values.

For example:

| Field           | Requirement                            |
| --------------- | -------------------------------------- |
| `patient_id`    | String matching `P` followed by digits |
| `age`           | Integer and at least 18                |
| `gender`        | `male` or `female`                     |
| `diagnosis`     | String or `None`                       |
| `medications`   | List containing only strings           |
| `last_visit_id` | String matching `V` followed by digits |

The checks are designed to validate the **format and type of the data**, rather than whether the medical information itself is medically correct.

---

## 🔍 Regular Expressions

The project uses Python's `re` module to validate the ID formats.

### Patient ID

```python
re.fullmatch(r'p\d+', patient_id, re.IGNORECASE)
```

This expects:

```text
P1001
p1002
P12345
```

The pattern means:

* `p` → must start with the letter `p`
* `\d+` → followed by one or more digits
* `re.IGNORECASE` → accepts both uppercase and lowercase `P`

The same idea is used for visit IDs:

```python
re.fullmatch(r'v\d+', last_visit_id, re.IGNORECASE)
```

---

## 🧩 How the Program Works

The validation process can be thought of as:

```text
Medical Records
       │
       ▼
Is it a list or tuple?
       │
       ▼
Are the records dictionaries?
       │
       ▼
Do they contain the correct keys?
       │
       ▼
Are the individual values valid?
       │
       ▼
Valid / Invalid
```

If a problem is found, the program reports where it occurred.

For example:

```text
Unexpected format 'age: 16' at position 2.
```

The `position` helps identify which record contains the problem.

---

## 🧠 Main Functions

### `validate(data)`

This is the main validation function.

It checks:

* Overall data type
* Individual record types
* Dictionary keys
* Individual field values

It returns:

```python
True
```

when everything is valid, and:

```python
False
```

when one or more problems are found.

---

### `find_invalid_records(...)`

This function handles the validation of the individual fields.

It creates a dictionary containing the validation result for every field:

```python
constraints = {
    'patient_id': ...,
    'age': ...,
    'gender': ...,
    'diagnosis': ...,
    'medications': ...,
    'last_visit_id': ...
}
```

It then returns the names of the fields that failed validation.

This keeps the detailed value checks separate from the main `validate()` function.

---

## 🛠️ Python Concepts Practiced

This project helped me practice several Python concepts together:

* `import`
* Regular expressions with `re`
* Functions
* Function arguments
* `**kwargs` / dictionary unpacking
* Dictionaries
* Lists
* Tuples
* Sets
* `isinstance()`
* `all()`
* `enumerate()`
* List comprehensions
* Conditional expressions
* Loops
* Boolean expressions
* String methods such as `.lower()`
* Error/validation messages

---

## ▶️ Running the Project

Make sure Python is installed, then run:

```bash
python main.py
```

The sample data is passed to:

```python
validate(medical_records)
```

If all records follow the expected format:

```text
Valid format.
```

Otherwise, the program reports the invalid records or fields.

---

## 💡 What I Learned

The main thing I learned from this project is that **checking data isn't just about checking whether the values are correct**.

There are different levels of validation.

For example:

```text
Is the data a list?
        ↓
Is each item a dictionary?
        ↓
Does the dictionary have the right keys?
        ↓
Are the values the correct types?
        ↓
Do the values follow the required format?
```

This project helped me understand how these different checks can be combined to validate structured data.

It also gave me more practice with regular expressions and made me think more carefully about how real-world data needs to be validated before a program can safely work with it.

---

## 🚀 Possible Improvements

Some things I could improve in a future version:

* Add more detailed validation rules
* Collect all errors and return them as structured data
* Add unit tests
* Create a reusable validation system
* Read records from a JSON or CSV file
* Add support for more patient fields
* Separate validation logic into different modules

---

**Built with Python 🐍**
