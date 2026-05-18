from models import RegularUser, PremiumUser
from interfaces import Printable, Loginable


def print_all(items):
    for item in items:
        print(item.to_string())


def login_all(items):
    for item in items:
        print(item.login())


def scenario1():
    print("SCENARIO 1: Creating objects")

    user1 = RegularUser(
        "Diego",
        25,
        "diego@mail.com",
        "Moscow",
        15
    )

    user2 = PremiumUser(
        "Anna",
        30,
        "anna@mail.com",
        "Saint Petersburg",
        "Gold"
    )

    print(user1.to_string())
    print(user2.to_string())


def scenario2():
    print("\nSCENARIO 2: Polymorphism")

    users = [
        RegularUser(
            "Tom",
            21,
            "tom@mail.com",
            "London",
            7
        ),

        PremiumUser(
            "Eva",
            28,
            "eva@mail.com",
            "Berlin",
            "Platinum"
        )
    ]

    login_all(users)


def scenario3():
    print("\nSCENARIO 3: isinstance and interfaces")

    user = PremiumUser(
        "Mike",
        35,
        "mike@mail.com",
        "Madrid",
        "VIP"
    )

    print(isinstance(user, PremiumUser))
    print(isinstance(user, Printable))
    print(isinstance(user, Loginable))


def main():
    scenario1()
    scenario2()
    scenario3()


if __name__ == "__main__":
    main()