from lab02.model import User



class UserCollection:
    def __init__(self, name="Users"):
        self._name = name
        self._items = []

    def add(self, user):
        if not hasattr(user, "name"):
              raise TypeError("Invalid object")

        for existing in self._items:
            if existing.email == user.email:
                raise ValueError(f"User with email '{user.email}' already exists")

        self._items.append(user)
        print(f"User '{user.name}' added to collection '{self._name}'")

    def remove(self, user):
        if user not in self._items:
            raise ValueError("User not found in collection")

        self._items.remove(user)
        print(f"User '{user.name}' removed from collection '{self._name}'")

    def get_all(self):
        return self._items.copy()

    def find_by_email(self, email):
        for user in self._items:
            if user.email == email:
                return user
        return None

    def find_by_city(self, city):
        result = []
        for user in self._items:
            if user.city == city:
                result.append(user)
        return result

    def remove_at(self, index):
        if 0 <= index < len(self._items):
            return self._items.pop(index)
        raise IndexError("Index out of range")

    def sort_by_name(self, reverse=False):
        self._items.sort(key=lambda u: u.name, reverse=reverse)

    def get_adults(self):
        result = UserCollection(f"{self._name}_adults")
        for user in self._items:
            if user.is_adult():
                result._items.append(user)
        return result

    # ===== MAGIC METHODS =====
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        return f"UserCollection('{self._name}', {len(self._items)} users)"