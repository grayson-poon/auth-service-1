from fastapi import APIRouter, Request, status

from firebase_admin import auth
from firebase_admin.auth import UserRecord

from util.user import user_details
from util.responses import http_response, raise_exception


router = APIRouter()

@router.post("/signup")
async def signup(request: Request):
    req = await request.json()
    email = req.get("email")
    password = req.get("password")

    if not email or not password:
        exception = Exception("An email and password are required to sign up for an account.")
        raise_exception(exception, status.HTTP_400_BAD_REQUEST)

    try:
        # create user in Firebase
        user: UserRecord = auth.create_user(email=email, password=password)

        body = {
            "message": "Successfully signed up.",
            "user": user_details(user)
        }
        return http_response(body, status.HTTP_200_OK)
    except Exception as exception:
        raise_exception(exception, status.HTTP_400_BAD_REQUEST)
