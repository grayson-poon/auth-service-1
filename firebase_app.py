import pyrebase, json, firebase_admin, os

from firebase_admin import credentials

from dotenv import load_dotenv
load_dotenv()

FIREBASE_PRIVATE_KEY_ID = os.environ.get("FIREBASE_PRIVATE_KEY_ID")
FIREBASE_PRIVATE_KEY = os.environ.get("FIREBASE_PRIVATE_KEY")
FIREBASE_CLIENT_ID = os.environ.get("FIREBASE_CLIENT_ID")

FIREBASE_API_KEY = os.environ.get("FIREBASE_API_KEY")
FIREBASE_MESSAGING_SENDER_ID = os.environ.get("MESSAGING_SENDER_ID")
FIREBASE_APP_ID = os.environ.get("FIREBASE_APP_ID")
FIREBASE_MEASUREMENT_ID = os.environ.get("MEASUREMENT_ID")
DATABASE_URL = os.environ.get("DATABASE_URL")

firebase_credentials = json.dumps({
    "type": "service_account",
    "project_id": "user-management-api-1",
    "private_key_id": FIREBASE_PRIVATE_KEY_ID,
    "private_key": FIREBASE_PRIVATE_KEY,
    "client_email": "firebase-adminsdk-jdm4m@user-management-api-1.iam.gserviceaccount.com",
    "client_id": FIREBASE_CLIENT_ID,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-jdm4m%40user-management-api-1.iam.gserviceaccount.com"
})

firebase_config = json.dumps({
    "apiKey": FIREBASE_API_KEY,
    "authDomain": "user-management-api-1.firebaseapp.com",
    "projectId": "user-management-api-1",
    "storageBucket": "user-management-api-1.appspot.com",
    "messagingSenderId": FIREBASE_MESSAGING_SENDER_ID,
    "appId": FIREBASE_APP_ID,
    "measurementId": FIREBASE_MEASUREMENT_ID,
    "databaseURL": DATABASE_URL
})


cred = credentials.Certificate(json.loads(firebase_credentials))
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.loads(firebase_config))