from interfaces import Printable, Loginable


class User:
    total_users = 0

    def __init__(self, name, age, email, city):
        self._name = name
        self._age = age
        self._email = email
        self._city = city

        User.total_users += 1

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def email(self):
        return self._email

    @property
    def city(self):
        return self._city

    def is_adult(self):
        return self._age >= 18

    def get_user_type(self):
        return "Generic User"


class RegularUser(User, Printable, Loginable):

    def __init__(self, name, age, email, city, login_count):
        super().__init__(name, age, email, city)
        self._login_count = login_count

    @property
    def login_count(self):
        return self._login_count

    def login(self):
        return f"{self._name} logged in as Regular User"

    def to_string(self):
        return (
            f"Regular User: {self._name} | "
            f"Email: {self._email} | "
            f"Logins: {self._login_count}"
        )

    def get_user_type(self):
        return "Regular User"


class PremiumUser(User, Printable, Loginable):

    def __init__(self, name, age, email, city, membership_level):
        super().__init__(name, age, email, city)
        self._membership_level = membership_level

    @property
    def membership_level(self):
        return self._membership_level

    def login(self):
        return f"{self._name} logged in as Premium User"

    def to_string(self):
        return (
            f"Premium User: {self._name} | "
            f"Email: {self._email} | "
            f"Level: {self._membership_level}"
        )

    def get_user_type(self):
        return "Premium User"