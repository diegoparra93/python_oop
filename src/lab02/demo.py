from model import User
from collection import UserCollection


def scenario1():
    print("\nSCENARIO 1: Basic operations")

    collection = UserCollection("Main Users")

    user1 = User("Diego", "O+", 75.5, 25, "diego@email.com", "Madrid")
    user2 = User("Daniel", "A-", 80.0, 17, "daniel@email.com", "Barcelona")
    user3 = User("Sofia", "B+", 60.0, 30, "sofia@email.com", "Madrid")

    collection.add(user1)
    collection.add(user2)
    collection.add(user3)

    print(f"Total users: {len(collection)}")

    for user in collection:
        print(user)

    collection.remove(user3)

    print("\nAfter removal:")
    for user in collection:
        print(user)


def scenario2():
    print("\nSCENARIO 2: Search and validation")

    collection = UserCollection()

    user1 = User("Diego", "O+", 75.5, 25, "diego@email.com", "Madrid")
    user2 = User("Sofia", "B+", 60.0, 30, "sofia@email.com", "Madrid")

    collection.add(user1)
    collection.add(user2)

    found = collection.find_by_email("diego@email.com")
    print(f"Found by email: {found}")

    madrid_users = collection.find_by_city("Madrid")
    print(f"Users in Madrid: {len(madrid_users)}")

    # Duplicate test
    try:
        collection.add(user1)
    except ValueError as e:
        print(f"Duplicate error: {e}")

    # Wrong type test
    try:
        collection.add("not a user")
    except TypeError as e:
        print(f"Type error: {e}")


def scenario3():
    print("\nSCENARIO 3: Indexing, sorting and filtering")

    collection = UserCollection()

    collection.add(User("Zoe", "O+", 70, 20, "z@mail.com", "Paris"))
    collection.add(User("Anna", "A+", 55, 22, "a@mail.com", "Berlin"))
    collection.add(User("Mike", "B+", 80, 17, "m@mail.com", "Rome"))

    print(f"First user: {collection[0]}")
    print(f"Last user: {collection[-1]}")

    collection.remove_at(1)

    print("\nAfter removing index 1:")
    for user in collection:
        print(user)

    collection.sort_by_name()

    print("\nAfter sorting:")
    for user in collection:
        print(user)

    adults = collection.get_adults()

    print("\nAdult users:")
    for user in adults:
        print(user)


def main():
    print("UserCollection demonstration")

    scenario1()
    scenario2()
    scenario3()


if __name__ == "__main__":
    main()