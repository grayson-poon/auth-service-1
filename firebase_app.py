import pyrebase, json, firebase_admin
from firebase_admin import credentials
from util.fb import firebase_config, firebase_credentials

cred = credentials.Certificate(json.loads(firebase_credentials))
firebase = firebase_admin.initialize_app(cred)
pb = pyrebase.initialize_app(json.loads(firebase_config))