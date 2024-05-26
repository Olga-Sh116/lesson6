class User:
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'


    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name
class Admin(User):

    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._users = []

    def add_user(self, user):
        if not isinstance(user, User):
            raise ValueError("Можно добавлять только экземпляры класса User.")
        self._users.append(user)
        print(f"Пользователь {user.get_name()} добавлен.")

    def remove_user(self, user_id):
        user_to_remove = None
        for user in self._users:
            if user.get_user_id() == user_id:
                user_to_remove = user
                break
        if user_to_remove:
            self._users.remove(user_to_remove)
            print(f"Пользователь {user_to_remove.get_name()} удален.")
        else:
            print("Пользователь не найден.")

    def list_users(self):
        return [user.get_name() for user in self._users]


admin = Admin(1, "Admin")

# Создание обычных пользователей
user1 = User(2, "Ольга")
user2 = User(3, "Виталий")

admin.add_user(user1)
admin.add_user(user2)

#
print("Пользователи:", admin.list_users())

admin.remove_user(2)

print("Пользователи:", admin.list_users())
