from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from firebase_admin import auth
from firebase_admin._auth_utils import UserNotFoundError
from firebase_admin.auth import UserRecord

from util.user import user_details

router = APIRouter(prefix="/user")

@router.get("")
async def getUserByEmail(request: Request):
    req = await request.json()
    email = req.get("email")
    
    if not email:
        raise HTTPException(detail={ "message": "An email address is required for lookup." }, status_code=400)
    
    try:
        user: UserRecord = auth.get_user_by_email(email)
        return JSONResponse(content={ "user": user_details(user) }, status_code=200)
    except UserNotFoundError:
        raise HTTPException(detail={ "message": "No user exists with this email address." }, status_code=400)
    except Exception as e:
        raise HTTPException(
            detail={ 
            	"message": "An unknown error has occurred.",
                "details": str(e)
            },
            status_code=400
        )
    

# ping endpoint to verify an idToken to return a user
@router.post("/verify")
async def validate(request: Request):
   # headers is a dictionary of type Headers object
   headers = request.headers

   idToken = headers.get("authorization")

   user = auth.verify_id_token(idToken)
   return user