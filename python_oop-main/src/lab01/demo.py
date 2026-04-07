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

# Case 1: Invalid email
try:
    invalid_user = User("Error", "O+", 70, 30, "invalid-email", "Seville")
    print("This should have failed")
except ValueError as e:
    print(f"Error captured (invalid email): {e}")

# Case 2: Empty city
try:
    invalid_user = User("Error", "O+", 70, 30, "test@email.com", "")
    print("This should have failed")
except ValueError as e:
    print(f"Error captured (empty city): {e}")

# Case 3: Negative age
try:
    invalid_user = User("Error", "O+", 70, -5, "test@email.com", "Valencia")
    print("This should have failed")
except ValueError as e:
    print(f"Error captured (negative age): {e}")

print("\n=== END OF DEMONSTRATION ===")