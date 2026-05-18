from models import PremiumUser, RegularUser

from collection import UserCollection

from strategies import (
    by_name,
    by_age,
    by_city,
    is_adult,
    is_premium,
    make_age_filter,
    AgeIncreaseStrategy,
    PremiumLabelStrategy
)


def print_collection(title, collection):

    print(f"\n{title}")

    for item in collection:
        print(item.name, "-", item.age, "-", item.city)


def scenario1():

    print("\nSCENARIO 1: FILTER → SORT → APPLY")

    users = UserCollection()

    users.add(RegularUser(
        "Diego",
        25,
        "d@mail.com",
        "Moscow",
        10
    ))

    users.add(PremiumUser(
        "Anna",
        30,
        "a@mail.com",
        "Berlin",
        "Gold"
    ))

    users.add(RegularUser(
        "Tom",
        17,
        "t@mail.com",
        "Paris",
        3
    ))

    users.add(PremiumUser(
        "Eva",
        40,
        "e@mail.com",
        "Madrid",
        "VIP"
    ))

    users.add(RegularUser(
        "Mike",
        22,
        "m@mail.com",
        "Rome",
        5
    ))

    print_collection("Original collection:", users)

    adults = users.filter_by(is_adult)

    print_collection("Adults only:", adults)

    sorted_users = adults.sort_by(by_age)

    print_collection("Sorted by age:", sorted_users)

    increased = sorted_users.apply(AgeIncreaseStrategy())

    print_collection("After increasing age:", increased)


def scenario2():

    print("\nSCENARIO 2: CHANGING STRATEGIES")

    users = UserCollection()

    users.add(PremiumUser(
        "Sophia",
        28,
        "s@mail.com",
        "London",
        "Platinum"
    ))

    users.add(RegularUser(
        "Chris",
        21,
        "c@mail.com",
        "Toronto",
        4
    ))

    strategy = PremiumLabelStrategy()

    result = users.apply(strategy)

    print("\nUsing PremiumLabelStrategy:")

    for item in result:
        print(item)


def scenario3():

    print("\nSCENARIO 3: FUNCTION FACTORY + LAMBDA")

    users = UserCollection()

    users.add(RegularUser(
        "Alex",
        19,
        "alex@mail.com",
        "Prague",
        2
    ))

    users.add(PremiumUser(
        "Maria",
        35,
        "maria@mail.com",
        "Warsaw",
        "Gold"
    ))

    users.add(RegularUser(
        "Kevin",
        16,
        "kevin@mail.com",
        "Lisbon",
        1
    ))

    age_filter = make_age_filter(20)

    filtered = users.filter_by(age_filter)

    print_collection("Users older than 20:", filtered)

    names = list(map(lambda x: x.name, users))

    print("\nNames using lambda + map:")
    print(names)


def main():

    scenario1()
    scenario2()
    scenario3()


if __name__ == "__main__":
    main()