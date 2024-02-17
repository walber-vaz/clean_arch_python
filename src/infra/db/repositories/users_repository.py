from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.infra.db.entities.users import Users as UsersEntity
from src.infra.db.settings.connection import DBConnectionHandler


class UsersRepository(UsersRepositoryInterface):
    @classmethod
    def insert(cls, name: str, password: str, email: str, role: str) -> Users:
        with DBConnectionHandler() as db_connection:
            try:
                new_user = UsersEntity(
                    name=name, password=password, email=email, role=role
                )
                if db_connection.session is not None:
                    db_connection.session.add(new_user)
                    db_connection.session.commit()
                    db_connection.session.refresh(new_user)
                    return new_user
                else:
                    raise Exception("DB connection session is None.")
            except Exception as exception:
                if db_connection.session is not None:
                    db_connection.session.rollback()
                raise exception

    @classmethod
    def select(cls, id: int) -> list[Users]:
        with DBConnectionHandler() as db_connection:
            try:
                if db_connection.session is None:
                    raise Exception("DB connection session is None.")
                user = (
                    db_connection.session.query(UsersEntity)
                    .filter(UsersEntity.id == id)
                    .first()
                )
                return user
            except Exception as exception:
                if db_connection.session is not None:
                    db_connection.session.rollback()
                raise exception
