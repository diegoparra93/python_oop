from models import RegularUser, PremiumUser

from exceptions import (
    UserNotFoundError,
    DuplicateUserError
)

from storage import save, load


class UserApp:

    def __init__(self) -> None:

        self._users = load("users.json")

    def get_all_users(self) -> list:
        """Return all users."""

        return self._users

    def add_regular_user(
        self,
        name: str,
        age: int,
        email: str,
        city: str,
        login_count: int
    ) -> None:
        """Add regular user."""

        self._check_duplicate(email)

        user = RegularUser(
            name,
            age,
            email,
            city,
            login_count
        )

        self._users.append(user)

    def add_premium_user(
        self,
        name: str,
        age: int,
        email: str,
        city: str,
        membership_level: str
    ) -> None:
        """Add premium user."""

        self._check_duplicate(email)

        user = PremiumUser(
            name,
            age,
            email,
            city,
            membership_level
        )

        self._users.append(user)

    def find_user(self, email: str):
        """Find user by email."""

        for user in self._users:

            if user.email == email:
                return user

        return None

    def delete_user(self, email: str) -> None:
        """Delete user."""

        user = self.find_user(email)

        if not user:
            raise UserNotFoundError(
                f"User '{email}' not found."
            )

        self._users.remove(user)

    def sort_users(self, strategy: str) -> list:
        """Sort users."""

        if strategy == "name":

            return sorted(
                self._users,
                key=lambda x: x.name
            )

        elif strategy == "age":

            return sorted(
                self._users,
                key=lambda x: x.age
            )

        elif strategy == "city":

            return sorted(
                self._users,
                key=lambda x: x.city
            )

        return self._users

    def filter_adults(self) -> list:
        """Return adult users."""

        return [
            user
            for user in self._users
            if user.age >= 18
        ]

    def save_data(self) -> None:
        """Save data to file."""

        save(self._users, "users.json")

    def _check_duplicate(self, email: str) -> None:
        """Check duplicate email."""

        for user in self._users:

            if user.email == email:

                raise DuplicateUserError(
                    f"User '{email}' already exists."
                )