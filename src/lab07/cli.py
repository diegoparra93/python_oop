from app import UserApp

from exceptions import (
    UserNotFoundError,
    DuplicateUserError
)


class CLI:

    def __init__(self) -> None:

        self._app = UserApp()

    def run(self) -> None:
        """Start CLI loop."""

        while True:

            self._print_menu()

            try:

                choice = int(
                    input("\nChoose option: ")
                )

                if choice == 1:
                    self._add_user()

                elif choice == 2:
                    self._show_users()

                elif choice == 3:
                    self._find_user()

                elif choice == 4:
                    self._delete_user()

                elif choice == 5:
                    self._sort_users()

                elif choice == 0:

                    self._app.save_data()

                    print("\nData saved.")
                    print("Goodbye.")

                    break

                else:
                    print("\nInvalid option.")

            except ValueError:
                print("\nError: enter a valid number.")

            except DuplicateUserError as error:
                print(f"\n{error}")

            except UserNotFoundError as error:
                print(f"\n{error}")

    def _print_menu(self) -> None:

        print("\n========== USER MENU ==========")
        print("1. Add user")
        print("2. Show all users")
        print("3. Find user")
        print("4. Delete user")
        print("5. Sort users")
        print("0. Exit")

    def _add_user(self) -> None:

        user_type = input(
            "\nRegular or Premium? "
        ).lower()

        name = input("Name: ")

        age = int(input("Age: "))

        email = input("Email: ")

        city = input("City: ")

        if user_type == "regular":

            login_count = int(
                input("Login count: ")
            )

            self._app.add_regular_user(
                name,
                age,
                email,
                city,
                login_count
            )

        elif user_type == "premium":

            membership_level = input(
                "Membership level: "
            )

            self._app.add_premium_user(
                name,
                age,
                email,
                city,
                membership_level
            )

        else:
            print("\nInvalid user type.")
            return

        print("\nUser added successfully.")

    def _show_users(self) -> None:

        users = self._app.get_all_users()

        if not users:
            print("\nNo users found.")
            return

        print("\n========== USERS ==========")

        for user in users:

            print(
                f"{user.name} | "
                f"{user.age} | "
                f"{user.email} | "
                f"{user.city}"
            )

    def _find_user(self) -> None:

        email = input("\nEnter email: ")

        user = self._app.find_user(email)

        if not user:
            print("\nUser not found.")
            return

        print(
            f"\nFound: "
            f"{user.name} | "
            f"{user.email}"
        )

    def _delete_user(self) -> None:

        email = input("\nEnter email: ")

        confirm = input(
            f"Delete '{email}'? (y/n): "
        ).lower()

        if confirm != "y":
            print("\nOperation cancelled.")
            return

        self._app.delete_user(email)

        print("\nUser deleted.")

    def _sort_users(self) -> None:

        print("\nSort by:")
        print("1. Name")
        print("2. Age")
        print("3. City")

        choice = input("\nChoose: ")

        strategy = "name"

        if choice == "2":
            strategy = "age"

        elif choice == "3":
            strategy = "city"

        users = self._app.sort_users(strategy)

        print("\n========== SORTED USERS ==========")

        for user in users:

            print(
                f"{user.name} | "
                f"{user.age} | "
                f"{user.city}"
            )