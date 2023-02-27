import uvicorn
import firebase_admin
import pyrebase
import json

from firebase_admin import credentials, auth
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from firebase import firebase_config, firebase_credentials

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
    email = req["email"]
    password = req["password"]

    if email is None or password is None:
        return HTTPException(detail={ "message": "Error! Missing Email or Password" }, status_code=400)

    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        return JSONResponse(content={"message": f"Successfully created user {user.uid}"}, status_code=200)    
    except:
        return HTTPException(detail={"message": "Error Creating User"}, status_code=400)

# login endpoint
@app.post("/login", include_in_schema=False)
async def login(request: Request):
    req = await request.json()
    email = req["email"]
    password = req["password"]

    try:
        user = pb.auth().sign_in_with_email_and_password(email, password)
        jwt = user["idToken"]
        return JSONResponse(content={"token": jwt}, status_code=200)
    except:
        return HTTPException(detail={"message": "Incorrect email or password."}, status_code=400)

# ping endpoint
@app.post("/ping", include_in_schema=False)
async def validate(request: Request):
   # headers is a dictionary of type Headers object
   headers = request.headers

   jwt = headers.get("authorization")
   print(f"jwt: {jwt}")

   user = auth.verify_id_token(jwt)
   return user.get("uid")

if __name__ == "__main__":
    uvicorn.run("main:app")