from pydantic import BaseModel, model_validator

from gamr_backend_service.models.errors import UserBlank


class User(BaseModel):
    username: str

    @model_validator(mode="after")
    def username_not_blank(self):
        if not self.username:
            raise UserBlank
        return self
