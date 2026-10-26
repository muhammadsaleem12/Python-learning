# 🗼 Tower of Hanoi — Python

A beginner-friendly Python implementation of the **Tower of Hanoi** puzzle. The program solves the puzzle recursively and records the arrangement of all three rods after every move.

## How the puzzle works

The puzzle starts with all disks stacked on the first rod, largest at the bottom and smallest at the top. The goal is to move every disk to the third rod.

**Rules**
- Move only one disk at a time.
- Move only the top disk from a rod.
- Never place a larger disk on top of a smaller disk.

## Example

For `n = 3`, the first and last arrangements are:

```text
[3, 2, 1] [] []
...
[] [] [3, 2, 1]
```

Each line shows the contents of the first, second, and third rods, separated by spaces.

## Run it

1. Make sure Python is installed.
2. Save the code as `hanoi_solver.py`.
3. Run:

   ```bash
   python hanoi_solver.py
   ```

To try another number of disks, change the final call, for example:

```python
print(hanoi_solver(4))
```

## How the solution works

The `helper()` function uses recursion. For each task, it:

1. Moves `num_disks - 1` disks to the auxiliary rod.
2. Moves one disk to the destination rod and records the arrangement.
3. Moves the smaller disks from the auxiliary rod to the destination.

The starting arrangement is recorded before the first move. `rstrip("\n")` removes the extra newline at the very end of the returned string while preserving the line breaks between arrangements.

## Move count

The minimum number of moves for `n` disks is:

```text
2**n - 1
```

The output contains one additional arrangement for the initial state, so it has `2**n` lines in total.

## What I practiced

- Lists and list methods (`pop()` and `append()`)
- Nested functions and `nonlocal`
- Recursion and a base case
- Building a multiline string
- Matching an exact expected output format

## Learning project

Built while practicing Python through the freeCodeCamp Python curriculum.
