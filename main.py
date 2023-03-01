import uvicorn
import firebase_admin
import pyrebase
import json

from firebase_admin import credentials, auth
from firebase_admin.auth import UserRecord
from firebase_admin._auth_utils import EmailAlreadyExistsError, UserNotFoundError

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from util.firebase import firebase_config, firebase_credentials
from util.user import user_details

cred = credentials.Certificate(json.loads(firebase_credentials))
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.loads(firebase_config))

app = FastAPI()
ALLOW_ALL = ["*"]

app.add_middleware(
   CORSMiddleware,
   allow_origins=ALLOW_ALL,
   allow_credentials=True,
   allow_methods=ALLOW_ALL,
   allow_headers=ALLOW_ALL
)
 
# signup endpoint
@app.post("/signup", include_in_schema=False)
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

# login endpoint
@app.post("/login", include_in_schema=False)
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

@app.get("/user", include_in_schema=False)
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
        raise HTTPException(detail={ "message": "An unknown error has occurred. Please try again." }, status_code=400) 

# ping endpoint
@app.post("/verify-user", include_in_schema=False)
async def validate(request: Request):
   # headers is a dictionary of type Headers object
   headers = request.headers

   idToken = headers.get("authorization")

   user = auth.verify_id_token(idToken)
   return user

if __name__ == "__main__":
    uvicorn.run("main:app", port=1234, reload=True)