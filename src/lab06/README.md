# Laboratory Work 6 - Generics and Typing

## Goal of the Work

The purpose of this laboratory work is to study:

- type annotations in Python
- Generic classes
- TypeVar
- Protocol
- structural typing

---

# Implemented Generic Classes

## TypedCollection[T]

A generic collection class that stores typed objects.

Implemented methods:

- add()
- remove()
- get_all()
- find()
- filter()
- map()

The collection supports different object types through TypeVar.

---

# Implemented TypeVars

## T

Used as the main generic type for collection items.

## R

Used for map() transformations where the result type changes.

## D

Bound to the Displayable protocol.

## S

Bound to the Scorable protocol.

---

# Implemented Protocols

## Displayable

Requires:

```python
display() -> str