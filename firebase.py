import os, json

from dotenv import load_dotenv
load_dotenv()

firebase_credentials = json.dumps({
    "type": "service_account",
    "project_id": "user-management-api-1",
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
    "client_email": "firebase-adminsdk-jdm4m@user-management-api-1.iam.gserviceaccount.com",
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-jdm4m%40user-management-api-1.iam.gserviceaccount.com"
})

firebase_config = json.dumps({
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": "user-management-api-1.firebaseapp.com",
    "projectId": "user-management-api-1",
    "storageBucket": "user-management-api-1.appspot.com",
    "messagingSenderId": os.getenv("MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("MEASUREMENT_ID"),
    "databaseURL": os.getenv("DATABASE_URL")
})