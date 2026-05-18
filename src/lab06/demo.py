from container import TypedCollection

from models import RegularUser, PremiumUser


# =========================
# ADDING METHODS FOR PROTOCOLS
# =========================

def user_display(self) -> str:
    return f"{self.name} ({self.email})"


def user_score(self) -> float:
    return float(self.age)


RegularUser.display = user_display
PremiumUser.display = user_display

RegularUser.score = user_score
PremiumUser.score = user_score


# =========================
# SCENARIO 1
# =========================

def scenario1():

    print("\nSCENARIO 1: TypedCollection")

    users = TypedCollection[RegularUser]()

    user1 = RegularUser(
        "Diego",
        25,
        "d@mail.com",
        "Moscow",
        10
    )

    user2 = RegularUser(
        "Tom",
        19,
        "t@mail.com",
        "Berlin",
        5
    )

    users.add(user1)
    users.add(user2)

    for user in users:
        print(user.name, "-", user.city)


# =========================
# SCENARIO 2
# =========================

def scenario2():

    print("\nSCENARIO 2: find(), filter(), map()")

    users = TypedCollection[PremiumUser]()

    users.add(
        PremiumUser(
            "Anna",
            30,
            "a@mail.com",
            "Madrid",
            "Gold"
        )
    )

    users.add(
        PremiumUser(
            "Eva",
            40,
            "e@mail.com",
            "Rome",
            "VIP"
        )
    )

    found = users.find(lambda x: x.name == "Anna")

    print("\nFound user:")
    print(found.name if found else "None")

    not_found = users.find(lambda x: x.name == "Mike")

    print("\nUser not found:")
    print(not_found)

    filtered = users.filter(lambda x: x.age > 35)

    print("\nFiltered users:")

    for user in filtered:
        print(user.name)

    names = users.map(lambda x: x.name)

    print("\nMapped names:")
    print(names)

    ages = users.map(lambda x: x.age)

    print("\nMapped ages:")
    print(ages)


# =========================
# SCENARIO 3
# =========================

def scenario3():

    print("\nSCENARIO 3: Protocols")

    users = TypedCollection()

    users.add(
        RegularUser(
            "Chris",
            21,
            "c@mail.com",
            "Paris",
            3
        )
    )

    users.add(
        PremiumUser(
            "Sophia",
            35,
            "s@mail.com",
            "London",
            "Platinum"
        )
    )

    print("\nDisplay methods:")

    for user in users:
        print(user.display())

    print("\nScore methods:")

    for user in users:
        print(user.score())


# =========================
# MAIN
# =========================

def main():

    scenario1()
    scenario2()
    scenario3()


if __name__ == "__main__":
    main()