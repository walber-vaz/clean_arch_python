from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler


class UsersRepository:
    @classmethod
    def insert(cls, name: str, password: str, email: str, role: str) -> None:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersEntity(
                    name=name, password=password, email=email, role=role
                )
                if db_connection.session is not None:
                    db_connection.session.add(new_user)
                    db_connection.session.commit()
                    db_connection.session.refresh(new_user)
                else:
                    raise Exception("DB connection session is None.")
            except Exception as exception:
                if db_connection.session is not None:
                    db_connection.session.rollback()
                raise exception
