# Media Catalogue

A small Python project for managing movies and TV series in a single media catalogue.

The project uses **object-oriented programming, inheritance, validation, and custom exceptions** to build a simple catalogue that can store and display different types of media.

> This is a practice project created as part of my Python learning journey.

## Features

* Add movies to a catalogue
* Add TV series using inheritance
* Validate media information
* Prevent invalid titles, years, directors, and durations
* Validate seasons and episode counts
* Use a custom `MediaError` for catalogue-specific errors
* Separate movies and TV series when displaying the catalogue
* Format media information with `__str__`
* Handle errors with `try` / `except`

## How It Works

The project has three main classes:

```text
                 Movie
                   │
                   ▼
               TVSeries

              MediaCatalogue
                   │
              ┌────┴────┐
              ▼         ▼
            Movie    TVSeries
```

`Movie` acts as the parent class, while `TVSeries` extends it with additional information such as seasons and total episodes.

`MediaCatalogue` stores both types of media and can display them separately.

## `Movie`

The `Movie` class stores:

* Title
* Release year
* Director
* Duration

It also validates the supplied information when a movie is created.

For example:

```python
movie = Movie(
    'The Matrix',
    1999,
    'The Wachowskis',
    136
)
```

## `TVSeries`

`TVSeries` inherits from `Movie`.

This means it gets the common movie information while adding:

* Number of seasons
* Total number of episodes

For example:

```python
series = TVSeries(
    'Breaking Bad',
    2008,
    'Vince Gilligan',
    47,
    5,
    62
)
```

Using `super().__init__()` allows the parent `Movie` class to handle the shared attributes and validation.

## `MediaCatalogue`

The `MediaCatalogue` class maintains a list of media objects.

It provides methods to:

* Add media items
* Retrieve movies
* Retrieve TV series
* Display the complete catalogue

The catalogue checks that only `Movie` or `TVSeries` objects can be added.

## Custom Exception

The project includes a custom `MediaError` exception:

```python
class MediaError(Exception):
    ...
```

It is used when an invalid object is passed to the catalogue.

The exception also stores the object that caused the error, making it possible to inspect what could not be added.

## Validation

The project validates data at the time objects are created.

Examples include:

```text
Empty title       → ValueError
Year before 1895 → ValueError
Empty director    → ValueError
Invalid duration  → ValueError
Invalid seasons   → ValueError
Invalid episodes  → ValueError
Invalid catalogue object → MediaError
```

This keeps invalid data from entering the system.

## Example Output

With the sample data, the catalogue produces output similar to:

```text
Media Catalogue (4 items):

=== MOVIES ===
1. The Matrix (1999) - 136 min, The Wachowskis
2. Inception (2010) - 148 min, Christopher Nolan
=== TV SERIES ===
1. Scrubs (2001) - 9 seasons, 182 episodes, 24 min avg, Bill Lawrence
2. Breaking Bad (2008) - 5 seasons, 62 episodes, 47 min avg, Vince Gilligan
```

## Concepts Practiced

This project brought together several important Python concepts:

* Classes and objects
* Inheritance
* `super()`
* Custom exceptions
* Exception handling
* `try` / `except`
* `raise`
* Validation
* `isinstance()`
* Lists of objects
* List comprehensions
* `type()`
* `enumerate()`
* `__str__`
* Object-oriented design

## What I Learned

This project gave me more practical experience with **inheritance and exceptions**.

The `TVSeries` class helped reinforce how a child class can reuse functionality from a parent class while adding its own attributes and validation.

I also practiced creating a custom exception instead of relying only on Python's built-in exceptions.

Another useful part was making the catalogue work with different media types while still keeping their individual behavior and information.

This was a good exercise in thinking about how several classes can work together as one small system.

---

A small practice project from my Python learning journey.
