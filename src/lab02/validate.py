def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Name must be a string")

    if not name.strip():
        raise ValueError("Name cannot be empty")

    return name.strip()


def validate_email(email):
    if not isinstance(email, str):
        raise TypeError("Email must be a string")

    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")

    return email


def validate_blood_type(blood_type):
    valid_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

    if blood_type not in valid_types:
        raise ValueError(f"Blood type must be one of: {', '.join(valid_types)}")

    return blood_type


def validate_weight(weight):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")

    if weight <= 0:
        raise ValueError("Weight must be greater than 0")

    return weight


def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")

    if age <= 0:
        raise ValueError("Age must be greater than 0")

    return age


def validate_city(city):
    if not isinstance(city, str):
        raise TypeError("City must be a string")

    if not city.strip():
        raise ValueError("City cannot be empty")

    return city.strip()