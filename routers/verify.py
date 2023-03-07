import requests

from fastapi import APIRouter, Request, status

from firebase_app import pb, FIREBASE_API_KEY

from util.responses import http_response, raise_exception


EMAIL_VERIFICATION_API_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_API_KEY}"

router = APIRouter()

@router.post("/verify")
async def verify(request: Request):
    req = await request.json()
    email = req.get("email")
    password = req.get("password")
    
    try:
        # sign in new user and retrieve their session token
        session: dict[str, str] = pb.auth().sign_in_with_email_and_password(email, password)
        id_token: str = session.get("idToken")
        
        # send email verification
        body = {
            "requestType": "VERIFY_EMAIL",
            "idToken": id_token
        }
        requests.post(EMAIL_VERIFICATION_API_URL, json=body)

        # TODO: revoke the generated id_token so its no longer valid
        body = { "message": f"Email verification sent to {email}." }
        return http_response(body, status.HTTP_200_OK)
    except Exception as exception:
        raise_exception(exception, status.HTTP_500_INTERNAL_SERVER_ERROR)
