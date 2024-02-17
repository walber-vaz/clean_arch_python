from abc import ABC, abstractmethod

from src.infra.db.entities.users import Users


class UsersRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, name: str, password: str, email: str, role: str) -> Users:
        pass

    @abstractmethod
    def select(self, id: int) -> list[Users]:
        pass
