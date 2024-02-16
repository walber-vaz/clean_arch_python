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
        name=str(mocked_user.get("name")),
        password=str(mocked_user.get("password")),
        email=str(mocked_user.get("email")),
        role=str(mocked_user.get("role")),
    )
