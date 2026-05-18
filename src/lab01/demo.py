from lab01.validate import User

def scenario1():
    print("\nSCENARIO 1: Creation and display")

    user1 = User("Diego", "O+", 75.5, 25, "diego@email.com", "Madrid")
    user2 = User("Daniel", "A-", 80.0, 17, "daniel@email.com", "Barcelona")

    print(user1)
    print(user2)

    print(f"repr: {repr(user1)}")


def scenario2():
    print("\nSCENARIO 2: Class attribute and business method")

    user1 = User("Diego", "O+", 75.5, 25, "diego@email.com", "Madrid")

    print(f"Total users: {User.total_users}")

    if user1.is_adult():
        print(f"{user1.name} is an adult")
    else:
        print(f"{user1.name} is not an adult")


def scenario3():
    print("\nSCENARIO 3: Comparison")

    user1 = User("Diego", "O+", 75.5, 25, "diego@email.com", "Madrid")
    user2 = User("Daniel", "A-", 80.0, 17, "daniel@email.com", "Barcelona")
    user3 = User("Test", "O+", 70, 30, "diego@email.com", "Seville")

    print(f"user1 == user2: {user1 == user2}")
    print(f"user1 == user3: {user1 == user3}")


def scenario4():
    print("\nSCENARIO 4: Validation")

    try:
        User("Error", "O+", 70, 30, "invalid-email", "Seville")
    except ValueError as e:
        print(f"Email error: {e}")

    try:
        User("Error", "O+", 70, 30, "test@email.com", "")
    except ValueError as e:
        print(f"City error: {e}")

    try:
        User("Error", "O+", 70, -5, "test@email.com", "Valencia")
    except ValueError as e:
        print(f"Age error: {e}")


def main():
    print("User class demonstration")

    scenario1()
    scenario2()
    scenario3()
    scenario4()


if __name__ == "__main__":
    main()