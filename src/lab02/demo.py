from model import User
from collection import UserCollection

u1 = User("Diego", "O+", 75.5, 25, "diego@email.com", "Madrid")
u2 = User("Ana", "A+", 60.0, 30, "ana@email.com", "Barcelona")

collection = UserCollection()

collection.add(u1)
collection.add(u2)

print("Usuarios en la colección:")
for user in collection.get_all():
    print(user)