import uuid

from src.appl.dto import Resp
from src.domain.entity.auth import User
from src.domain.repo.i_db_context import IDBContext
from src.domain.repo.i_user_repo import IUserRepo


class SignUpResp(Resp):
    access_token: str


class SignUp:
    def __init__(self, db_context: IDBContext, user_repo: IUserRepo) -> None:
        self.db_context = db_context
        self.user_repo = user_repo

    def run(self, email: str, password: str, password_confirm: str) -> SignUpResp:
        with self.db_context.begin_tx():
            user = User.create(email, password, password_confirm)
            self.user_repo.save(user)
            return SignUpResp(access_token=user.session.token)
