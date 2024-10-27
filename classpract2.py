class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль.
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm and len(password) >= 8 and any(char.isupper() for char in password):
            self.password = password
        else:
            raise AttributeError("Пароль должен содержать 8 символов и хотя бы одну заглавную букву.")

class Database:
    """
    Класс, сохраняющий логин и пароль пользователя в словарь (ключ:значение)
    """
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


if __name__ == '__main__':
    data = Database()
    while True:
        try:
            choice = input("Приветствую! Выберите действие:\n1 - Вход\n2 - Регистрация\nВаш выбор: ")
            if choice == '2':
                login = input("Введите логин: ")
                password = input("Введите пароль: ")
                if login in data.data and password == data.data[login]:
                    print("Вы успешно вошли!")
                    break
                else:
                    print("Неверный логин или пароль!")
            elif choice == '2':
                user = User(input('Введите логин: '), password := input('Введите пароль: '),
                            password2 := input('Подтвердите пароль: '))
                # Если пароли не совпадают:
                if password != password2:
                    # Но перед этим выведем строку о том, что пароли не совпадают
                    print("Пароли не совпадают!")
                    # Мы выходим из программы
                    print("Пароли не совпадают! Попробуйте снова.")
                    continue
                else:
                    print(f"Пользователь {user.username} успешно добавлен!")
                data.add_user(user.username, user.password)
            print(f"Все пользователи: {data.data}")
        except AttributeError as error_message:
            print(error_message)

        cont = input("Продолжить?\n1 - Да\n2 - Нет\nВаш ответ: ")
        if cont != '1':
            break
