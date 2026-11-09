# Breadth First Search Algorithm — Python

Generate every valid combination of `n` pairs of parentheses using a **breadth-first search (BFS)** approach.

The program builds combinations one character at a time and only adds a closing parenthesis when doing so keeps the sequence valid.

## Example

For two pairs:

```python
gen_parentheses(2)
```

Output:

```python
["(())", "()()"]
```

For three pairs:

```python
["((()))", "(()())", "(())()", "()(())", "()()()"]
```

## Run the project

1. Make sure Python 3 is installed.
2. Open a terminal in this project folder.
3. Run:

   ```bash
   python main.py
   ```

## How it works

Each queue item contains three values:

- `current`: the parentheses string built so far.
- `opens_used`: the number of opening parentheses added.
- `closes_used`: the number of closing parentheses added.

The algorithm follows two rules:

1. Add `(` only while fewer than `pairs` opening parentheses have been used.
2. Add `)` only when `closes_used < opens_used`, so a closing parenthesis always has an opening one to match.

When the string reaches `2 * pairs` characters, it is complete and is added to the results.

## Concepts practiced

- Breadth-first search (BFS)
- Queues and tuples
- Loops and conditional logic
- Building strings incrementally
- Tracking state with counters
- Validating function arguments
- Generating valid combinations without first creating invalid ones

## A note on the approach

This project uses a Python list as a queue and removes items with `pop(0)`. That is straightforward for learning; for larger searches, `collections.deque` is generally more efficient for removing items from the front.

---

*Python learning project — Parentheses Generator.*
