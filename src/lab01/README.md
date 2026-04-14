# ЛР-1 — Класс и инкапсуляция (Python 3.x)

## Цель работы

* Освоить объявление пользовательских классов.
* Разобраться с инкапсуляцией (атрибуты экземпляра, закрытые поля).
* Реализовать свойства (`@property`).
* Переопределить магические методы (`__str__`, `__repr__`, `__eq__`).
* Осознать разницу между атрибутами класса и экземпляра.

---

# Результат лабораторной

## Демонстрация

### Код программы (demo.py)

```python
from user import User

print("=== USER CLASS DEMONSTRATION ===\n")

# 1. CREATING VALID OBJECTS
try:
    diego = User("Diego", "O+", 75.5, 25, "diego@email.com", "Madrid")
    daniel = User("Daniel", "A-", 80.0, 17, "daniel@email.com", "Barcelona")
    print("Users created successfully")
except ValueError as e:
    print(f"Unexpected error: {e}")

# 2. DISPLAY USER INFORMATION (__str__)
print("\n--- USER INFORMATION ---")
print(diego)
print(daniel)

# 3. CLASS ATTRIBUTE
print("\n--- CLASS ATTRIBUTE ---")
print(f"Total users created: {User.total_users}")

# 4. BUSINESS METHOD (is_adult)
print("\n--- AGE VERIFICATION ---")
if diego.is_adult():
    print(f"{diego._name} is an adult")
else:
    print(f"{diego._name} is not an adult")

if daniel.is_adult():
    print(f"{daniel._name} is an adult")
else:
    print(f"{daniel._name} is not an adult")

# 5. COMPARISON (__eq__)
print("\n--- USER COMPARISON ---")
if diego == daniel:
    print("Diego and Daniel are the same user (same email)")
else:
    print("Diego and Daniel are different users")

# 6. VALIDATION DEMONSTRATION (with try/except)
print("\n--- VALIDATION DEMONSTRATION ---")

try:
    invalid_user = User("Error", "O+", 70, 30, "invalid-email", "Seville")
except ValueError as e:
    print(f"Error captured (invalid email): {e}")

try:
    invalid_user = User("Error", "O+", 70, 30, "test@email.com", "")
except ValueError as e:
    print(f"Error captured (empty city): {e}")

try:
    invalid_user = User("Error", "O+", 70, -5, "test@email.com", "Valencia")
except ValueError as e:
    print(f"Error captured (negative age): {e}")

print("\n=== END OF DEMONSTRATION ===")
---
```
## Демонстрация

Результат выполнения программы:

![demo](../../images/lab01/run1.png)