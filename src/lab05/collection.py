class UserCollection:

    def __init__(self, name="Users"):
        self._name = name
        self._items = []

    def add(self, user):
        self._items.append(user)

    def get_all(self):
        return self._items

    def filter_by(self, predicate):

        filtered = list(filter(predicate, self._items))

        result = UserCollection(f"{self._name}_filtered")
        result._items = filtered

        return result

    def sort_by(self, key_func):

        sorted_items = sorted(self._items, key=key_func)

        result = UserCollection(f"{self._name}_sorted")
        result._items = sorted_items

        return result

    def apply(self, func):

        applied = list(map(func, self._items))

        result = UserCollection(f"{self._name}_applied")
        result._items = applied

        return result

    def __iter__(self):
        return iter(self._items)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        return f"UserCollection('{self._name}', {len(self._items)} users)"