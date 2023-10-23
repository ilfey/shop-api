from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import RedirectResponse, JSONResponse

from models import User

router = APIRouter()


@router.get(
    path="/",
    summary="Redirect from index to docs",
)
@router.get(
    path="/index",
    summary="Redirect from index to docs",
)
def index() -> RedirectResponse:
    return RedirectResponse("/docs")


@router.post(
    path="/refresh",
    summary="Refresh tokens",
)
def refresh() -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "access_token": "new_access_token",
        },
    )


@router.post(
    path="/login",
    summary="Login",
)
def login() -> JSONResponse:
    return JSONResponse(
        status_code=200,
        content={
            "access_token": "access_token",
            "refresh_token": "refresh_token",
        },
    )


@router.post(
    path="/register",
    summary="Register",
)
def register() -> JSONResponse:
    JSONResponse(
        status_code=200,
        content={
            "ok": True,
        },
    )
