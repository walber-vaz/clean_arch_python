from abc import ABC, abstractmethod


class UserFind(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> dict:
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> dict:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> dict:
        pass
