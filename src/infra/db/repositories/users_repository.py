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
                db_connection.session.add(new_user)
                db_connection.session.commit()
                db_connection.session.refresh(new_user)
            except Exception as exception:
                db_connection.session.rollback()
                raise exception
