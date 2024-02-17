from abc import ABC, abstractmethod


class UserFind(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> list:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> list:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> list:
        pass
