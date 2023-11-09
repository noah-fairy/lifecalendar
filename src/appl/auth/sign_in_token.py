import uuid

from src.appl.dto import Resp
from src.domain.entity.auth import InvalidAccessTokenError
from src.domain.repo.i_db_context import IDBContext
from src.domain.repo.i_user_repo import IUserRepo


class SignInTokenResp(Resp):
    user_id: uuid.UUID


class SignInToken:
    def __init__(self, db_context: IDBContext, user_repo: IUserRepo) -> None:
        self.db_context = db_context
        self.user_repo = user_repo

    def run(self, token: str) -> SignInTokenResp:
        with self.db_context.begin_tx():
            user = self.user_repo.get_by_token(token)
            if user is None:
                raise InvalidAccessTokenError

            user.authenticate()
            return SignInTokenResp(user_id=user.id)
