from fastapi import APIRouter, Request, status

from firebase_admin import auth
from firebase_admin.auth import UserRecord

from firebase_app import pb

from util.responses import http_response, raise_exception

router = APIRouter()

@router.post("/login")
async def login(request: Request):
    req = await request.json()
    email = req.get("email")
    password = req.get("password")

    try:
        user: UserRecord = auth.get_user_by_email(email)
        if not user.email_verified:
            raise ValueError("Email must be verified in order to login.")
    except ValueError as exception:
        raise_exception(exception, status.HTTP_400_BAD_REQUEST)
    
    try:
        session: dict[str, str] = pb.auth().sign_in_with_email_and_password(email, password)
        body = { "session": session }
        return http_response(body, status.HTTP_200_OK)
    except Exception as exception:
        raise_exception(exception, status.HTTP_400_BAD_REQUEST)
