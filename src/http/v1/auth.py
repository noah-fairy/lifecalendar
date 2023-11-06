import uuid
from typing import Annotated, Literal

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from src.appl.auth.sign_in_password import SignInPassword, SignInPasswordResp
from src.appl.auth.sign_out import SignOut
from src.appl.auth.sign_up import SignUp, SignUpResp
from src.appl.container import container
from src.http.auth import get_user_id

api_router_auth = APIRouter(prefix="/auth")


class SignUpReq(BaseModel):
    email: str
    password: str
    password_confirm: str


@api_router_auth.post("/sign-up", response_model=SignUpResp)
async def sign_up(req: SignUpReq):
    return container.resolve(SignUp).run(req.email, req.password, req.password_confirm)


class SignInPasswordReq(BaseModel):
    email: str
    password: str


@api_router_auth.post("/sign-in-password", response_model=SignInPasswordResp)
async def sign_in_password(req: SignInPasswordReq):
    return container.resolve(SignInPassword).run(req.email, req.password)


class SignInPasswordFastAPITokenResp(BaseModel):
    access_token: str
    token_type: Literal["bearer"]


@api_router_auth.post(
    "/sign-in-password/fastapi-token", response_model=SignInPasswordFastAPITokenResp
)
async def sign_in_password_fastapi_token(
    req: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> SignInPasswordFastAPITokenResp:
    resp = container.resolve(SignInPassword).run(req.username, req.password)
    return SignInPasswordFastAPITokenResp(
        access_token=str(resp.session_id), token_type="bearer"
    )


@api_router_auth.post("/sign-out")
async def sign_out(user_id: uuid.UUID = Depends(get_user_id)):
    container.resolve(SignOut).run(user_id)
