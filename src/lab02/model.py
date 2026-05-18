from datetime import datetime
from lab02 import validate


class User:
    total_users = 0

    def __init__(self, name, blood_type, weight, age, email, city):
        self._name = validate.validate_name(name)
        self._blood_type = validate.validate_blood_type(blood_type)
        self._weight = validate.validate_weight(weight)
        self._age = validate.validate_age(age)
        self._email = validate.validate_email(email)
        self._city = validate.validate_city(city)

        self._created_at = datetime.now()

        User.total_users += 1

    # ===== PROPERTIES =====
    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def blood_type(self):
        return self._blood_type

    @property
    def weight(self):
        return self._weight

    @property
    def age(self):
        return self._age

    @property
    def city(self):
        return self._city

    @property
    def created_at(self):
        return self._created_at

    # ===== SETTER WITH VALIDATION =====
    @age.setter
    def age(self, value):
        self._age = validate.validate_age(value)

    # ===== BUSINESS METHODS =====
    def is_adult(self):
        return self._age >= 18

    def update_city(self, new_city):
        self._city = validate.validate_city(new_city)
        print(f"User {self._name} moved to {self._city}")

    # ===== MAGIC METHODS =====
    def __str__(self):
        return (
            f"User: {self._name}\n"
            f"Email: {self._email}\n"
            f"Age: {self._age}\n"
            f"City: {self._city}\n"
            f"Created: {self._created_at.strftime('%Y-%m-%d %H:%M')}"
        )

    def __repr__(self):
        return f"User(name='{self._name}', email='{self._email}', age={self._age})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self._email == other._email