class User:
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age

    def __str__(self):
        return f'User(username={self.username}, email={self.email}, age={self.age})'


class UserAlreadyExistsError(Exception):
    """Исключение, выбрасываемое, если пользователь с таким именем уже существует."""
    pass


class UserNotFoundError(Exception):
    """Исключение, выбрасываемое, если пользователь с указанным именем не найден."""
    pass


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user: User):
        if user.username in self.users:
            raise UserAlreadyExistsError(f"User with username '{user.username}' already exists.")
        self.users[user.username] = user

    def remove_user(self, username: str):
        if username not in self.users:
            raise UserNotFoundError(f"User with username '{username}' not found.")
        del self.users[username]

    def find_user(self, username: str) -> User:
        if username not in self.users:
            raise UserNotFoundError(f"User with username '{username}' not found.")
        return self.users[username]


def main() -> None:
    user_manager = UserManager()

    # Добавление нескольких пользователей
    try:
        user1 = User(username="john_doe", email="john@example.com", age=30)
        user_manager.add_user(user1)
        print(f"Added: {user1}")

        user2 = User(username="jane_doe", email="jane@example.com", age=25)
        user_manager.add_user(user2)
        print(f"Added: {user2}")

        # Добавление пользователя с существующим именем
        user3 = User(username="john_doe", email="john_doe@example.com", age=28)
        user_manager.add_user(user3)
    except UserAlreadyExistsError as e:
        print(f"Error: {e}")

    # Удаление пользователей
    try:
        user_manager.remove_user("jane_doe")
        print("User 'jane_doe' removed.")

        # Удаление несуществующего пользователя
        user_manager.remove_user("alice")
    except UserNotFoundError as e:
        print(f"Error: {e}")

    # Нахождение пользователей
    try:
        user = user_manager.find_user("john_doe")
        print(f"Found: {user}")

        # Нахождение несуществующего пользователя
        user = user_manager.find_user("alice")
    except UserNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()