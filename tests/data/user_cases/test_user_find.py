from src.data.user_cases.user_find import UserFind
from src.infra.db.repositories.users_repository import UsersRepository


def test_find_by_id():
    repo = UsersRepository()
    user_find = UserFind(repo)
