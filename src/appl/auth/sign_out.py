import uuid

from src.domain.repo.i_db_context import IDBContext
from src.domain.repo.i_user_repo import IUserRepo


class SignOut:
    def __init__(self, db_context: IDBContext, user_repo: IUserRepo) -> None:
        self.db_context = db_context
        self.user_repo = user_repo

    def run(self, user_id: uuid.UUID) -> None:
        with self.db_context.begin_tx():
            user = self.user_repo.get_or_error(user_id)
            user.unauthenticate()
