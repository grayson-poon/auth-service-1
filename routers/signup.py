from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from firebase_admin import auth
from firebase_admin.auth import UserRecord
from firebase_admin._auth_utils import EmailAlreadyExistsError

from util.user import user_details

router = APIRouter()

@router.post("/signup")
async def signup(request: Request):
    req = await request.json()
    email = req.get("email")
    password = req.get("password")

    if not email or not password:
        raise HTTPException(detail={ "message": "An email and password are required to sign up for an account." }, status_code=400)

    try:
        user: UserRecord = auth.create_user(
            email=email,
            password=password
        )
        return JSONResponse(
            content={
                "message": "Successfully created user.",
                "user": user_details(user)
            },
            status_code=200
        )
    except EmailAlreadyExistsError:
        raise HTTPException(detail={ "message": "A user already exists with this email address. If you have an account, please sign in. Otherwise, use a different email address." }, status_code=400)
    except ValueError as value_error:
        raise HTTPException(detail={ "message": str(value_error) }, status_code=400)
    except Exception as e:
        raise HTTPException(detail={ "message": "An unknown error occurred, please try again", "error": str(e) }, status_code=400)