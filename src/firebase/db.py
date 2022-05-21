import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

path = os.path.dirname(os.path.abspath("src"))

firebase_cred = credentials.Certificate(path + '/certificate.json')

firebase_admin.initialize_app(firebase_cred)

db = firestore.client()