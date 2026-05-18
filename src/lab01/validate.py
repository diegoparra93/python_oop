def validate_name(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Name cannot be empty")
    return name.strip()


def validate_email(email):
    if not isinstance(email, str) or "@" not in email:
        raise ValueError("Invalid email address")
    return email


def validate_blood_type(blood_type):
    valid = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    if blood_type not in valid:
        raise ValueError("Invalid blood type")
    return blood_type


def validate_weight(weight):
    if not isinstance(weight, (int, float)) or weight <= 0:
        raise ValueError("Weight must be positive")
    return weight


def validate_age(age):
    if not isinstance(age, int) or age <= 0:
        raise ValueError("Age must be greater than 0")
    return age


def validate_city(city):
    if not isinstance(city, str) or not city.strip():
        raise ValueError("City cannot be empty")
    return city.strip()