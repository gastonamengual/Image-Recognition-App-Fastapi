from dataclasses import dataclass

import firebase_admin
from firebase_admin import credentials, firestore

from app.models.user import User


@dataclass
class FirestoreConnector:
    def __post_init__(self):  # TODO fix url to be variable
        cred = credentials.Certificate(
            "/Users/gastonamengual/Library/Mobile Documents/com~apple~CloudDocs/Documents/Software/Projects/Image-Recognition-App-Fastapi/firebase.json"
        )
        firebase_admin.initialize_app(cred)

    @property
    def _db(self):
        return firestore.client()

    def add_user(self, username):
        doc_ref = self._db.collection("users").document()
        doc_ref.set(
            {
                "username": username,
            }
        )

    def get_all_users(self) -> list[User]:
        users = []
        docs = self._db.collection("users").stream()
        for doc in docs:
            user = User(username=doc.to_dict()["username"])
            users.append(user)
        return users
