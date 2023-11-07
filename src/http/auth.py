import uuid

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from src.appl.auth.sign_in_session_id import SignInSessionID
from src.appl.container import container

oauth2_password_bearer = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/sign-in-password/fastapi-token"
)


async def get_user_id(token: str = Depends(oauth2_password_bearer)) -> uuid.UUID:
    sign = container.resolve(SignInSessionID)
    resp = sign.run(uuid.UUID(token))
    return resp.user_id
