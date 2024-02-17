from enum import Enum


class Role(Enum):
    ADMIN = "admin"
    USER = "user"


class Users:
    def __init__(
        self, id: int, name: str, password: str, email: str, role: Role
    ) -> None:
        self.id = id
        self.name = name
        self.password = password
        self.email = email
        self.role = role
