# Game Character Stats Tracker

A small Python practice project that simulates the basic stats of a game character.

The project uses **properties and setters** to control the character's health and mana, making sure their values always stay within the allowed limits. It also includes a simple level-up system that restores the character's stats.

> This is a small practice project created while learning Python OOP.

## Features

* Create a game character with a name
* Track health, mana, and level
* Keep health between `0` and `100`
* Keep mana between `0` and `50`
* Automatically prevent stats from going outside their limits
* Level up the character
* Restore health and mana after leveling up
* Display character stats in a readable format

## How It Works

A `GameCharacter` starts with:

```text
Level  → 1
Health → 100
Mana   → 50
```

For example:

```python
kratos = GameCharacter('Kratos')
```

creates:

```text
Name: Kratos
Level: 1
Health: 100
Mana: 50
```

The character's stats can then be changed:

```python
kratos.health = 20
kratos.mana = 5
```

And when the character levels up:

```python
kratos.level_up()
```

the level increases and health and mana are restored to their maximum values.

## Stat Limits

| Stat   | Minimum | Maximum |
| ------ | ------- | ------- |
| Health | 0       | 100     |
| Mana   | 0       | 50      |

The setters automatically enforce these limits.

For example:

```python
kratos.health = 150
```

will result in:

```text
Health: 100
```

And:

```python
kratos.mana = -10
```

will result in:

```text
Mana: 0
```

## Main Components

### `GameCharacter`

The `GameCharacter` class contains the character's:

* Name
* Health
* Mana
* Level

### Properties

The project uses properties for:

* `name`
* `health`
* `mana`
* `level`

The `health` and `mana` setters are responsible for keeping the stats within their valid ranges.

### `level_up()`

The `level_up()` method:

1. Increases the character's level by `1`.
2. Restores health to `100`.
3. Restores mana to `50`.
4. Prints a level-up message.

## Example

```python
kratos = GameCharacter('Kratos')

kratos.mana = 5
kratos.health = 20

print(kratos)

kratos.level_up()

print(kratos)
```

Output:

```text
Name: Kratos
Level: 1
Health: 20
Mana: 5

Kratos leveled up to 2!

Name: Kratos
Level: 2
Health: 100
Mana: 50
```

## Concepts Practiced

This project was mainly practice for:

* Classes and objects
* Constructors
* Instance attributes
* Properties
* Getters
* Setters
* Encapsulation
* Validating attribute values
* Methods
* `__str__`
* Incrementing values
* Working with object state

## What I Learned

This project gave me more practice with **properties and setters**.

Instead of allowing health and mana to contain any value, the setters act as a simple safeguard around the character's stats.

It also helped me understand that an object's state can change through methods like `level_up()` while still keeping certain rules enforced by its properties.

This is a small project, but it was useful practice for thinking about how objects should manage and protect their own data.

---

A small practice project from my Python learning journey.
