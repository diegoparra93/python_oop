import json

from models import RegularUser, PremiumUser


def save(users, filepath: str) -> None:
    """Save users to JSON file."""

    data = []

    for user in users:

        if isinstance(user, RegularUser):

            data.append({
                "type": "regular",
                "name": user.name,
                "age": user.age,
                "email": user.email,
                "city": user.city,
                "login_count": user.login_count
            })

        elif isinstance(user, PremiumUser):

            data.append({
                "type": "premium",
                "name": user.name,
                "age": user.age,
                "email": user.email,
                "city": user.city,
                "membership_level": user.membership_level
            })

    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)


def load(filepath: str) -> list:
    """Load users from JSON file."""

    users = []

    try:

        with open(filepath, "r") as file:
            data = json.load(file)

            for item in data:

                if item["type"] == "regular":

                    users.append(
                        RegularUser(
                            item["name"],
                            item["age"],
                            item["email"],
                            item["city"],
                            item["login_count"]
                        )
                    )

                elif item["type"] == "premium":

                    users.append(
                        PremiumUser(
                            item["name"],
                            item["age"],
                            item["email"],
                            item["city"],
                            item["membership_level"]
                        )
                    )

    except FileNotFoundError:
        return []

    return users