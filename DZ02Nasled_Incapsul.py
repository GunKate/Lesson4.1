#Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа. Администраторы, помимо обычных данных пользователей, имеют дополнительный
# уровень доступа и могут добавлять или удалять пользователя из системы.

#Требования:

#1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).

#2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).

#3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы)

class User:
    def __init__(self, user_id, name, access_level='user'):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level

    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_access_level(self):
        return self.__access_level

    def set_name(self, name):
        self.__name = name

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def __str__(self):
        return f"Пользователь (ID: {self.__user_id}, Имя: {self.__name}, Уровень доступа: {self.__access_level})"

class Admin(User):
    def __init__(self, user_id, name, admin_access_level='admin'):
        super().__init__(user_id, name, admin_access_level)
        self.__admin_access_level = admin_access_level

    def add_user(self, user_list, user):
        if isinstance(user, User):
            user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print(f"Ошибка: неверный пользователь.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь с ID {user_id} успешно удален из списка.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def __str__(self):
        return f"Admin(ID: {self.get_user_id()}, Name: {self.get_name()}, Access Level: {self.__admin_access_level})"


# Пример использования
user_list = []

# Создание обычных пользователей
user1 = User(1, 'Таня')
user2 = User(2, 'Уля')

# Создание администратора
admin = Admin(3, 'Кирилл')

# Добавление пользователей
admin.add_user(user_list, user1)
admin.add_user(user_list, user2)

# Печать списка пользователей
for user in user_list:
    print(user)

# Удаление пользователя
admin.remove_user(user_list, 1)

# Печать списка пользователей после удаления
for user in user_list:
    print(user)