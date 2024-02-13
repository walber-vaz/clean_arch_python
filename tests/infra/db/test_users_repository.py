from src.infra.db.repositories.users_repository import UsersRepository

# from src.infra.db.settings.connection import DBConnectionHandler


def test_insert_user():
    mocked_user = {
        "name": "Any Name",
        "password": "password",
        "email": "any@email.com",
        "role": "user",
    }

    UsersRepository().insert(
        name=mocked_user.get("name"),
        password=mocked_user.get("password"),
        email=mocked_user.get("email"),
        role=mocked_user.get("role"),
    )
