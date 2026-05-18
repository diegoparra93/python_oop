# Laboratory Work 3: Inheritance and Class Hierarchy

## 1. Purpose of the Work

The goal of this laboratory work is to understand:

- class inheritance
- building class hierarchies
- the difference between base and derived classes
- code reuse using inheritance
- method overriding and polymorphism

---

## 2. Implemented Class Hierarchy

### Base Class

**User**

The base class represents a general user in the system.  
It contains common attributes such as:

- name
- email
- age
- weight
- blood type
- city

It also includes validation, properties, and basic behavior such as checking if a user is an adult.

---

### Derived Classes

#### RegularUser

Represents a standard user of the system.

Additional attributes:
- login_count

Additional behavior:
- tracks how many times the user has logged in

---

#### PremiumUser

Represents a premium user with extended privileges.

Additional attributes:
- subscription_level

Additional behavior:
- identifies premium membership level

---

### Key Differences

- RegularUser focuses on activity (login count)
- PremiumUser focuses on subscription level
- Both inherit common logic from User
- Each class overrides behavior differently

---

## 3. Demonstration (demo.py)

### Scenario 1: Creating Different Types of Users

Demonstrates:
- creation of RegularUser and PremiumUser
- printing objects
- use of overridden __str__ method

📸 (insert screenshot)

---

### Scenario 2: Polymorphism

Demonstrates:
- calling the same method on different objects
- different behavior depending on object type

📸 (insert screenshot)

---

### Scenario 3: Working with Collection

Demonstrates:
- storing different types of users in one collection
- iterating through collection
- type checking using isinstance()

📸 (insert screenshot)

---

## 4. Conclusion

In this laboratory work, the following concepts were learned:

- inheritance
- class hierarchy design
- polymorphism
- method overriding
- reuse of base class logic