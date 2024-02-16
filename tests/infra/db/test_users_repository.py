from pytest import mark
from sqlalchemy import text

from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.settings.connection import DBConnectionHandler

db_connection = DBConnectionHandler()
connection = db_connection.get_engine().connect()


@mark.skip(reason="Sensitive data")
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

    sql = """
        SELECT id, name, email, role FROM users
        WHERE name = "{}"
        AND email = "{}"
        AND role = "{}";
    """.format(
        mocked_user.get("name"),
        mocked_user.get("email"),
        mocked_user.get("role"),
    )

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.name == mocked_user.get("name")
    assert registry.email == mocked_user.get("email")
    assert registry.role == mocked_user.get("role")

    connection.execute(
        text(
            f"""
                DELETE FROM users
                WHERE id = {registry.id};
            """
        )
    )
    connection.commit()


@mark.skip(reason="Sensitive data")
def test_select_user():
    mocked_user = {
        "name": "Any Name 2",
        "password": "password",
        "email": "any2@email.com",
        "role": "user",
    }

    sql = f"""
        INSERT INTO users (name, password, email, role)
        VALUES (
            "{mocked_user.get("name")}",
            "{mocked_user.get("password")}",
            "{mocked_user.get("email")}",
            "{mocked_user.get("role")}"
        );
    """

    res = connection.execute(text(sql))
    connection.commit()
    registry = res.lastrowid

    user_repository = UsersRepository()
    query = user_repository.select(registry)

    assert query.id == registry
    assert query.name == mocked_user.get("name")
    assert query.email == mocked_user.get("email")
    assert query.role == mocked_user.get("role")

    connection.execute(
        text(
            f"""
                DELETE FROM users
                WHERE id = {registry};
            """
        )
    )
    connection.commit()
