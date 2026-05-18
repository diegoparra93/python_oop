from lab03.base import User


class RegularUser(User):
    def __init__(self, name, blood_type, weight, age, email, city, login_count):
        super().__init__(name, blood_type, weight, age, email, city)
        self._login_count = login_count

    def get_user_type(self):
        return "Regular User"

    def __str__(self):
        return f"{super().__str__()} | Type: Regular | Logins: {self._login_count}"


class PremiumUser(User):
    def __init__(self, name, blood_type, weight, age, email, city, subscription_level):
        super().__init__(name, blood_type, weight, age, email, city)
        self._subscription_level = subscription_level

    def get_user_type(self):
        return "Premium User"

    def __str__(self):
        return f"{super().__str__()} | Type: Premium | Level: {self._subscription_level}"