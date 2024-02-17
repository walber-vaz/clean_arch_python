from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.use_cases.user_find import UserFind as UserFindInterface


class UserFind(UserFindInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find_by_id(self, user_id: int) -> list:
        pass
