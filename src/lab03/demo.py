import sys
import os

sys.path.append(os.path.abspath("src"))

from lab02.collection import UserCollection
from lab03.models import RegularUser, PremiumUser

def scenario1():
    print("\nSCENARIO 1: Creating different user types")

    u1 = RegularUser("Diego", "O+", 75, 25, "d@mail.com", "Madrid", 10)
    u2 = PremiumUser("Anna", "A+", 60, 30, "a@mail.com", "Berlin", "Gold")

    print(u1)
    print(u2)


def scenario2():
    print("\nSCENARIO 2: Polymorphism")

    users = [
        RegularUser("Mike", "B+", 80, 20, "m@mail.com", "Rome", 5),
        PremiumUser("Sofia", "O-", 55, 28, "s@mail.com", "Paris", "Platinum")
    ]

    for user in users:
        print(user.get_user_type())


def scenario3():
    print("\nSCENARIO 3: Collection usage")

    collection = UserCollection()

    collection.add(RegularUser("Tom", "A+", 70, 19, "t@mail.com", "London", 3))
    collection.add(PremiumUser("Eva", "B-", 65, 35, "e@mail.com", "Madrid", "Gold"))

    for user in collection:
        print(user)

    for user in collection:
        if isinstance(user, PremiumUser):
            print(f"Premium user found: {user.name}")


def main():
    scenario1()
    scenario2()
    scenario3()


if __name__ == "__main__":
    main()