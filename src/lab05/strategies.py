from models import PremiumUser


# =========================
# SORTING STRATEGIES
# =========================

def by_name(user):
    return user.name


def by_age(user):
    return user.age


def by_city(user):
    return user.city


# =========================
# FILTER FUNCTIONS
# =========================

def is_adult(user):
    return user.age >= 18


def is_premium(user):
    return isinstance(user, PremiumUser)


# =========================
# FUNCTION FACTORY
# =========================

def make_age_filter(min_age):

    def filter_fn(user):
        return user.age >= min_age

    return filter_fn


# =========================
# CALLABLE STRATEGIES
# =========================

class AgeIncreaseStrategy:

    def __call__(self, user):
        user._age += 1
        return user


class PremiumLabelStrategy:

    def __call__(self, user):

        if isinstance(user, PremiumUser):
            return f"[PREMIUM] {user.name}"

        return user.name