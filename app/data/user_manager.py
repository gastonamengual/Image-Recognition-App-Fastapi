from dataclasses import dataclass, field

from app.auth.exceptions import (
    UserNotExists,
)
from app.database_connector import AbstractDatabaseConnector, FirestoreConnector
from app.models.user import User


@dataclass
class UserManager:
    db_connector: AbstractDatabaseConnector = field(default_factory=FirestoreConnector)  # type: ignore

    def validate_user_exists(self, user: User):
        users = self.db_connector.get_all_users()
        user_exists = any(
            user for found_user in users if user.username == found_user.username
        )
        if not user_exists:
            raise UserNotExists
