# 📧 Email Simulator

A small **object-oriented email simulator** built with Python.

The project simulates a basic email system where users can send emails to each other, check their inbox, read messages, and delete them.

The main goal was to practice **Object-Oriented Programming by modeling a real-world system with interacting classes**.

---

## ✨ Features

* 📤 Send emails between users
* 📥 Receive and list emails
* 📖 Read individual emails
* ✅ Automatically mark emails as read
* 🗑️ Delete emails
* 🕒 Store the time an email was received
* 🔢 Number emails for easy selection
* ⚠️ Handle invalid email numbers and empty inboxes

---

## 🧩 How It Works

The simulator is built around three main classes:

```text
User
 │
 └── Inbox
      │
      ├── Email-1
      ├── Email-2
      └── Email-3
```

### `User`

Represents a person using the email simulator.

A user can:

* Send emails
* Check their inbox
* Read emails
* Delete emails

### `Inbox`

Manages the emails belonging to a user.

It handles:

* Receiving emails
* Listing emails
* Opening emails
* Deleting emails

### `Email`

Represents an individual email.

It stores:

* Sender
* Receiver
* Subject
* Body
* Timestamp
* Read/unread status

---

## 🧠 Example

The simulator creates two users:

```python
tory = User('Tory')
ramy = User('Ramy')
```

Tory can then send an email to Ramy:

```python
tory.send_email(
    ramy,
    'Hello',
    'Hi Ramy, just saying hello!'
)
```

The email is automatically added to Ramy's inbox.

When Ramy opens it, the email is marked as **read**.

---

## 🛠️ Python Concepts Practiced

* Classes and objects
* Constructors with `__init__`
* Instance attributes
* Instance methods
* Object relationships
* `__str__`
* Lists
* `enumerate()`
* Conditional logic
* Functions
* `datetime`
* Index validation
* `if __name__ == '__main__'`

---

## ▶️ Run

```bash
python main.py
```

The `main()` function demonstrates sending, reading, deleting, and checking emails.

---

## 💡 What I Learned

This project helped me understand OOP from a more practical perspective.

Instead of creating classes just to practice the syntax, I used them to represent **real things and their relationships**.

A `User` has an `Inbox`, and an `Inbox` contains `Email` objects.

This made the purpose of classes, objects, and methods much clearer to me.

**Built with Python 🐍**
