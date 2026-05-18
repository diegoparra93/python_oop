import sys
import os

sys.path.append(os.path.abspath("src/lab01"))

import validate
from datetime import datetime


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

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def age(self):
        return self._age

    def is_adult(self):
        return self._age >= 18

    def __str__(self):
        return f"User: {self._name} | Email: {self._email} | Age: {self._age}"

    def __repr__(self):
        return f"User(name='{self._name}', email='{self._email}', age={self._age})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self._email == other._email