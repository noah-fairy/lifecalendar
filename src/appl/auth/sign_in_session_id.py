import uuid

from src.appl.dto import Resp
from src.domain.entity.auth import InvalidSessionIDError
from src.domain.repo.i_db_context import IDBContext
from src.domain.repo.i_user_repo import IUserRepo


class SignInSessionIDResp(Resp):
    user_id: uuid.UUID


class SignInSessionID:
    def __init__(self, db_context: IDBContext, user_repo: IUserRepo) -> None:
        self.db_context = db_context
        self.user_repo = user_repo

    def run(self, session_id: uuid.UUID) -> SignInSessionIDResp:
        with self.db_context.begin_tx():
            user = self.user_repo.get_by_session_id(session_id)
            if user is None:
                raise InvalidSessionIDError

            user.authenticate()
            return SignInSessionIDResp(user_id=user.id)
