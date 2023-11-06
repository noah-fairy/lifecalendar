import uuid

from src.appl.dto import Resp
from src.domain.repo.i_db_context import IDBContext
from src.domain.repo.i_user_repo import IUserRepo


class SignInPasswordResp(Resp):
    access_token: uuid.UUID


class SignInPassword:
    def __init__(self, db_context: IDBContext, user_repo: IUserRepo) -> None:
        self.db_context = db_context
        self.user_repo = user_repo

    def run(self, email: str, password: str) -> SignInPasswordResp:
        with self.db_context.begin_tx():
            user = self.user_repo.get_by_email_or_error(email)
            user.authenticate_with_password(password)
            return SignInPasswordResp(access_token=user.session.id)
