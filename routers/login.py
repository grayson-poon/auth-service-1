from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from firebase_app import pb

router = APIRouter()

@router.post("/login")
async def login(request: Request):
    req = await request.json()
    email = req.get("email")
    password = req.get("password")

    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        idToken = user.get("idToken")
        return JSONResponse(content={ "idToken": idToken }, status_code=200)
    except:
        raise HTTPException(detail={ "message": "Incorrect email or password." }, status_code=400)
