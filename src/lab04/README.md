# Laboratory Work 4 - Interfaces and Abstract Base Classes

## Goal of the Work

The purpose of this laboratory work is to learn:

- abstract base classes (ABC)
- interfaces in Python
- polymorphism through interfaces
- architecture design using contracts of behavior

---

# Implemented Interfaces

## Printable

This interface requires classes to implement:

- to_string()

Used for displaying object information.

---

## Loginable

This interface requires classes to implement:

- login()

Used for simulating user login behavior.

---

# Implemented Classes

## User

Base class for all users.

Contains:

- name
- email
- age
- city

---

## RegularUser

Inherits from User.

Implements:

- Printable
- Loginable

Additional attribute:

- login_count

---

## PremiumUser

Inherits from User.

Implements:

- Printable
- Loginable

Additional attribute:

- membership_level

---

# Demonstration

## Scenario 1

Creating different user types and displaying their information.

---

## Scenario 2

Demonstrating polymorphism through interface methods.

---

## Scenario 3

Using collections with objects implementing interfaces.

---

# Conclusion

In this laboratory work we studied:

- abstract base classes
- interfaces
- polymorphism
- architecture using contracts
- multiple interface implementation